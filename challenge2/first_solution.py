print "The hints are:","k -> m","o -> q","e -> g"
print"so... these are K,L,M  O,P,Q   E,F,G \n"
print   "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.\n"
"""
### test area ######
print("FIRST  TEST_____")
print("ord(z)="), (ord("z"))#122
print"ord(a)= ",ord("a")#97
#RESTA DE VALORES
print "chr((ord(quotation marks(z) ) +2) - ord(quotation marks(a) ))  #27"
print("SECOND  TEST_____")
#print chr(((ord('z') + 2) - ord('a')) % 26)
print (27 % 26)#1
print("THIRD  TEST_____ z -> b")
print chr(((ord('z') + 2) - ord('a')) % 26 + ord('a'))

##### End Test Area #####
"""
print("SO... the result is: ")
raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
result =('')
for text in raw:
 if text >= 'a' and text <= 'z':
     result +=chr(((ord(text) + 2) - ord('a')) % 26 + ord('a'))
 else:
         result += text
print(result)
print("\n")
print("other Solutions is use |.join| \n")
print(''.join([chr(((ord(c) + 2) - ord('a')) % 26 + ord('a')) if c >= 'a' and c <= 'z' else c for c in raw]))
