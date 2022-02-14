#f = open("E:\Files/cv.csv", "r")
# x = f.readlines()
# for i in x[1:]:
#     a = i.split(",")
#     x = int(a[0])
#     y = int(a[1])
#     print(x, y)
# f.close()
a = """<HTML>
<HEAD>
</HEAD>
<BODY>
<TABLE>
<TR><TD>x</TD><TD>y</TD></TR>
"""
t = open("cv.csv", "r")
f = open("harry.html", "w")
f.write(a)
a = t.readlines()
for i in a[1:]:
    b = i.split(",")
    x = int(b[0])
    y = int(b[1])
    print(x, y)
    f.write("<TR><TD>{}</TD><TD>{}</TD></TR>\n".format(x, y))
    print()
f.write("\n</BODY>\n</TABLE>\n</HTML>")
f.close()
t.close()