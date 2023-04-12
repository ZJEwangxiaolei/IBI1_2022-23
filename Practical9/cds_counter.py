# read the sequence
seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'

# input the start and stop codons
start_codon = 'ATG'
stop_codons = ['TAA', 'TAG', 'TGA']

# count the stop codon in the sequence
count = 0
for i in range(len(seq)):
    if seq[i:i+3] == start_codon:
        for j in range(i+3,len(seq),1):
            if seq[j:j+3] in stop_codons:
                count += 1
print(count)