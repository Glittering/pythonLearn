#coding:gbk

import re

#python ����re��:���ַ�����һ�ָ߼�����ʽ��ͨ����������ƥ��
    #����ƥ��:ͨ��������Ҫƥ�����ݵ���������ƥ��
        #ƥ��Ĺ���
            #ƥ�����ݵĹ���
                #ԭ��ƥ��
s = 'My name is xiao_zhen,\nI am 20 years old,\tmy job is ITmonkey!!!'
#print re.findall('is',s)

                # . ���˻��з�֮�����������
#print re.findall('..',s)

                #\w ƥ�����е�������ĸ�»���
#print re.findall(r'\w',s)
#print re.findall(r'\w.',s)

                #\W ƥ�����з�������ĸ�»��ߵ�����
#print re.findall(r'\W',s)
#print re.findall('\w\W',s)
                
                #\d ƥ�����е�����
#print re.findall(r'\d',s)
                #\D ƥ�����еķ���������
#print re.findall(r'\D',s)
s = 'My name is xiao_zhen,\nI am 20 years old,\tmy job is ITmonkey!!!'

#print re.findall(r'\w\d',s)
                
                #\s ƥ�����еĿհ׷�������\n��\t��
#print re.findall(r'\s',s)
                #\S ƥ�����еķǿհ׷�����
#print re.findall(r'\S',s)

                #\b ���ʱ߽磬ֻƥ��һ��λ��
#print re.findall(r'\b\w',s)
                #\B
#print re.findall(r'\w\B',s)              

                #\A ���ַ����Ŀ�ʼλ�ý���ƥ��
#print re.findall(r'\A\w\w',s)
#print re.findall(r'\A\d',s)
                #\Z ���ַ����Ŀ�ʼĩβ����ƥ��
#print re.findall(r'.\W\Z',s)

                #^ �ڿ�ͷƥ��
#print re.findall(r'^\w\w',s)

                #$ ��ĩβƥ��
#print re.findall(r'.\W$',s)
#print re.findall(r'^python$','python')

                #[] ƥ����������������һ��
#print re.findall(r'[\W\d]',' , , ')
#print re.findall(r'[\W\d]',s)

                #[...-...] ƥ��һ����Χ
                    #[a-z]  [A-Z] 
#print re.findall(r'[A-Z]',s)
#print re.findall(r'[0-9]',s)
#print re.findall(r'[h-w]',s)
#print re.findall(r'1[358]',s)
#print re.findall(r'[A-Za-z]',s)

                #[^...] ��
#print re.findall(r'[^\w]',s)
#print re.findall(r'\W',s)
#print re.findall(r'[^\D]',s)


                #() ��ƥ�䣬����ƥ����ֵ�ʱ��������ƥ����Ϊ��ƥ�����������ƥ�䣬���շ�����ƥ��ƥ�䵽������
s = 'My name is xiao_zhen,\nI am 20 years old,\tmy job is ITmonkey!!!'

#print re.findall(r'(\w)\d',s)
#print re.findall(r'\w\d',s)

                #(?P<name>...) ������
#print re.findall(r'(?P<xiaoli>\w)\d',s)

                #(?P=name) ����������ƥ�䵽�Ľ��
a = 'b2b c3e d4f g5g h6h o7i'
#print re.findall(r'(?P<xiaoli>\w)\d',a)
#print re.findall(r'(?P<xiaoli>\w)\d(?P=xiaoli)',a)
'''
b 2 b
c 3 c
d 4 d
g 5 g
h 6 h
o 7 o
'''
                #(.*) ̰��ƥ��
#print re.findall(r'a(.*)b','abbbbbbbb')

                #(.*?) ��̰��ƥ��
#print re.findall(r'a(.*?)b','abbbbbbbb')

html = '''
<html>
    <body>
        <p>hello <br/> world</p>
        <p style = 'color:red;'>123</p>
    </body>
</html>
'''
#print re.findall(r'<p>(.*?)</p>',html)
#print re.findall(r'<p .*>(.*?)</p>',html)

                #(?=...) ǰհ����ƥ��
s = 'My name is xiao_zhen,\nI am 20 years old,\tmy job is ITmonkey!!!'

#print re.findall(r'\w(?=\d)',s)
#print re.findall(r'(\w)\d',s)
                #(?!...) ��ǰհ����ƥ��
#print re.findall(r'\w(?!\d)',s)
#print re.findall(r'(\w)\D',s)

                #(?<=...) ��˶���ƥ��
#print re.findall(r'(?<=\d)\w',s)

                #(?<!...) ����˶���ƥ��

#print re.findall(r'(?<!\w)\d',s)

                #| ƥ��ܵ�����������һ��
#print re.findall(r'\W|\d',s)
#print re.findall(r'13|15|18')

            #ƥ�������Ĺ���
                #* ƥ��0�����
#print re.findall(r'\w*',s)
                #+ ƥ��1�����
#print re.findall(r'\w+',s)
                #? ƥ��0��1��
#print re.findall(r'\w?',s)
                #{4} ƥ��ָ���Ĵ���
#print re.findall(r'\w{4}',s)
                #{2,4 }
#print re.findall(r'\w{2,4}',s)

            #�������
z = 'AaBbAaCc'
                #re.I ���Դ�Сд
#print re.findall(r'a',z,re.I)

                #re.S �޸�.��ƥ�䷽ʽ
#print re.findall(r'.',s)
#print re.findall(r'.',s,re.S)

                #re.M ����ģʽ
s = '''My name is xiao_zhen,
I am 20 years old,
my job is ITmonkey!!!'''

#print re.findall(r'\A\w',s,re.M)
#print re.findall(r'^\w',s,re.M)

#print re.findall(r'.\Z',s,re.M)
#print re.findall(r'.$',s,re.M)

        #ƥ��ķ���
            #findall ��ָ���ַ������в������з���������ʽ���������ݣ��������б���ʽ
#print re.findall(r'zzz',s)
s = '''My name is xiao_zhen,
I am 20 years old,
my job is ITmonkey!!!'''

            #search ��ָ���ַ������в��ҷ���������ʽ���������ݣ�
                    #����ҵ�������ƥ����󣨵�һ��ƥ�䵽�����ݣ�
                    #���û�У�����None
#print re.search(r'\d',s)
#print re.search(r'zzz',s)

#ƥ�����
    #group

    #gropus
m = re.search(r'\d',s)
#print m.group()
#print dir(m)
#print re.search(r'\w+',s).group()
#print re.search(r'\w+',s).groups()

            #match ���ַ����Ŀ�ͷ���ҷ���������ʽ���������ݣ�
                    #����ҵ�������ƥ����󣨵�һ��ƥ�䵽�����ݣ�
                    #���û�У�����None
#print re.match(r'\w+',s).group()
#print re.match(r'\d+',s)
#print re.match(r'zzz',s)
#print re.match(r'\w+',s,re.M).group()

#print re.match(r'(\w)(.)',s).groups()
#print re.search(r'(\w+)(.)(\w+)',s).groups()
#print re.search(r'(\w+)(.)(\w+)',s).group()

            #compile �γ�һ������ģ��
p = re.compile(r'\w+')
#print dir(p)
#print p.findall(s)
#print re.findall(r'\w+',s)
#print re.findall(p,s)

            #sub �������ַ�����replace����
#print re.sub(r'\w','*',s)
#print s
#print re.sub(r'\w+','hello',s,3)

            #split �������ַ�����split����
#print re.split(r'\d',s)
#print re.split(r'\W',s,5)

    #�ṹƥ��
        #lxml  BeautifulSoup
#print re.findall(r'\.','I am xiaoli.')


#ƥ��IP��ַ
#ƥ�����֤��
#ƥ���ֻ���


