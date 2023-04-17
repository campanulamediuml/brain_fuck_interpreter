## Brain Fuck Interpreter

- 一个效果酷炫的brainfuck解释器，采用65536个内存地址的环状结构，当地址小于0后会回环到最大地址，反之亦然，永远不用担心>>>>>
  溢出啦！
- 支持近乎无穷长度的纸带录入，采用控制台交互模式的话，只要一直输入代码，就能一直执行下去，再也不用担心纸带用完啦！
- 输入内容必须是数字，输出内容是数字，但是，我想输文字怎么办？？不要紧，不管输入输出，控制台同时还会告诉你这次输入的数字对应的ascii字符！

```brainfuck
++++++++[>++++[>++>+++>+++>+>+<<<<<-]>+>+>->+[<]<-]>>.>---.+++++++..+++.>>++++.>.<<-.<.+++.------.--------.>>>+.

```

你别笑！这可是图灵完备的语言！如果你愿意，甚至可以等价翻译成简单的汇编

## 简单的食用指南

### 导包执行模式

```python
from virtual_machine.interpreter import brainfucker

tape = '++++++++[>++++[>++>+++>+++>+>+<<<<<-]>+>+>->+[<]<-]>>.>---.+++++++..+++.>>++++.>.<<-.<.+++.------.--------.>>>+.'

brainfucker.execute(tape)
# 执行这条纸带

brainfucker.debug = True
brainfucker.execute(tape)
# 此时可以输出每一个brainfuck指令符的执行过程！特别酷炫哦

```

### 命令行执行模式

```shell
python main.py 
```

进入控制台后

```shell
BrainFuckTapeIn >>>
```

允许大段大段输入指令，非常有写打孔纸带的快感

### 带调试的执行模式

```shell
python main.py -D
```

此时控制台会显示出每一个语句的执行过程

### 直接执行语句模式

```shell
python main.py -C '++++++++[>++++[>++>+++>+++>+>+<<<<<-]>+>+>->+[<]<-]>>.>---.+++++++..+++.>>++++.>.<<-.<.+++.------.--------.>>>+.'
```

程序将会直接运行你的打孔纸带

## 关于brain fuck

这可是一个著名的图灵完备语言

### 简单的brainfuck语法

brainfuck可以理解为是对图灵机的完全模拟

计算机对指令纸带上逐个符号进行执行，同时计算机内拥有一条有限或无限长度的内存，每一个位置的数据都为0，指针初始位置指向地址为0的内存块

```
> 内存指针右移一个地址

< 内存指针左移一个地址

+ 当前指针指向的内存块内的数据+1

- 当前指针指向的内存块内的数据-1

. 把当前内存块内的数据输出到控制台

, 从控制台读取一个小于2^8的数字，写入控制台(本解释器中输入一个大于255的数字会被自动取256模)

[ 如果当前指针指向的内存块数据为0，则跳转到对应的]后执行

] 如果当前指针指向的内存块数据不为0，则跳转到对应的[后执行
```

看，语法很简单吧，现在，我们可以尝试着用brainfuck写一个简单的减法器了

```
,>++++++[<-------->-]<.
```

首先读取控制台中的一个数储存在地址0内，左移一格内存，在地址1的内存中写入6作为计数器，之后回到储存数字的内存地址，进行8次-1，然后令计数器-1，直到计数器归零后输出地址0的数字
等于对地址0进行了6次批量-1的计算，每次计算为8次-1，总计6*8 = 48次减一

同理

```
,>++++++++[<------>-]<.
```

也能输出完全相同的结果

现在你对brainfuck或者打孔编程有一点简单的概念了吧？好了，我们开始尝试着用它来写一个网络app，或者做个3A游戏吧！