class Stack:
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def depth(self):
        return len(self._items)

def do_math(op,num1,num2):
    if op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    elif op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "^":
        return num1 ** num2


def suf_exp_evaluator(exp):
    """核心求值的函数
    exp:一个项的表"""
    operators="+-*/^"
    st = Stack()
    for x in exp:
        if x not in operators:
            st.push(float(x))  #不能转换则自动引发异常
            continue
        if st.depth()<2:
            raise SyntaxError("short of operand(s).")
        a = st.pop()
        b = st.pop()
        st.push(do_math(x,b,a))
    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Extra operand(s).")


def suffix_exp_evaluator(line):
    """"将后缀表达式的字符串转化为项后再求值"""
    return suf_exp_evaluator(line.split())


# 空格分开的项
print(suffix_exp_evaluator(str( ( 2 + 3 ) * 6 + 4 / 2) ))
