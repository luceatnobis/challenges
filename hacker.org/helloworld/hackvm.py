#!/usr/bin/env python

### Imports
import sys,re
from functools import partial

### Constants
MAX_CYCLES=10000

MIN_INT=-(1<<63)
MAX_INT=(1<<63)-1

### Globals
Memory = [0]*16384
CallStack = []
OperandStack = []
ProgramCounter = 0
CycleCounter = 0

### Functions
def Push(v):
    if (v < MIN_INT or v > MAX_INT): raise Exception('integer overflow')
    OperandStack.append(v)
    
def Pop():
    if len(OperandStack) == 0: raise Exception('stack underflow')
    return OperandStack.pop()

def DoPrintChar():
    sys.stdout.write(chr(Pop()&0x7F))

def DoPrintInt():
    sys.stdout.write(str(Pop()))
    
def DoAdd():
    Push(Pop()+Pop())
    
def DoSub():
    a = Pop()
    b = Pop()
    Push(b-a)

def DoMul():
    Push(Pop()*Pop())

def DoDiv():
    a = Pop()
    b = Pop()
    Push(b/a)

def DoCmp():
    a = Pop()
    b = Pop()
    Push(cmp(b,a))
    
def DoGoto():
    global ProgramCounter
    ProgramCounter += Pop()

def DoGotoIfZero():
    global ProgramCounter
    offset = Pop()
    if Pop() == 0: ProgramCounter += offset

def DoCall():
    global ProgramCounter
    CallStack.append(ProgramCounter)
    ProgramCounter = Pop()

def DoReturn():
    global ProgramCounter
    ProgramCounter = CallStack.pop()
    
def DoPeek():
    addr = Pop()
    if addr < 0 or addr >= len(Memory): raise Exception('memory read access violation @'+str(addr))
    Push(Memory[addr])

def DoPoke():
    addr = Pop()
    if addr < 0 or addr >= len(Memory): raise Exception('memory write access violation @'+str(addr))
    Memory[addr] = Pop()

def DoPick():
    where = Pop()
    if where < 0 or where >= len(OperandStack): raise Exception('out of stack bounds @'+str(where))
    Push(OperandStack[-1-where])

def DoRoll():
    where = Pop()
    if where < 0 or where >= len(OperandStack): raise Exception('out of stack @'+str(where))
    v = OperandStack[-1-where]
    del OperandStack[-1-where]
    Push(v)
    
def DoDrop():
    Pop()
    
def DoEnd():
    global ProgramCounter
    ProgramCounter = len(Code)
    
def DoNothing():
    pass

OPS = {
    ' ': DoNothing,
    '\n':DoNothing,
    'p': DoPrintInt,
    'P': DoPrintChar,
    '0': partial(Push, 0),
    '1': partial(Push, 1),
    '2': partial(Push, 2),
    '3': partial(Push, 3),
    '4': partial(Push, 4),
    '5': partial(Push, 5),
    '6': partial(Push, 6),
    '7': partial(Push, 7),
    '8': partial(Push, 8),
    '9': partial(Push, 9),
    '+': DoAdd,
    '-': DoSub,
    '*': DoMul,
    '/': DoDiv,
    ':': DoCmp,
    'g': DoGoto,
    '?': DoGotoIfZero,
    'c': DoCall,
    '$': DoReturn,
    '<': DoPeek,
    '>': DoPoke,
    '^': DoPick,
    'v': DoRoll,
    'd': DoDrop,
    '!': DoEnd
}

### Parse the command line
if len(sys.argv) < 2:
    print 'hackvm.py [--init <init-mem-filename>] [--trace] <code-filename>\nThe format for the initial memory file is: cell0,cell1,...'
    sys.exit(0)

Trace = False
args = sys.argv
args.reverse()
args.pop()
while len(args):
    arg = args.pop()
    if len(args) == 0:
        Code = open(arg).read()
    elif arg == '--trace':
        Trace = True
    elif arg == '--init':    
        initial_memory = re.compile('\s*,\s*').split(open(args.pop()).read())
        #print initial_memory
        for i in range(0,len(initial_memory)):
            Memory[i] = int(initial_memory[i].strip())
    else:
        raise Exception('invalid argument '+arg)
    
### main loop
try:
    while ProgramCounter != len(Code):
        op_code = Code[ProgramCounter]
        if Trace: sys.stderr.write('@'+str(ProgramCounter)+' '+op_code+' ')
        ProgramCounter += 1
        CycleCounter += 1
        if CycleCounter > MAX_CYCLES: raise Exception('too many cycles')
        OPS[op_code]()
        if ProgramCounter < 0 or ProgramCounter > len(Code): raise Exception('out of code bounds')
        if Trace: sys.stderr.write(str(OperandStack)+'\n')
except:
    sys.stderr.write('!ERROR: exception while executing I='+str(op_code)+' PC='+str(ProgramCounter-1)+' STACK_SIZE='+str(len(OperandStack))+'\n')
    sys.stderr.write(str(sys.exc_info()[1])+'\n')
    sys.exit(1)
    
print

