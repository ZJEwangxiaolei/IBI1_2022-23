# open the file called Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa
with open("/Users/wangxiaolei/IBI1_2022-23/Practical9/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa") as f:
    lines = f.readlines()
    
# find "<" in the text and store the information between two "<" into seq and stop when the last 3 letters are "TGA"
with open('TGA_genes.fa', 'w') as f:
    for i in range(len(lines)):
        if lines[i][0] == '>':
            name = lines[i].split()[0][1:]
            seq = ''
            for j in range(i+1, len(lines)):
                if lines[j][0] == '>':
                    break
                seq += lines[j].strip()
            if seq[-3:] == 'TGA':
                f.write(f'{name}\n{seq}\n')