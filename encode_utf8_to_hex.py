
def strToHex(strValue):
    hexa = ""
    for i  in range(len(strValue)):
        ch = strValue[i]
        int1 = ord((ch))
        inthex = hex(int1).lstrip("0x").rstrip("L")
        #if there is any space(whose ASCII = 20) than it will covert it into "%20" (as mentioned in question)
        # if str(inthex) == "20":
        #     hexa += "%20"
        # else:
        #     hexa += inthex
        for i in range(0,8-len(inthex)): # assumeing max 8 caharacter
            inthex = "0" + inthex
        hexa += inthex    
    return hexa

def hexToStr(hexStr):
    asci = ""
    for i in range(0, len(hexStr), 8):
        part = hexStr[i : i + 8]
        ch = chr(int(part, 16))
        asci += ch
    return asci


s = input("enter string to convert into hex:-")
#string to hex (via ASCII)
a = strToHex(s)
print("string to hex value:- ",a)

#hex to string
#removing all "%" as we have included for space instead of 20
# b = a.replace("%20","20")
# print("hex value to string:- ",hexToStr(b))
print("hex value to string:- ",hexToStr(a))
