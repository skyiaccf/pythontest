## 这是一个注释
"""
这也是注释
这也是注释
"""


txt = open('test.txt','w')
txt.write('123456789')
txt.close()

txt = open('test.txt','r+')
txt.write('00000')
tttt = txt.readlines(txt,1)
print(tttt)
txt.close()



