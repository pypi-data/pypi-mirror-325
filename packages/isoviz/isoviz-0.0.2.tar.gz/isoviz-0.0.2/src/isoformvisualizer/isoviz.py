# handler function
import argparse
from isoformvisualizer.isoformvisualizer import visualizer

def main():
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
