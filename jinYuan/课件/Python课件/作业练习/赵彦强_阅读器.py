# coding:gbk

import time

# ������
def readBook(x):

    f = open(x, 'r')
    f.read()
    #��ȡ���ֽ�
    ziJie_ZongShu = f.tell()

    #��ȡ��ҳ�Ķ��ֽ�
    r_zijie = 0

    #ָ�����
    f.seek(0,0)

    lists = ['�ֶ�','�Զ�','��һҳ','�˳�']
    a = raw_input("��������Ҫ���Ķ���ʽ���ֶ����Զ�����")

    if a not in lists:
        a = raw_input("��������ȷ��ָ��ֶ����Զ�����")

    print '��ʼ�Ķ�'

    rounds = 0

    while True:

        rounds += 1

        if a == '�ֶ�':



            if r_zijie < ziJie_ZongShu:
                nextS = raw_input("������ָ���һҳ���˳�����")
                if nextS not in lists:
                    nextS = raw_input("��������ȷ��ָ���һҳ���˳�����")

                if nextS == '��һҳ':

                    print '�� %d ҳ' % rounds
                    print f.read(500)
                    r_zijie = f.tell()
                    print '���Ķ�:%.1f%%\n' % (float(r_zijie) / float(ziJie_ZongShu) * 100)

                else:
                    f.close()
                    break

            else:

                print '�Ķ����'
                f.close()
                break


        elif a == '�Զ�':


            if r_zijie != ziJie_ZongShu:


                time.sleep(2)

                print '�� %d ҳ' % rounds
                print f.read(300)
                r_zijie = f.tell()
                print '���Ķ�:%.1f%%\n' % (float(r_zijie) / float(ziJie_ZongShu) * 100)



            else:

                print '�Ķ����'
                f.close()
                break

if __name__ == '__main__':

    readBook('123.txt')
