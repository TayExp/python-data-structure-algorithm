class StackUnderflow(ValueError):#栈下溢（访问空栈）
    pass


class LNode(object):
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next = next_


class LStack(object):
    """栈的链接表实现"""
    def __init__(self):
        self._top = None

    def push(self,item):
        """添加一个元素到栈顶"""
        self._top = LNode(item,self._top)

    def pop(self):
        """弹出栈顶元素"""
        if self._top is None:
            raise StackUnderflow("in LStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem

    def peek(self):
        """返回栈顶元素"""
        if self._top is None:
            raise StackUnderflow("in LStack.top()")
        return self._top.elem

    def is_empty(self):
        return self._top is None


def check_parents(text):
    """括号配对检查函数，text是检查的正文串"""
    parents = "()[]{}"
    open_parents = "([{" #开括号字符
    opposite = {")":"(", "]":"[", "}":"{"}

    def parentheses(text):
        """括号生成器，每次调用返回下一括号及位置"""
        i, text_len = 0,len(text)
        while True:
            while i<text_len and text[i] not in parents:
                i += 1
            if i >= text_len:
                return
            yield text[i],i
            i += 1
    st = LStack()  #保存括号的栈
    for pr, i in parentheses(text):
        if pr in open_parents:
            st.push(pr)
        elif st.is_empty():
            print("Unmatching is found at %d for %s." % (i, pr))
            return False  # 出现不匹配
        elif st.pop() != opposite[pr]:
            print("Unmatching is found at %d for %s." %(i,pr))
            return False #出现不匹配
    if st.is_empty():
        print("All parentheses are correctly matched.")
        return True
    else:
        print("Unmatching for redundant:")
        while not st.is_empty():
            print(st.pop(),)
        return False


def main():
    check_parents("{1+[6*(3+5)/4]+4}*}8")


if __name__ == '__main__':
    main()