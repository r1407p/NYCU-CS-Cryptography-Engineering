import math
def decode(words,dim):
    ans = [""]*dim[0]
    rest = dim[1]-(dim[0]*dim[1]-50)
    if rest <0 or rest==0:
        print(dim, "is not avaliable")
        return
    for i in range(0,rest*dim[0]):
        ans[i%dim[0]]+=words[i]
    at = 0
    for i in range(rest*dim[0],50):
        ans[at%(dim[0]-1)]+=words[i]
        at+=1
    for i in ans:
        print(i)
        
if __name__ == "__main__":
    words = "LLOWA POLNH NHOEG YSOKD NDWNI TUIEE FHMDR IEBYT CWEOH ARRUE".replace(" ","")
    for i in range(6,15):
        temp = math.ceil(50/i)
        print("=================="+str(i)+"*"+str(temp)+"===================")
        decode(words,(i,temp))
        print("=====================================================")
        
    