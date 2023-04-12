# ask the user for the stop codon
stop_codon = input("Enter a stop codon (TAA, TAG, or TGA): ")

# create the output filename
output_filename = f"{stop_codon}_stop_genes.fa"

# open the Saccharomyces_cerevisiae into a dictionary
with open("/Users/wangxiaolei/IBI1_2022-23/Practical9/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa") as f:
    lines = f.readlines()

# loop over the sequences and write the ones that end with the stop codon to the output file
with open(output_filename, 'w') as f:
 for i in range(len(lines)):
        if lines[i][0] == '>':
            name = lines[i].split()[0][1:]
            seq = ''
            num = 0
            for j in range(i+1, len(lines)):
                if lines[j][0] == '>':
                    break
                seq += lines[j].strip()
            if seq[-3:] == stop_codon:
                num += 1
        f.write(f'{num}" "{name}\n{seq}\n')