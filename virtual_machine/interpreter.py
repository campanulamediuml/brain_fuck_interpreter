# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Author     ：Campanula 梦芸 何
from error import error_info

MOVE_L = '<'
MOVE_R = '>'
V_ADD = '+'
V_SUB = '-'
STD_O = '.'
STD_I = ','
LOOP_I = '['
LOOP_O = ']'

LAN_DESC_I = 'BrainFuckINBOX'
LAN_DESC_O = 'BrainFuckOUTBOX'

TAPE_LENGTH = 65536
MOD_DATA = 0
byte_mode = 2 ** 8


class Interpreter(object):

    def __init__(self):
        self.memory = [0] * TAPE_LENGTH
        self.tape_string = ''
        self.pointer = 0
        self.executor_pointer = 0
        self.debug = False
        self.command_table = self.init_table()

    def init_table(self):
        command_table = {
            MOVE_L: self.move_l,
            MOVE_R: self.move_r,
            V_ADD: self.v_add,
            V_SUB: self.v_sub,
            STD_O: self.std_o,
            STD_I: self.std_i,
            LOOP_I: self.jump_r,
            LOOP_O: self.jump_l,
        }
        return command_table

    def move_l(self):
        self.pointer = (self.pointer - 1) % TAPE_LENGTH
        self.executor_pointer += 1

    def move_r(self):
        self.pointer = (self.pointer + 1) % TAPE_LENGTH
        self.executor_pointer += 1

    def v_add(self):
        self.memory[self.pointer] = (self.memory[self.pointer] + 1) % byte_mode
        self.executor_pointer += 1

    def v_sub(self):
        self.memory[self.pointer] = (self.memory[self.pointer] - 1) % byte_mode
        self.executor_pointer += 1

    def std_i(self):
        try:
            inbox = int(input('%s > ' % LAN_DESC_I))
            try:
                letter = inbox.to_bytes(8, "little").decode()
            except:
                letter = 'Not_ASCII'
            print(inbox, '--->', letter)
        except:
            print('INVALID ASCII CODE!')
            return
        self.memory[self.pointer] = inbox % byte_mode
        self.executor_pointer += 1

    def std_o(self):
        value: int = self.memory[self.pointer]
        try:
            outbox = value.to_bytes(8, "little").decode()
        except:
            outbox = 'Not_ASCII'
        print(value, '--->', outbox)
        self.executor_pointer += 1

    def jump_r(self):
        """
        跳转
        :return:
        """
        start_loop = 1
        cur_executor = self.executor_pointer
        if self.memory[self.pointer] != 0:
            self.executor_pointer += 1
            return
        while start_loop > 0:
            cur_executor += 1
            if self.tape_string[cur_executor] == LOOP_I:
                start_loop += 1
            if self.tape_string[cur_executor] == LOOP_O:
                start_loop -= 1
        self.executor_pointer = cur_executor
        self.executor_pointer += 1

    def jump_l(self):
        """
        跳转
        :return:
        """
        end_loop = 1
        cur_executor = self.executor_pointer
        if self.memory[self.pointer] == 0:
            self.executor_pointer += 1
            return
        while end_loop > 0:
            cur_executor -= 1
            if self.tape_string[cur_executor] == LOOP_O:
                end_loop += 1
            if self.tape_string[cur_executor] == LOOP_I:
                end_loop -= 1
        self.executor_pointer = cur_executor
        self.executor_pointer += 1

    def execute(self, tape):
        tape = tape.split('//')[0].strip()
        for i in tape:
            if i not in self.command_table:
                return print('EXECUTE_ERR --->', error_info.INVALID_COMMAND, i)
        self.tape_string += tape
        while 1:
            if self.executor_pointer >= len(self.tape_string):
                return
            # print(self.executor_pointer,len(self.tape_string))
            command = self.tape_string[self.executor_pointer]
            func = self.command_table.get(command)
            r = func()
            self.dbg(command)
            if r is not None:
                print('EXECUTE_ERR --->', r)
                return

    def dbg(self, command):
        if self.debug == True:
            print('当前指针 >>', self.pointer)
            print('当前数值 >>', self.memory[self.pointer])
            print('解释器已走到 >>', self.executor_pointer)
            print('本次执行命令 >>', command)
            print('------------------------')


brainfucker = Interpreter()

if __name__ == '__main__':
    brainfucker.execute(
        '++++++++[>++++[>++>+++>+++>+>+<<<<<-]>+>+>->+[<]<-]>>.>---.+++++++..+++.>>++++.>.<<-.<.+++.------.--------.>>>+.')
