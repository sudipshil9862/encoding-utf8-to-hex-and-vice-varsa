
def convertToHex(s):
    utf8 = []
    for i in s:
        #utf8.append((str(i.encode('utf-8').hex()).lstrip("b")).replace("'","").replace("\\x",""))
        utf8.append((str(i.encode('utf-8').hex())))
    return utf8

def convertToString(hexStr):
    l = []
    for i in hexStr:
        x = int(i,16)
        if(x < 256):
            res = (x).to_bytes(1, byteorder='big')
            l.append(res.decode())
        elif(x < pow(2,16)):
            res = (x).to_bytes(2, byteorder='big')
            l.append(res.decode())
        else:
            res = (x).to_bytes(4, byteorder='big')
            l.append(res.decode())
    return l

s= input("enter the string : ")
a = convertToHex(s)
print("utf8 hex code:-")
for i in a:
    print(i,end=" ")


b = convertToString(a)
print("\noriginal string:- ")
for i in b:
    print(i,end="")
