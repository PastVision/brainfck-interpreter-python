import sys
class brainF:
    chars = '<>.,+-[]'

    def __init__(self,bfCode,regSize=200):
        self.pointer =  0
        self.regSize = regSize
        self.register = [0]*self.regSize
        self.bfCode = self.fixCode(bfCode)
        self.execute(self.bfCode)

    def fixCode(self, cod):
        newCode = ''
        for i in cod:
            if i in self.chars:
                newCode += i
        return newCode
    
    def incPtr(self):
        self.pointer = 0 if self.pointer == self.regSize-1 else self.pointer + 1

    def decPtr(self):
        self.pointer = self.regSize-1 if self.pointer == 0 else self.pointer - 1
    
    def incVal(self):
        self.register[self.pointer] = 0 if self.register[self.pointer] == 255 else self.register[self.pointer] + 1

    def decVal(self):
        self.register[self.pointer] = 255 if self.register[self.pointer] == 0 else self.register[self.pointer] - 1
    
    def out(self):
        print(chr(self.register[self.pointer]),end="")

    def inp(self):
        i = input()
        if len(i)==1:
            self.register[self.pointer] = ord(i)
        else:
            print(f'Input Error! Expected 1 character, got {len(i)}! Exiting!')
            quit()

    def loop(self, bfcode):
        while True:
            self.execute(bfcode)
            if self.register[self.pointer] == 0:
                break
        return

    def execute(self, bfcode):
        pC,pLen=0,len(bfcode)
        cmd = {
            '>':self.incPtr,
            '<':self.decPtr,
            '+':self.incVal,
            '-':self.decVal,
            '[':self.loop,
            ',':self.inp,
            '.':self.out
        }
        while True:
            if pC == pLen:
                break
            if bfcode[pC] == '[':
                self.endL = bfcode[pC:].find(']') + pC
                loopCode = bfcode[pC+1:self.endL]
                self.loop(loopCode)
                pC += len(loopCode)+2
                continue
            cmd[bfcode[pC]]()
            pC+=1


def main():
    with open(sys.argv[1],'r') as f:
            brainF(f.read())
            print('')


if __name__=='__main__':
    main()