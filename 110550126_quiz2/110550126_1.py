
def vowel_rate(words,dim):
    diff = 0
    for i in range(0,dim[0]):
        vow = 0
        for j in range(0,dim[1]):
            print(words[j*dim[0]+i],end="")
            if words[j*dim[0]+i] in 'AEIOU':
                vow+=1
        print("",abs(vow-dim[1]*0.4))
        diff += abs(vow-dim[1]*0.4)
        #print(vow-dim[1]*0.4)
    return diff
if __name__ == "__main__":
    words = "ECDTM ECAER AUOOL EDSAM MERNE NASSO DYTNRVBNLC RLTIQ LAETR IGAWE BAAEI HOR".replace(" ","")
    dim1 = (7,9)
    dim2 = (9,7)
    print("dim:",dim1,"error:",vowel_rate(words,dim1))
    print()
    print("1253467")
    print("dim:",dim2,"error:",vowel_rate(words,dim2))
    