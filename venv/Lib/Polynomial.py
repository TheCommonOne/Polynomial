class mynode:
    def __init__(self):
        self.index = 0
        self.coefficient = 0
        self.p = 0
        self.id = 0


class mylist:
    def __init__(self):
        self.head = mynode()
        self.head.id = 1
        self.head.p = mynode()
        self.head.p.id = -1

    def __add__(self, other):
        rtn = mylist()
        now = self.head.p
        while now.id != -1:
            rtn.append(now.index, now.coefficient)
            now = now.p
        now = other.head.p
        while now.id != -1:
            rtn.append(now.index, now.coefficient)
            now = now.p
        rtn.simplify()
        return rtn

    # Too complex __add__
    '''def __add__(self, other):
        if type(other) == mylist:
            # Parameter validity
            if self.head.p.id == -1 and other.head.p.id == -1:
                print("Two Invalid Polynomial")
                return 0
            if self.head.p.id == -1:
                return other
            elif other.head.p.id == -1:
                return self
            else:
                now_left = self.head.p
                rtn = mylist()
                while now_left.id == 0:
                    now_right = other.head.p
                    while now_right.id == 0:
                        if now_right.index == now_left.index:
                            rtn.append(now_right.index, now_left.coefficient+now_right.coefficient)
                            break
                        else:
                            pass
                        now_right = now_right.p
                    if now_right.id == -1:
                        rtn.append(now_left.index, now_left.coefficient)
                    now_left = now_left.p
                now_right = other.head.p
                while now_right.id == 0:
                    now = rtn.head.p
                    while now.id == 0:
                        if now.index == now_right.index:
                            break
                        else:
                            pass
                        now = now.p
                    if now.id != 0:
                        rtn.append(now_right.index, now_right.coefficient)
                    now_right = now_right.p
                return rtn

        elif type(other) == int or type(other) == float:
            now = self.head.p
            while now.id == 0:
                if now.index == 0 and now.coefficient != 0:
                    break
            if now.id == 0:
                now.coefficient += other
            else:
                self.append(0, other)
            return self'''

    # Useless append(self)
    '''def append(self):
        # No chance for if
        if not self.head:
            self.head = mynode()
            self.head.id = 0
            self.head.index = eval(input("Input the Index"))
            self.head.coefficient = eval(input("Input the Coefficient"))
            self.head.p = 0
        else:
            now = self.head
            while now.p.id != -1:
                now = now.p
            temp = mynode()
            temp.p = now.p
            temp.index = eval(input("Input the Index"))
            temp.coefficient = eval(input("Input the Coefficient"))
            now.p = temp
        self.simplify()'''

    def append(self, i=0, c=0):
        # No chance for if
        if not self.head:
            self.head = mynode()
            self.head.id = 0
            self.head.index = eval(input("Input the Index"))
            self.head.coefficient = eval(input("Input the Coefficient"))
            self.head.p = 0
        else:
            now = self.head
            while now.p.id != -1:
                now = now.p
            temp = mynode()
            temp.p = now.p
            if i == 0 and c == 0:
                temp.index = eval(input("Input the Index"))
                temp.coefficient = eval(input("Input the Coefficient"))
            else:
                temp.index = i
                temp.coefficient = c
            now.p = temp
        self.simplify()

    def output(self):
        # Simplified automatically
        i = self.head.p
        while i.id == 0:
            if i.coefficient == 0:
                pass
            else:
                if i.index == 0:
                    if i.coefficient < 0:
                        print("(", i.coefficient, ")", end=' ')
                    else:
                        print(i.coefficient, end=' ')
                else:
                    if i.coefficient < 0:
                        print("(", i.coefficient, ")", 'x^', end=' ')
                    else:
                        print(i.coefficient, 'x^', end=' ')
                    if i.index < 0:
                        print('(', i.index, ')', end=' ')
                    else:
                        print(i.index, end=' ')

            if not i.p.id and i.coefficient != 0:
                print('+', end=' ')

            i = i.p

    def simplify(self):
        # Will Delete the One whose Coefficient is 0
        p1 = self.head.p
        while not p1.id:
            if p1.coefficient != 0:
                p2 = p1.p
                p2_before = p1
                while not p2.id:
                    if p2.coefficient != 0:
                        if p1.index == p2.index:
                            p1.coefficient += p2.coefficient
                            p2_memory = p2.p
                            del p2_before.p
                            p2_before.p = p2_memory
                    p2_before = p2
                    p2 = p2.p
            p1 = p1.p

def main():
    l = mylist()
    l.append()
    l.append()
    l.output()
    print("\n")
    m = mylist()
    m.append()
    m.append()
    m.output()
    print("\n")
    (m+l).output()


main()