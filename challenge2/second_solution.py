### By AstroAmat ###

print("Solutions implementing the method |.maketrans|\n")


#documentation https://stackoverflow.com/questions/28271515/what-is-difference-between-maketrans-and-replace-in-python
#documentation https://www.tutorialspoint.com/python/string_maketrans.htm

##### EXAMPLE ######
print ( "aeiu -> 4235\n")

from string import maketrans   # Required to call maketrans function.

intab = "aei"
outtab = "431"
trantab = maketrans(intab, outtab)

str = "Change By Dr.Nemo"
print str.translate(trantab)

#### END EXAMPLE ######
raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle grgl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
table = maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
result = raw.translate(table)
print(result)
