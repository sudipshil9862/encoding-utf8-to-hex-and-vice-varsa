#procedure:--
--------------
#converting utf8 to hex
1. user input string
2. taking each character of string and converting to ASCII value of that character
3. converting it to hexadecimal by hex(num).lstrip("0x").rstrip("L") where num is ASCII value of character  and here lstrip means I'm cutting the 0x from beginning and L from last if there
4. Assuming at max the hex code tange can be 8 (for emoji its 5) . So making a loop for including zero to fulfill 8 characters for each
6. putting every hex value into string string as output

#converting hex to utf8
1. Include the string to hextostr function
2. take 8 character(as I have taken at max 8 characters) of hex value together from the hex string
3. changing it to base 16 int and type cast to character
4. store characters into a output string one by one and display

(NOW, it will work for emoji)
