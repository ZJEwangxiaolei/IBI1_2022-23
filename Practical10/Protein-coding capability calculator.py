def protein_coding(seq):
 start_condon = "ATG"
 stop_condon = "TGA"
 start = seq.find(start_condon) 
 stop = seq.find(stop_condon)
 if start == -1 or stop == -1:
  return "unclear",0,"%"
 coding = seq[start:stop+3]
 total_len = len(seq)
 coding_len = len(coding)
 persentage = coding_len/total_len
 persentage_str = str(persentage*100) + "%"
 if persentage > 0.5:
  return 'protein coding',persentage_str
 elif persentage < 0.1:
  return 'non-coding',persentage_str
 else:
  return 'unclear',persentage_str
# Example usage
seq="AAATGAAAAAAATGA"
print(protein_coding(seq))