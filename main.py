import sys

from virtual_machine.interpreter import brainfucker

query = [
    '-F',
    '-f',
    '-C',
    '-c',
    '-i',
    '-I',
    '-D',
    '-d'
]

desc = '''这是个特别酷炫(误)的图灵机模拟器，支持长度高达65536的寄存器！是的！不是128，不是256，更不是512的弱鸡！
是65536长度的寄存器！并且支持近乎无穷的纸条长度！！
数值计算也不再是弱鸡的0-256，而是支持2**64位计算！~~~
上古时代程序员那种纸带长度有限的痛苦将不复存在！来吧！用这玩意儿来写你的程序吧！体验上古时代的打孔编程吧~！
'''
def main():
    if len(sys.argv) == 1:
        brain_fuck_console()
    if len(sys.argv) >= 2:
        if sys.argv[1] in query[2:4]:
            string = str(sys.argv[2]).strip()
            expain_string(string)
        if sys.argv[1] in query[4:6]:
            print(desc)
        if sys.argv[1] in query[6:8]:
            brainfucker.debug = True
            brain_fuck_console()


def brain_fuck_console():
    while 1:
        command = str(input('BrainFuckTapeIn >>> ')).strip()
        brainfucker.execute(command)
        print('')

def expain_string(string):
    brainfucker.execute(string)
    print('')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print('\nexit~')


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
