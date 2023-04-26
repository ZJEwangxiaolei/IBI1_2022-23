import blosum as bl
def read_seq_from_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        sequence = lines[1].replace("\n", "")
    return sequence

seq_cat=read_seq_from_file("/Users/wangxiaolei/IBI1_2022-23/Practical11/ACE2_cat.fa")
seq_human=read_seq_from_file("/Users/wangxiaolei/IBI1_2022-23/Practical11/ACE2_human.fa")
seq_mouse=read_seq_from_file('/Users/wangxiaolei/IBI1_2022-23/Practical11/ACE2_mouse.fa')
len1 = len(seq_cat)
len2 = len(seq_human)
len3 = len(seq_mouse)
edit_distance1 = 0
for i in range(len1):
    if seq_cat[i]==seq_human[i]:
     edit_distance1 += 1
print (edit_distance1)
edit_distance2 = 0
for i in range(len3):
    if seq_mouse[i] ==seq_human[i]:
     edit_distance2 += 1
print (edit_distance2)
if edit_distance1>edit_distance2:
   print("human's ACE2 gene sequence more like the cat")
if edit_distance1<edit_distance2:
   print("human's ACE2 gene sequence more like the mouse")


