def strxor(a, b):     
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
def padding(plaintext,cypher):
    num = str(int(len(cypher)/2 - len(plaintext)))
    padding = "".join([num] * int(num))
    
    return plaintext+padding
if __name__ =="__main__":
    cypherText ="20814804c1767293b99f1d9cab3bc3e7ac1e37bfb15599e5f40eef805488281d"
    cypherTextIV = cypherText[:int(len(cypherText)/2)]
    cypherTextC0 = cypherText[int(len(cypherText)/2):]
    plainText = "Pay Bob 100$"		
    plainTextTarget = "Pay Bob 500$"
    plainText = padding(plainText,cypherTextIV)
    plainTextTarget = padding(plainTextTarget,cypherTextC0)
    xorredPlainText = int.from_bytes(plainText.encode(),'big') ^ int.from_bytes(plainTextTarget.encode(),'big')
    newIV = xorredPlainText ^  int(cypherTextIV, 16)
    answer = hex(newIV)[2:] + cypherText[int(len(cypherText)/2):]
    print(answer)