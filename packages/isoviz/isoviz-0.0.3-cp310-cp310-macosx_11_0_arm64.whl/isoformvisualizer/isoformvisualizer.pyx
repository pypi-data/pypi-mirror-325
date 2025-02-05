import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np
import re
import sys
import argparse
import matplotlib.ticker as ticker
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import Normalize
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.cm import ScalarMappable
import matplotlib.pyplot as plt

def parse_metadata(meta_data):
    with open(meta_data) as f:
        lines = f.readlines()
    current_section = None
    sample_meta = dict()
    config_meta = dict()
    for line in lines:
        line = line.strip()
        if line.startswith("[") and line.endswith("]"):
            current_section = line[1:-1]

        elif current_section == "sample":
            if line.startswith("#"):
                ctrl_trgt = line.lstrip("#")
                ctrl_trgt = [i.strip() for i in ctrl_trgt.split(",")]
                ctrl_trgt_table = dict()
                for pair in ctrl_trgt:
                    CT, var = pair.split("=")
                    ctrl_trgt_table[var.strip()] = CT.strip().lower()
            else:
               if line:
                   if "\t" in line:
                       i = line.split("\t")
                       sample_meta[i[0]] = i[1]
                   else:
                       i = line.split(",")
                       sample_meta[i[0]] = i[1]

        elif current_section == "config":
            if line.startswith("#"):
                key, value = line.split("=")
                key = key.lstrip("#")
                key = key.strip()
                value = value.strip()
                if key == 'qval':
                    value = float(value)
                elif key == 'order':
                    value = [i.strip() for i in value.split(',')]
                config_meta[key] = value
    return sample_meta, config_meta, ctrl_trgt_table


def get_isoform_model(gtf_file):
    transcripts = {}        # for exons
    transcripts_CDS = {}    # for CDS
    with open(gtf_file) as gtf:
        for line in gtf:
            if line.startswith('#'):
                continue
            fields = line.strip().split('\t')
            chrom, source, feature, start, end, score, strand, frame, attributes = fields
            chrom = chrom.replace("chr","")
            feature = feature.lower()
            if feature == 'exon':
                # 属性フィールドのパース
                attr_dict = {match.group(1): match.group(2) for match in re.finditer(r'(\S+)\s+"([^"]+)"', attributes)}
                transcript_id = attr_dict.get('transcript_id')
                if transcript_id not in transcripts:
                    if strand == "+":
                        transcripts[transcript_id] = [[], 1, chrom]
                    else:
                        transcripts[transcript_id] = [[], -1, chrom]
                transcripts[transcript_id][0].append((int(start), int(end)))
            if feature == 'cds':
                attr_dict = {match.group(1): match.group(2) for match in re.finditer(r'(\S+)\s+"([^"]+)"', attributes)}
                transcript_id = attr_dict.get('transcript_id')
                if transcript_id not in transcripts_CDS:
                    if strand == "+":
                        transcripts_CDS[transcript_id] = [[], 1, chrom]
                    else:
                        transcripts_CDS[transcript_id] = [[], -1, chrom]
                transcripts_CDS[transcript_id][0].append((int(start), int(end)))
    return transcripts, transcripts_CDS


def formatting_isoform_model(transcripts_data, transcripts, annot):
    if annot == "annotated":
        for transcript_id, exons in transcripts.items():
            start = min([i[0] for i in exons[0]])
            end = max(i[1] for i in exons[0])
            transcripts_data.append({'id': transcript_id, 'exons': exons[0], 'strand': exons[1], 'seq_region_name': exons[2], 'start': start, 'end': end, 'is_novel': False})
    elif annot == "unannotated":
        for transcript_id, exons in transcripts.items():
            start = min([i[0] for i in exons[0]])
            end = max(i[1] for i in exons[0])
            transcripts_data.append({'id': transcript_id, 'exons': exons[0], 'strand': exons[1], 'seq_region_name': exons[2], 'start': start, 'end': end, 'is_novel': True})
    elif annot == "cds":
        for i in range(len(transcripts_data)):
            isomodel = transcripts_data[i]
            tx_id = isomodel['id']
            if tx_id in transcripts:
                # CDSを持つアイソフォーム
                transcripts_data[i]['cds'] = transcripts[tx_id][0]
            else:
                # CDSを持たないアイソフォーム
                transcripts_data[i]['cds'] = []
    return transcripts_data


def get_expression_data(expression_file, transcripts_data, ctrl_trgt_table, sample_meta):
    df = pd.read_csv(expression_file, sep="\t", header=0)
    targets = [i['id'] for i in transcripts_data]
    filtered_df = df[df.iloc[:, 0].isin(targets)]
    GROUP_0, GROUP_1 = dict(), dict()
    for index, row in filtered_df.iterrows():
        tx_id = row.iloc[0]
        group_0, group_1 = [], []
        for sample in filtered_df.columns[1:]:
            expression = row[sample]
            group_symbol = sample_meta[sample]
            if ctrl_trgt_table[group_symbol] == 'control':
                group_0.append(expression)
            elif ctrl_trgt_table[group_symbol] == 'target':
                group_1.append(expression)

        GROUP_0[tx_id] = group_0
        GROUP_1[tx_id] = group_1

    # integrate expression data to main data
    for i in range(len(transcripts_data)):
        transcripts_data[i]['group0_exp'] = GROUP_0[transcripts_data[i]['id']]
        transcripts_data[i]['group1_exp'] = GROUP_1[transcripts_data[i]['id']]

    return transcripts_data


def get_det_data(det_file, transcripts_data):
    det_data = dict()
    with open(det_file) as f:
        for line in f:
            line = line.strip()
            if not line.startswith("#"):
                if "\t" in line:
                    col = line.split("\t")
                else:
                    col = line.split(",")
                tx_id = col[0]
                logFC = float(col[1])
                qval = float(col[2])
                det_data[tx_id] = [logFC, qval]

    # integrate det data to main data
    for i in range(len(transcripts_data)):
        transcripts_data[i]['det'] = det_data[transcripts_data[i]['id']]

    return transcripts_data

def prepare_ax1(transcripts_data, ax1, gene_name):
    # AX1: 各アイソフォームを視覚化
    y_positions = []
    MIN = min(transcripts_data, key=lambda x: x['start'])['start']
    MAX = max(transcripts_data, key=lambda x: x['end'])['end']
    transcripts_data = transcripts_data[::-1]
    for i, transcript_data in enumerate(transcripts_data):
        y_positions.append(i)
        start = transcript_data['start']
        end = transcript_data['end']
        # === Known transcript の描画 ===
        if not transcript_data['is_novel']:

            # 1. 背骨 を描画 (エクソンの背面に灰色の矢印付きの線分を描画)
            strand = transcript_data['strand']
            arrow_direction = "right" if strand == 1 else "left"
            y_pos = i
            interval = (MAX-MIN)//10
            x_positions = np.arange(start, end, interval)
            x_positions = x_positions[1:-1]

            ax1.annotate('', xy=(end, y_pos), xytext=(start, y_pos), arrowprops=dict(arrowstyle="-", color='gray', lw=1))
            if arrow_direction == "right":
                for x in x_positions:
                    ax1.scatter(x, y_pos, marker=">", color="gray", s=10)
            else:
                for x in x_positions:
                    ax1.scatter(x, y_pos, marker="<", color="gray", s=10)

            # 2. exon を描画（少し濃い水色で描画）
            for exon in transcript_data['exons']:
                exon_start = exon[0]
                exon_end = exon[1]
                # CDS以外の部分を新しい色で描画
                ax1.add_patch(patches.Rectangle((exon_start, i - 0.1), exon_end - exon_start, 0.2, color='#B3C8CF'))

            # 3. CDS を描画
            for cds in transcript_data['cds']:
                cds_start = cds[0]
                cds_end = cds[1]
                ax1.add_patch(patches.Rectangle((cds_start, i - 0.2), cds_end - cds_start, 0.4, color='#6D868E'))

            # CDS情報を描画（もし存在する場合）
            cds_info = transcript_data.get('Translation')
            if cds_info:
                cds_start = cds_info['start']
                cds_end = cds_info['end']
        
                # エクソンにCDS部分が含まれるか確認し、その領域だけ強調
                for exon in transcript_data['Exon']:
                    exon_start = exon['start']
                    exon_end = exon['end']
            
                    # CDSの範囲がエクソンに重なる部分だけ高さを変える
                    if exon_start <= cds_end and exon_end >= cds_start:
                        cds_region_start = max(exon_start, cds_start)
                        cds_region_end = min(exon_end, cds_end)
                        # 柔らかい青色で描画（エクソンの上に描画）
                        ax1.add_patch(patches.Rectangle((cds_region_start, i - 0.2), cds_region_end - cds_region_start, 0.4, color='#6699FF'))

        # === Novel transcript の描画 ===
        elif transcript_data['is_novel']:
            #遺伝子の向きに合わせた線分を描画
            strand = transcript_data['strand']
            arrow_direction = "right" if strand == 1 else "left"
            y_pos = i
            interval = (MAX-MIN)//10
            x_positions = np.arange(start, end, interval)
            x_positions = x_positions[1:-1]
            
            ax1.annotate('', xy=(end, y_pos), xytext=(start, y_pos), arrowprops=dict(arrowstyle="-", color='gray', lw=1))
            if arrow_direction == "right":
                for x in x_positions:
                    ax1.scatter(x, y_pos, marker=">", color="gray", s=10)
            else:
                for x in x_positions:
                    ax1.scatter(x, y_pos, marker="<", color="gray", s=10)


            # エクソン情報を描画（少し濃い水色で描画）
            for exon in transcript_data['exons']:
                exon_start = exon[0]
                exon_end = exon[1]
                ax1.add_patch(patches.Rectangle((exon_start, i - 0.1), exon_end - exon_start, 0.2, color='#FFC94A'))

    # 軸と図の設定
    space = int((MAX-MIN)/20)
    ax1.set_xlim(MIN - space, MAX + space)
    ax1.set_ylim(-0.5, len(transcripts_data) - 0.5)
    ax1.set_xlabel(f'Chr{transcript_data["seq_region_name"]}')
    ax1.set_title(gene_name)
    ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
    ax1.set_yticks(y_positions)
    transcripts = [i['id'] for i in transcripts_data]
    ax1.set_yticklabels(transcripts)
    return ax1

def prepare_ax2(transcripts_data, ax2, config_meta):
    # AX2: 箱ひげ図
    transcripts_data = transcripts_data[::-1]
    transcripts = [i['id'] for i in transcripts_data]
    labels = []
    data = []
    for i in range(len(transcripts_data)):
        tx_id = transcripts_data[i]['id']
        data.append(transcripts_data[i]['group1_exp'])
        data.append(transcripts_data[i]['group0_exp'])
        labels.append(f'{tx_id}_1')
        labels.append(f'{tx_id}_0')

    # プロットの位置調整
    positions = []
    for i, name in enumerate(transcripts):
        positions.extend([i*3+1, i*3+1.6])

    # 箱ひげ図をプロット
    ax2_outlier = False
    if 'ax2_outlier' in config_meta:
        if config_meta['ax2_outlier'] == 'True':
            ax2_outlier = True
    boxplot = ax2.boxplot(data, positions=positions, vert=False, patch_artist=True, showfliers=ax2_outlier)

    # 色を設定 (奇数: 薄い, 偶数: 濃い)
    colors = ['lightgray' if idx % 2 == 1 else 'gray' for idx in range(len(data))]
    for patch, color in zip(boxplot['boxes'], colors):
        patch.set_facecolor(color)

    # 詳細設定
    for median in boxplot['medians']:
        median.set_color('black')  # 色を黒に設定

    ax2_xlabel = ""
    if 'ax2_xlabel' in config_meta:
        ax2_xlabel = config_meta['ax2_xlabel']
    ax2.set_yticklabels([])
    ax2.tick_params(axis='y', length=0)
    ax2.set_xlabel(ax2_xlabel)
    return ax2

def prepare_ax3(transcripts_data, config_meta, ax3):
    # AX3: 色塗り
    def color_mapping(nlogqval):
        if nlogqval > 20:
            return 1
        else:
            return 0.3 + nlogqval*0.035
    DET = list()
    for i in range(len(transcripts_data)):
        DET.append([transcripts_data[i]['id']] + transcripts_data[i]['det'])
    qval_threshold = config_meta['qval']
    # カラーマップを設定
    warm_cmap = plt.cm.Reds    # 暖色系
    cold_cmap = plt.cm.Blues   # 寒色系
    # 最大値のスケーリングを計算（色の濃さを調整するため）
    max_value = max(-np.log10(v[2]) for v in DET)
    for i, val in enumerate(DET):
        logFC = DET[i][1]
        qval = DET[i][2]
        # 色の設定
        if qval < qval_threshold:
            if logFC > 0:
                color = warm_cmap(color_mapping(-np.log10(qval)))
            else:
                color = cold_cmap(color_mapping(-np.log10(qval)))
        else:
                color = (0.5, 0.5, 0.5, 0.5)  # Gray
        # 長方形の作図
        rect = patches.Rectangle((0, len(DET) - i - 1), 0.1, 1, facecolor=color, edgecolor='black', linewidth=2)
        ax3.add_patch(rect)

    # 凡例の作成
    reds_colors = [plt.cm.Reds(x) for x in np.linspace(0.3, 1, 128)]
    blues_colors = [plt.cm.Blues(x) for x in np.linspace(0.3, 1, 128)]
    combined_colors = blues_colors[::-1] + reds_colors
    combined_cmap = LinearSegmentedColormap.from_list("CombinedMap", combined_colors)
    norm = Normalize(vmin=0, vmax=1)
    sm = ScalarMappable(cmap=combined_cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax3, orientation='vertical', fraction=0.05, pad=0.01, shrink=0.8)
    cbar.set_label('-log10(q)', rotation=90)
    cbar.set_ticks(np.linspace(0, 1, 5))
    tick_labels = [">20", "10", "0", "10", ">20"]
    cbar.ax.set_yticklabels(tick_labels)

    # Set limits and remove axes for a cleaner look
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, len(DET))
    ax3.axis('off')
    return ax3


def reorder(transcripts_data, meta_data):
    if not 'order' in meta_data:
        tmp_annotated = []
        tmp_unannotated = []
        for tx_data in transcripts_data:
            if tx_data['is_novel'] == False:
                tmp_annotated.append(tx_data)
            else:
                tmp_unannotated.append(tx_data)
        tmp_annotated = sorted(tmp_annotated, key=lambda x:x['id'])
        tmp_unannotated = sorted(tmp_unannotated, key=lambda x:x['id'])
        return tmp_annotated + tmp_unannotated
    else:
        tmp = []
        order = meta_data['order']
        for tx in order:
            for i in transcripts_data:
                if i['id'] == tx:
                    tmp.append(i)
                    break
        return tmp

def plot(transcripts_data, config_meta, gene_name, meta_data):
    # 並び替え
    transcripts_data = reorder(transcripts_data, meta_data)

    # プロットする場所を作成
    fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(20, 5), gridspec_kw={'width_ratios': [10, 10, 2]})

    # prep for ax1
    ax1 = prepare_ax1(transcripts_data, ax1, gene_name)

    # prep for ax2
    ax2 = prepare_ax2(transcripts_data, ax2, config_meta)

    # prep for ax3
    ax3 = prepare_ax3(transcripts_data, config_meta, ax3)

    plt.subplots_adjust(wspace=0.02)
    plt.show()

def visualizer(gene, gtf_annotated, gtf_unannotated, expression_data, det_data, meta_data):
    # metadata
    sample_meta, config_meta, ctrl_trgt_table = parse_metadata(meta_data)

    # raw isoform model: annotated
    model_annotated, model_annotated_CDS = get_isoform_model(gtf_annotated)

    # raw isoform model: unannotated
    model_unannotated, _ = get_isoform_model(gtf_unannotated)

    # formatted isoform model
    transcripts_main_data = list()
    transcripts_main_data = formatting_isoform_model(transcripts_main_data, model_annotated, annot="annotated")
    transcripts_main_data = formatting_isoform_model(transcripts_main_data, model_unannotated, annot="unannotated")
    transcripts_main_data = formatting_isoform_model(transcripts_main_data, model_annotated_CDS, annot="cds")

    # epxression data
    transcripts_main_data = get_expression_data(expression_data, transcripts_main_data, ctrl_trgt_table, sample_meta)

    # det data
    transcripts_main_data = get_det_data(det_data, transcripts_main_data)

    # plot
    plot(transcripts_main_data, config_meta, gene, config_meta)

if __name__ == '__main__':
    # parser
    parser = argparse.ArgumentParser(description='isoformvisualizer')
    parser.add_argument('-gene', '--gene_symbol', type=str, default=None, help='Gene name')
    parser.add_argument('-annot', '--gtf_annotated', type=str, default=None, help='GTF of annotated isoforms')
    parser.add_argument('-unannot', '--gtf_unannotated', type=str, default=None, help='GTF of unannotated isoforms')
    parser.add_argument('-exp', '--expression_data', type=str, default=None, help='Expression data')
    parser.add_argument('-det', '--det_data', type=str, default=None, help='Differential expression data')
    parser.add_argument('-meta', '--meta_data', type=str, default=None, help='metadata')

    args = parser.parse_args()
    gene = args.gene_symbol
    gtf_annotated = args.gtf_annotated
    gtf_unannotated = args.gtf_unannotated
    expression_data = args.expression_data
    det_data = args.det_data
    meta_data = args.meta_data

    visualizer(gene, gtf_annotated, gtf_unannotated, expression_data, det_data, meta_data)
