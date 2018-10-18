# coding=utf-8
def mex(s):
    for i in range(0, len(s) + 1):
        if i not in s:
            return i


class sg_table:  # SG函数表
    def __init__(self):
        self.values = [0, 0]

    def get(self, x):
        for i in range(len(self.values), x + 1):
            succ = set([])
            for j in range(0, i - 1):
                succ.add(self.values[j] ^ self.values[i - 2 - j])
            self.values.append(mex(succ))
        return self.values[x]


def win(string):  # 直接算SG(x)异或
    sg = sg_table()

    total_sg = 0
    contigs = string.split("-")
    for c in contigs:
        total_sg ^= sg.get(len(c))
    if total_sg > 0:
        return True
    else:
        return False
print win('+++++')