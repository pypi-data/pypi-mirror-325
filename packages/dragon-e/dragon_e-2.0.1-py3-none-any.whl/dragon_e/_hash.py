import numpy as np


def make_signed_32(n: int) -> int:
  while n > 2**31:
    n -= 2**32
  while n < -(2**31):
    n += 2**32
  return n

def right_rotate(inp: str, n: int) -> str:
  lst = [*str(inp)]
  arr = np.array(lst)
  arr = np.roll(arr, n)
  arr = arr.tolist()
  return ''.join(arr)

class hash:
    def __init__(self, inp: str):
        if len(inp) > 55:
            raise Exception("Hash currently only supports strings of length 55 or less")
        bytesList = [hex(ord(i)) for i in inp]
        msgBlock = ['0x00' for _ in range(7)]
        msgBlock.append(hex(len(bytesList)*8))
        bytesList.append(hex(128))
        if len(bytesList)+len(msgBlock) < 64:
            bytesList.extend(['0x00' for _ in range(64-len(bytesList)-len(msgBlock))])
        elif len(bytesList)+len(msgBlock) > 64:
            bytesList.extend(['0x00' for _ in range(64*(((len(bytesList)+len(msgBlock))//64)+1)-len(bytesList)-len(msgBlock))])
        bytesList.extend(msgBlock)
        schedule = ""
        for i in range(len(bytesList)):
            schedule += (f"{int(bytesList[i],16):#010b}"+('\n' if (i+1)%4 == 0 and i != 0 else ''))[2:]
        schedule = schedule.split('\n')[:-1]
        for i in range(48):
            temp = [int(right_rotate(schedule[1+i],7),2),int(right_rotate(schedule[1+i],18),2),int(schedule[1+i],2)>>3]
            res = [temp[0] ^ temp[1] ^ temp[2]]
            temp = [int(right_rotate(schedule[14+i],17),2),int(right_rotate(schedule[14+i],19),2),int(schedule[14+i],2)>>10]
            res.extend([temp[0] ^ temp[1] ^ temp[2]])
            res = make_signed_32(int(schedule[i],2))+make_signed_32(res[0])+make_signed_32(int(schedule[9+i],2))+make_signed_32(res[1])
            schedule.extend([bin(res)[(2 if bin(res)[0] != "-" else 3):]])
        for i in range(len(schedule)):
            schedule[i] = f"{int(hex(int(schedule[i],2)),16):#034b}"[2:]
        a = "01101010000010011110011001100111"
        b = "10111011011001111010111010000101"
        c = "00111100011011101111001101110010"
        d = "10100101010011111111010100111010"
        e = "01010001000011100101001001111111"
        f = "10011011000001010110100010001100"
        g = "00011111100000111101100110101011"
        h = "01011011111000001100110100011001"
        H = [a,b,c,d,e,f,g,h]
        k = """01000010100010100010111110011000
    01110001001101110100010010010001
    10110101110000001111101111001111
    11101001101101011101101110100101
    00111001010101101100001001011011
    01011001111100010001000111110001
    10010010001111111000001010100100
    10101011000111000101111011010101
    11011000000001111010101010011000
    00010010100000110101101100000001
    00100100001100011000010110111110
    01010101000011000111110111000011
    01110010101111100101110101110100
    10000000110111101011000111111110
    10011011110111000000011010100111
    11000001100110111111000101110100
    11100100100110110110100111000001
    11101111101111100100011110000110
    00001111110000011001110111000110
    00100100000011001010000111001100
    00101101111010010010110001101111
    01001010011101001000010010101010
    01011100101100001010100111011100
    01110110111110011000100011011010
    10011000001111100101000101010010
    10101000001100011100011001101101
    10110000000000110010011111001000
    10111111010110010111111111000111
    11000110111000000000101111110011
    11010101101001111001000101000111
    00000110110010100110001101010001
    00010100001010010010100101100111
    00100111101101110000101010000101
    00101110000110110010000100111000
    01001101001011000110110111111100
    01010011001110000000110100010011
    01100101000010100111001101010100
    01110110011010100000101010111011
    10000001110000101100100100101110
    10010010011100100010110010000101
    10100010101111111110100010100001
    10101000000110100110011001001011
    11000010010010111000101101110000
    11000111011011000101000110100011
    11010001100100101110100000011001
    11010110100110010000011000100100
    11110100000011100011010110000101
    00010000011010101010000001110000
    00011001101001001100000100010110
    00011110001101110110110000001000
    00100111010010000111011101001100
    00110100101100001011110010110101
    00111001000111000000110010110011
    01001110110110001010101001001010
    01011011100111001100101001001111
    01101000001011100110111111110011
    01110100100011111000001011101110
    01111000101001010110001101101111
    10000100110010000111100000010100
    10001100110001110000001000001000
    10010000101111101111111111111010
    10100100010100000110110011101011
    10111110111110011010001111110111
    11000110011100010111100011110010""".split('\n')
        for i in range(64):
            s1 = int(right_rotate(e,6),2) ^ int(right_rotate(e,11),2) ^ int(right_rotate(e,25),2)
            ch = ""
            for j in range(len(e)):
                if e[j] == 0:
                    ch += g[j]
                else:
                    ch += f[j]
            ch = int(ch,2)
            Temp1 = make_signed_32(int(h,2)+ch+s1+int(k[i],2)+int(schedule[i],2))
            s0 = int(right_rotate(a,2),2) ^ int(right_rotate(a,13),2) ^ int(right_rotate(a,22),2)
            maj = ""
            for j in range(len(a)):
                try:
                    maj += ("0" if int(a[j])+int(b[j])+int(c[j]) < 2 else "1")
                except:
                   raise Exception(f"what the fuck apparently {j} is out of range for {a}, {b}, or {c}")
            Temp2 = int(maj,2)+s0
            h = g
            g = f
            f = e
            e = f"{make_signed_32(Temp1 + int(d,2)):#035b}"[-32:]
            d = c
            c = b
            b = a
            a = f"{make_signed_32(Temp1 + Temp2):#035b}"[-32:]
        res = ""
        H2 = [a,b,c,d,e,f,g,h]
        for i in range(len(H)):
           res += f"{int(H[i],2)+int(H2[i],2):#035b}"[-32:]
        self.res = res
    def hexdigest(self):
        return str(hex(int(self.res,2)))[-32:]
    def bindigest(self):
        return self.res