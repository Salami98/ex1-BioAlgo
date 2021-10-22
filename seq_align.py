import argparse
import numpy as np
from itertools import groupby
import pandas as pd

def fastaread(fasta_name):
    """
    Read a fasta file. For each sequence in the file, yield the header and the actual sequence.
    In Ex1 you may assume the fasta files contain only one sequence.
    You may keep this function, edit it, or delete it and implement your own reader.
    """
    f = open(fasta_name)
    faiter = (x[1] for x in groupby(f, lambda line: line.startswith(">")))
    for header in faiter:
        header = next(header)[1:].strip()
        seq = "".join(s.strip() for s in next(faiter))
        yield header, seq



def score_trace_table(S, T, sigma, align_type):
    trace = [[], []]
    m = len(S)
    n = len(T)
    score_mat = np.array((m,2))





def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('seq_a', help='first file')
    parser.add_argument('seq_b', help='second file')
    parser.add_argument('--align_type', help='Alignment type (e.g. local)', required=True)
    parser.add_argument('--score', help='score_matrix.tsv', default='score_matrix.tsv')
    command_args = parser.parse_args()
    T = fastaread(command_args.seq_a).__next__()[1]
    S = fastaread(command_args.seq_b).__next__()[1]
    sigma_mat = pd.read_csv(command_args.score, delimiter='\t')
    # if command_args.align_type == 'global':
    #     raise NotImplementedError
    # elif command_args.align_type == 'local':
    #     raise NotImplementedError
    # elif command_args.align_type == 'overlap':
    #     raise NotImplementedError
    # print the best alignment and score


if __name__ == '__main__':
    main()
