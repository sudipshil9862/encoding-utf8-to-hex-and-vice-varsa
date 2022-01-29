procedure:--
(language used: python)

#converting utf8 to hex
1. user input string
2. made a function to convert from space included string to hex code
3. taking each character of string and converting to ASCII value of that character
4. converting it to hexadecimal by hex(num).lstrip("0x").rstrip("L") where num is ASCII value of character
5. if the hex value is 20 that means it's space and we have to replace it by "%20" and send it to a string otherwise the hex value will be send to string 
6. putting every hex value into string string as output

#converting hex to utf8
1. Before performing the convertion we need to remove all the "%" we included for spcae (%20) by string replace method and then include the string to hextostr function
2. take two character of hex value together from the hex string
3. changing it to base 16 int and type cast to character
4. store characters into a output string one by one and display
