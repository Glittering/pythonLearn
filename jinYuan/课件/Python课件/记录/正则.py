#coding:gbk
import re

#python ������ʽ
    #re:һ���ַ����ĸ߼�����ʽ��ͨ������ƥ��
        #����ƥ��:ͨ��������Ҫƥ�����ݵ��ص����ƥ��
            #ƥ��Ĺ���
                #ƥ�����ݵĹ���
s = "My name is xiao_wang,\n I'm 24 years old,\t my job is ITmonkey."
                    #ԭ��ƥ��
#print re.findall(r'm',s)

                    # . ƥ����˻��з�֮�����������
#print re.findall(r'.',s)
#print re.findall(r'..',s)
#print re.findall(r'\.',s)
                    
                    #\s ƥ�����еĿհ׷�������\n,\t��
#print re.findall(r'\s',s)

                    #\S ƥ�����еķǿհ׷�����
#print re.findall(r'\S',s)
                    
#print re.findall(r'\s.',s)

                    #\d ƥ�����е�����
#print re.findall(r'\d',s)
 
                    #\D ƥ�����з����ֵ�����
#print re.findall(r'\D',s)

#print re.findall(r'\d.',s)

                    #\w ƥ�����е�������ĸ�»���
#print re.findall(r'\w',s)
                    #\W ƥ�����еķ�������ĸ�»�������
#print re.findall(r'\W',s)

#print re.findall(r'\d\w',s)
                    
                    #\b ���ʱ߽磬ֻƥ��һ��λ��
#print re.findall(r'\w\b',s)
#print re.findall(r'\b\w',s)
                    #\B ������ĸ֮�䣬ֻƥ��һ��λ��
#print re.findall(r'\w\B',s)
#print re.findall(r'\B\w',s)
s = "My name is xiao_wang,\n I'm 24 years old,\t my job is ITmonkey."           
                    #\A ���ַ�����ͷ����ƥ��
#print re.findall(r'\A\w',s)
#print re.findall(r'\A\d',s)
#print re.findall(r'\A.',s)

                    #\Z ���ַ���ĩβ����ƥ��
#print re.findall(r'\W\Z',s)

                    # ^ ��ÿ�п�ͷ
'''
print re.findall(r'^\w',s)
print re.findall(r'^\d',s)
print re.findall(r'^.',s)
'''
                    # $ ��ÿ��ĩβ
#print re.findall(r'\W$',s)

                    #[] ƥ�������ŵ�������һ��
#print re.findall(r'[aom]',s)
#print re.findall(r'[123]','15791579')
#print re.findall(r'[\s\d]',s)
#print re.findall(r'1[3578]','15378732778128913754785787887183234324324233')
'''
15 
18
13
17
'''
                    # | ƥ��ܵ�����������һ��
#print re.findall(r'13|15|18','178732778128917547857878871832')

                    #[^...] ��
'''
print re.findall(r'[^\d]',s)
print re.findall(r'\D',s)
'''
#print re.findall(r'[^\w]',s)

                    #[a-z] ƥ��һ����Χ
#print re.findall(r'[a-z]',s)
#print re.findall(r'[A-Z]',s)
#print re.findall(r'[f-k]',s)
#print re.findall(r'[0-9]',s)
#print re.findall(r'[a-zA-Z]',s)
#print re.findall(r'[A-Z0-9]',s)

                    #() ��ƥ�䣬����ƥ����ֵ�ʱ��������ƥ�䷽ʽ��Ϊ��ƥ�����������ƥ��
#print re.findall(r'\w\d',s)
#print re.findall(r'(\w)\d',s)
#print re.findall(r'\w\w',s)
#print re.findall(r'\w(\w)',s)

                    #(?P<name>...) ������
#print re.findall(r'(?P<laoli>\s)',s)
a = 'b3b c2d e5e f7h g8g l2u'
#print re.findall(r'(?P<xiaoli>\w)',a)
                    #(?P=name)  ����������ƥ�䵽�Ľ��
#print re.findall(r'(?P<xiaoli>\w)\d',a)
#print re.findall(r'(\w)\d',a)
#print re.findall(r'(?P<xiaoli>\w)\d(?P=xiaoli)',a)
'''
b 3 b
c 2 c
e 5 e
f 7 f
g 8 g
l 2 l
'''
                    #(.*) ̰��ƥ��
#print re.findall(r'a(.*)b','acc12345ccc\naaaacccb')
#print re.findall(r'a(.*)b','abbbbbbbbb')

                    #(.*?) ��̰��ƥ��
#print re.findall(r'a(.*?)b','abbbbbbbbb')

a = 'b3b c2d e5e f7h g8g l2u'
                    #(?=...) ǰհ����ƥ��
#print re.findall(r'\w(?=\d)',a)
#print re.findall(r'\w(?=\d)\w',a)
                    #(?!...) ��ǰհ����ƥ��
#print re.findall(r'\w(?!\d)',a)

                    #(?<=...) ��˶���ƥ��
#print re.findall(r'(?<=\d)\w',a)
                    #(?<!...) ����˶���ƥ��
#print re.findall(r'(?<!\d)\w',a)
#print re.findall(r'\D',a)

                #ƥ�������Ĺ���
s = "My name is xiao_wang,\n I'm 24 years old,\t my job is ITmonkey."  
                    #* ƥ��0�����
#print re.findall(r'\w*',s)

                    #+ ƥ��1�����
#print re.findall(r'\w+',s)

                    #? ƥ��0��1��
#print re.findall(r'\w?',s)

                    #{3} ƥ��ָ������
#print re.findall(r'\w{3}',s)

                    #{1,4} ƥ��1��4��
#print re.findall(r'\w{1,4}',s)

                #�������
                    #re.I ���Դ�Сд
s = 'aAbBcCdDeAfAg'
#print re.findall(r'a',s,re.I)

                    #re.S �޸�.��ƥ�䷽ʽ
s = "My name is xiao_wang,\n I'm 24 years old,\t my job is ITmonkey."
#print re.findall(r'.',s,re.S)

                    #re.M ����ģʽ
s = '''My name is xiao_wang,\n
I'm 24 years old,\t
my job is ITmonkey.'''

#print re.findall(r'\A\w',s,re.M)
#print re.findall(r'^\w',s,re.M)
#print re.findall(r'.\Z',s,re.M)
#print re.findall(r'.$',s,re.M)


            #ƥ��ķ���
                #findall ��ָ���ַ������в�����������������ʽ���������ݣ������б���ʽ
#print re.findall('m',s)

s = "My name is xiao_wang,\n I'm 24 years old,\t my job is ITmonkey."
                #search ��ָ�����ַ������в��ҷ���������ʽ���������ݣ�������ڣ�����ƥ����󣨵�һ��ƥ�䵽�Ľ����
                        #��������ڣ�����None
m = re.search(r'\w+',s)
#print re.search(r'aaa',s)
#print dir(m)
#print m.group()
#print re.search(r'\d',s).group()

#ƥ�����
    #group
    #groups
                #match ��ָ���ַ����Ŀ�ͷ���ҷ���������ʽ���������ݣ�������ڣ�����ƥ����󣨵�һ��ƥ�䵽�Ľ����
                        #��������ڣ�����None
#print re.match(r'\w+',s).group()
#print re.match(r'\d+',s)
#print re.match(r'aaa',s)
#print re.match(r'\s',s)

#print re.match(r'(\w+)(.)(\w+)(.)',s).groups()
#print re.match(r'(\w+)',s).groups()
#print re.search(r'(\d)(\d)',s).groups()

                #sub��ƥ�䵽�������滻Ϊָ�����ַ�
'''
print re.sub(r'\w','*',s)
print s
#print re.findall(r'\w+',s)
'''
#print re.sub(r'\w+','$',s,5)

                #split ����ƥ��������з��ַ���
'''
print len(re.split(r'\s',s))
print len(re.findall(r'\s',s))
'''
#print re.split(r'\s',s,4)
                #compile �γ�һ������ģ��
c = re.compile(r'\w')
#print c.findall(s)
#print c.findall(s,10,20)
#print re.findall(r'\w',s)
#print re.findall(c,s)


#�ṹƥ��
    #lxml  BeautifulSoup



#ƥ��11λ�ֻ���
#ƥ������
#ƥ��IP
s = '12.12.12.12'
#print re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])',s).group()

#ƥ�����֤��18 X  15
#re.findall(r'\d{18}|\d{17}X|\d{15}')



html = '''
<html>
    <head>
        <title>
            hello
        </title>
    </head>
    <body>
        <p>
            "��������ö����ֱ��ɵļ���Ҳ���õĳ�����ֱ�������������ҵ���"<br/>"��ֽ�������������ι����������"<br/>"���������������Ь���������"
        </p>
    </body>
</html>
'''
#print re.findall(r'<p>(.*?)</p>',html,re.S)


for i in re.findall(r'<p>(.*)</p>',html,re.S):
    pass
    #print i
    #print i.replace('<br/>','\n')

