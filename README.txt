Author: Barış Deniz Sağlam

## Requirements
Python 2.7.11

## Usage
./kmer_counter.py --filename big.fastq --kmersize 30 --topcount 25

Output:
The program prints a list of kmer_substring-count tuples such as

[('TTTTTTTTTT', 1234), ('AAAAAAAAAA', 1141), ('GGGGGGGGGG', 273), ('ACACACACAC', 177), ('CACACACACA', 176), ('TTTTCTTTTT', 142), ('AAAAAAAAAG', 127), ('ATTTTTTTTT', 123), ('GTGTGTGTGT', 123), ('CTTTTTTTTT', 123), ('TGTGTGTGTG', 123), ('TTTTTAAAAA', 118), ('TTTTGTTTTT', 115), ('TTTTTTTTTA', 115), ('TTTTTCTTTT', 115), ('AAAAAAAAAT', 102), ('TTTTTGTTTT', 101), ('AAAAACAAAA', 100), ('TTTCTTTTTT', 100), ('TTTTTTTTTC', 98), ('TTTTTTCTTT', 98), ('AAATAAATAA', 96), ('TCTTTTTTTT', 95), ('CAAAAAAAAA', 95), ('TTTTATTTTT', 95)]