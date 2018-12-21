# 表达式不变，用tuble好了

# 表达式构造函数
def make_sum(a,b):
    return ('+', a, b)
def make_prod(a,b):
    return ('*', a, b)
def make_diff(a,b):
    return ('-', a, b)
def make_div(a,b):
    return ('/', a, b)

# 区分是基本表达式（数，可直接处理）还是复合表达式(a是tuble，需要递归处理)
def is_basic_exp(a):
    return not isinstance(a, tuple)

def is_number(x):
    return (isinstance(x, int) or isinstance(x, float) or isinstance(x, complex))

# 对整个表达式求值
def eval_exp(e):
    if is_basic_exp(e):
        return e
    op, a, b = e[0], eval_exp(e[1]) , eval_exp(e[2])
    if op == '+':
        return eval_sum(a, b)
    if op == '-':
        return eval_diff(a, b)
    if op == '*':
        return eval_prod(a, b)
    if op == '/':
        return eval_div(a, b)


# 对一个表达式求值
def eval_sum(a,b):
    if is_number(a) and is_number(b):
        return a + b
    # if is_number(a) and a == 0:
    #     return b
    # if is_number(b) and b == 0:
    #     return a
    return make_sum(a, b)

def eval_diff(a,b):
    if is_number(a) and is_number(b):
        return a - b
    # if is_number(b) and b == 0:
    #     return a
    return make_diff(a, b)

def eval_prod(a,b):
    if is_number(a) and is_number(b):
        return a * b
    # if is_number(a):
    #     if a == 0:
    #         return 0
    #     elif a == 1:
    #         return b
    # if is_number(b):
    #     if b == 0:
    #         return 0
    #     elif b == 1:
    #         return a
    return make_prod(a, b)

def eval_div(a,b):
    if is_number(a) and is_number(b):
        return a / b
    # if is_number(a) and a == 0:
    #     return 0
    # if is_number(b) and b == 1:
    #     return a
    if is_number(b) and b == 0:
        raise ZeroDivisionError
    return make_div(a, b)
e1 = make_diff(0,make_diff(make_div(35.0,make_prod(4,7)),make_prod(3,make_sum(2,5))))
print(e1)
print(eval_exp(e1))