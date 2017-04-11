#coding:gbk

#匹配11位手机号
#匹配邮箱
#匹配IP
#匹配身份证号18 X  15

#怎么打开一个外部文件进行搜索？





import re
#a1='frhyjuioiiwq67tyoyuj'
class search():
        
    def phone_number(self):
        b1=re.findall(r'1[358]\d{8}',a1)
        b2=re.findall(r'1[7]7\d{7}',a1)
        print b1+b2
    def email(self):
        b3=re.findall(r'\w{1,18}@\w{1,8}\.com',a1)
        b4=re.findall(r'\w{1,18}@163\.com',a1)
        b5=re.findall(r'\d{1,18}@qq\.com',a1)
        b6=re.findall(r'\w{1,18}@sina\.com',a1)
        b7=re.findall(r'\w{1,18}@126\.com',a1)
        b8=re.findall(r'\w{1,18}@yahoo\.com',a1)
        b9=re.findall(r'\w{1,18}@sohu\.com',a1)
        print '全部疑似邮箱：',b3,'\n163邮箱：',b4,'\nQQ邮箱：',b5,'\n新浪邮箱：',b6,'\n网易邮箱：',b7,'\n雅虎邮箱：',b8,'\n搜狐邮箱：',b9,
    def ip(self):
        for i1 in range(256):
            for i2 in range(256):
                for i3 in range(256):
                    for i4 in range(256):
                        print re.findall(r'i1\.i2\.i3\.i4',a1)+'\n'
            
    def serial_number(self):
        c1 = re.findall(r'[1234]\d{5}19\d{2}0[13456789][012]\d{4}[0123456789x]',a1)
        c14 = re.findall(r'[1234]\d{5}19\d{2}0[13456789]30\d{3}[0123456789x]',a1)
        c2 = re.findall(r'[1234]\d{5}19\d{2}1[02][12]\d{4}[0123456789x]',a1)
        c3 = re.findall(r'[1234]\d{5}19\d{2}1[02]3[01]\d{3}[0123456789x]',a1)
        c4 = re.findall(r'[1234]\d{5}19\d{2}02[012]\d{4}[0123456789x]',a1)
        
        c5 = re.findall(r'[1234]\d{5}200\d0[13456789][012]\d{4}[0123456789x]',a1)
        c15 = re.findall(r'[1234]\d{5}200\d0[13456789]30\d{3}[0123456789x]',a1)
        c6 = re.findall(r'[1234]\d{5}200\d1[02][12]\d{4}[0123456789x]',a1)
        c7 = re.findall(r'[1234]\d{5}200\d1[02]3[01]\d{3}[0123456789x]',a1)
        c8 = re.findall(r'[1234]\d{5}200\d02[012]\d{4}[0123456789x]',a1)
    
        c9 = re.findall(r'[1234]\d{5}201[0-6]0[13456789][012]\d{4}[0123456789x]',a1)
        c16 = re.findall(r'[1234]\d{5}200\d0[13456789]30\d{3}[0123456789x]',a1)
        c10 = re.findall(r'[1234]\d{5}201[0-6]1[02][12]\d{4}[0123456789x]',a1)
        c11 = re.findall(r'[1234]\d{5}201[0-6]1[02]3[01]\d{3}[0123456789x]',a1)
        c12 = re.findall(r'[1234]\d{5}201[0-6]02[012]\d{4}[0123456789x]',a1)

        c13 = re.findall(r'[1234]\d{5}201701[012]\d{4}[0123456789x]',a1)
        c17 = re.findall(r'[1234]\d{5}20170130\d{3}[0123456789x]',a1)
        c18 = re.findall(r'[1234]\d{5}201702[012]\d{4}[0123456789x]',a1)
        c19 = re.findall(r'[1234]\d{5}2017030[123]\d{3}[0123456789x]',a1)

        d1 = re.findall(r'[1234]\d{7}0[13456789][012]\d{4}',a1)
        d2 = re.findall(r'[1234]\d{7}0[13456789]30\d{3}[',a1)
        d3 = re.findall(r'[1234]\d{7}1[02][12]\d{4}',a1)
        d4 = re.findall(r'[1234]\d{7}1[02]3[01]\d{3}[',a1)
        d5 = re.findall(r'[1234]\d{7}02[012]\d{4}',a1)
        print '18位身份证号：'
        print c1
        print c2
        print c3
        print c4
        print c5
        print c6
        print c7
        print c8
        print c9
        print c10
        print c11
        print c12
        print c13
        print c14
        print c15
        print c16
        print c17
        print c18
        print c19
        print '15位身份证号：'
        print d1
        print d2
        print d3
        print d4
        print d5
       
if __name__=='__main__':
    
    a=raw_input('请输入要搜索的文件路径')
    A=int(raw_input('请输入要查询的类型：1、（手机号）2、（邮箱）3、（IP地址）4、（身份证号）'))
    
    aa=open(a,'r')
    a1=aa.read()
    ed = search()
    if A == 1:
        ed.phone_number()
    elif A == 2:
        ed.email()
    elif A == 3:
        ed.ip()
    elif A == 4:
        ed.serial_number()
    else:
        print A
        
   

#C:\Users\异乡异客\Desktop\阅读.txt



















        
