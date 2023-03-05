import math
find_text = """T ZJDMBYFS VZRFGYRVY DBVY JIYFG
FKMFSRFGZF T IFFARGL JI GJY
ITS SFDJEFC ISJD TATSD JG
TGTANQRGL TGC FKMAJSF
YOF IAJJC JI TCETGZFC XGJHAFCLF HORZO
FTZO NFTS WSRGLV HRYO RY
"""
freq = [0]*26
total = 0
for i in find_text:
    if i!=" "and i!='\n':
        total +=1
        freq[ord(i)-ord('A')]+=1

for i in range(0,26):
    print(chr(ord('A')+i)+':',end = " ")
    print(freq[i])
    print(math.floor(freq[i]/total*10000)/100)
