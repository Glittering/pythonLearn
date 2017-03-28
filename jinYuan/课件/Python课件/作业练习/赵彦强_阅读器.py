# coding:gbk

import time

# 电子书
def readBook(x):

    f = open(x, 'r')
    f.read()
    #获取总字节
    ziJie_ZongShu = f.tell()

    #获取分页阅读字节
    r_zijie = 0

    #指针归零
    f.seek(0,0)

    lists = ['手动','自动','下一页','退出']
    a = raw_input("请输入想要的阅读方式（手动，自动）：")

    if a not in lists:
        a = raw_input("请输入正确的指令（手动，自动）：")

    print '开始阅读'

    rounds = 0

    while True:

        rounds += 1

        if a == '手动':



            if r_zijie < ziJie_ZongShu:
                nextS = raw_input("请输入指令（下一页，退出）：")
                if nextS not in lists:
                    nextS = raw_input("请输入正确的指令（下一页，退出）：")

                if nextS == '下一页':

                    print '第 %d 页' % rounds
                    print f.read(500)
                    r_zijie = f.tell()
                    print '已阅读:%.1f%%\n' % (float(r_zijie) / float(ziJie_ZongShu) * 100)

                else:
                    f.close()
                    break

            else:

                print '阅读完毕'
                f.close()
                break


        elif a == '自动':


            if r_zijie != ziJie_ZongShu:


                time.sleep(2)

                print '第 %d 页' % rounds
                print f.read(300)
                r_zijie = f.tell()
                print '已阅读:%.1f%%\n' % (float(r_zijie) / float(ziJie_ZongShu) * 100)



            else:

                print '阅读完毕'
                f.close()
                break

if __name__ == '__main__':

    readBook('123.txt')
