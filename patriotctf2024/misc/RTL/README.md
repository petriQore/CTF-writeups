```Python 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import re
>>> flag=open("./flag.vcd").read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: './flag.vcd'
>>>
KeyboardInterrupt
>>> flag=open("./flag.vcd").read()
>>> extract=re.findall("b.*",flag)
>>> print(extract)
['b01010000 "', 'b01010000 #', 'b01000011 "', 'b01000011 #', 'b01010100 "', 'b01010100 #', 'b01000110 "', 'b01000110 #', 'b01111011 "', 'b01111011 #', 'b01010010 "', 'b01010010 #', 'b01010100 "', 'b01010100 #', 'b01001100 "', 'b01001100 #', 'b01011111 "', 'b01011111 #', 'b01101001 "', 'b01101001 #', 'b00100100 "', 'b00100100 #', 'b01011111 "', 'b01011111 #', 'b01000100 "', 'b01000100 #', 'b01000000 "', 'b01000000 #', 'b01000100 "', 'b01000100 #', 'b01011111 "', 'b01011111 #', 'b00110000 "', 'b00110000 #', 'b01000110 "', 'b01000110 #', 'b01011111 "', 'b01011111 #', 'b01001000 "', 'b01001000 #', 'b01000000 "', 'b01000000 #', 'b01110010 "', 'b01110010 #', 'b01100100 "', 'b01100100 #', 'b01110111 "', 'b01110111 #', 'b01000000 "', 'b01000000 #', 'b01110010 "', 'b01110010 #', 'b00110011 "', 'b00110011 #', 'b01111101 "', 'b01111101 #']
>>> extract = [ _ for _ in extract[::2]]
>>> extract = "".join([ _.replace("b","").replace("\"","").strip() for _ in extract])
>>> print(extract)
01010000010000110101010001000110011110110101001001010100010011000101111101101001001001000101111101000100010000000100010001011111001100000100011001011111010010000100000001110010011001000111011101000000011100100011001101111101
>>> copy paste in cyberchef gg
  File "<stdin>", line 1
    copy paste in cyberchef gg
         ^^^^^
SyntaxError: invalid syntax
>>>
```
