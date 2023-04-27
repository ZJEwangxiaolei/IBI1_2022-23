from Bio import Align
from Bio.Seq import Seq
aligner = Align.PairwiseAligner()
def read_seq_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        sequence = lines[1].replace("\n", "")
    return sequence
seq_cat=read_seq_from_file("/Users/wangxiaolei/IBI1_2022-23/Practical11/ACE2_cat.fa")
seq_human=read_seq_from_file("/Users/wangxiaolei/IBI1_2022-23/Practical11/ACE2_human.fa")
seq_mouse=read_seq_from_file('/Users/wangxiaolei/IBI1_2022-23/Practical11/ACE2_mouse.fa')
alignments1 = aligner.score(seq_cat, seq_human)
print(alignments1)
alignments2 = aligner.score(seq_mouse, seq_human)
print(alignments2)
if alignments1>alignments2:
   print("human's ACE2 gene sequence more like the cat")
if alignments1<alignments2:
   print("human's ACE2 gene sequence more like the mouse")
