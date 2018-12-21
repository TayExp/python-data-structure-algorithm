from suffix_evaluator import *

# 优先级
priority = {"(":1, "+":3, "-":3,"*":5, "/":5}
infix_operators = "+-*/()"


def tokens(line):
    """生成器函数，逐一生成line中的一个个项。
    不能处理一元运算符，不能处理带符号的浮点数"""
    i, llen = 0, len(line)
    while i < llen:
        while i < llen and line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operators:
            yield line[i]
            i += 1
            continue
        # 非空格 非运算符
        j = i + 1
        while (j < llen and not line[j].isspace() and
                line[j] not in infix_operators):
            if ((line[j] == 'e' or line[j] == 'E') and
                    j+1<llen and line[j+1] == '-'):
                j += 1
            j += 1
        yield line[i:j]
        i = j


def trans_infix_suffix(line):
    st = Stack()
    exp = []

    for x in tokens(line):
        if x not in infix_operators: # 运算对象
            num = ""
            for i in x:
                num = num + i
            exp.append(num)
        elif st.isEmpty() or x == '(':# 左括号直接进栈，栈空无需比较运算符直接进栈
            st.push(x)
        elif x == ')': # 处理右括号
            while not st.isEmpty() and st.peek() != '(':
                exp.append(st.pop())
            if st.isEmpty():
                raise SyntaxError("Missing '('.")
            # 直到遇到了左括号
            st.pop()

        else: # 处理算术运算符
            # 要看到下个运算符x不高于st.peek时才将st.peek送入exp
            while not st.isEmpty() and (priority[x] <= priority[st.peek()]):
                exp.append(st.pop())
            st.push(x)

    while not st.isEmpty(): #送出栈里剩下的运算符
        if st.peek() == '(':
            raise SyntaxError("Extra '('.")
        exp.append(st.pop())
    return exp


def test_trans_infix_suffix(s):
    print(s)
    print(trans_infix_suffix(s))
    print("Values:", suffix_exp_evaluator(trans_infix_suffix(s)))


if __name__ == '__main__':
    s = " ( 3 -5) * (6+ 17*4) / 3e2"
    test_trans_infix_suffix(s)