from json.tool import main


def ASCIItoHEX(ascii):
    hexa = ""
    for i  in range(len(ascii)):
        ch = ascii[i]
        int1 = ord((ch))
        inthex = hex(int1).lstrip("0x").rstrip("L")
        #if there is any space(whose ASCII = 20) than it will covert it into "%20" (as mentioned in question)
        if str(inthex) == "20":
            hexa += "%20"
        else:
            hexa += inthex
    return hexa

def hexToASCII(hexx):
    asci = ""
    for i in range(0, len(hexx), 2):
        part = hexx[i : i + 2]
        ch = chr(int(part, 16))
        asci += ch
    print(asci)




s = input("enter string to convert into hex:-")

#string to hex (via ASCII)
a = ASCIItoHEX(s)
print(a)

#hex to string

#removing all "%" as we have included for space instead of 20
for i in a:
    if(i == "%"):
        i = ""
print(hexToASCII(a))

