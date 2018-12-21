class String(object):
    def __init__(self,sseq):
        self._list=list(sseq)
        self._length=len(self._list)

    def is_empty(self):
        return self._length == 0

    def list(self):
        s = []
        for i in range(self.len()):
            s.append(self._list[i])
        return s

    def len(self):
        return self._length

    def char(self,index):
        if isinstance(index,int) and index<self._length and index>=0:
            return self._list[index]
        else:
            return None

    def substr(self,a,b):
        return String(self._list[a:b])

    def naive_match(self,s):
        """朴素串匹配"""
        p, t =  s.list(),self._list
        m, n = s.len(),self._length
        i,j = 0,0
        while i < m and j < n:
            if p[i] == t[j]:
                i,j = i+1,j+1
            else:
                i,j = 0,j-i+1 #字符不同，考虑t中下一个位置
        if i == m:
            return j-i #找到匹配，返回开始下标
        return -1 #无匹配，返回-1

    def kmp_match(self,s):
        """kmp算法"""
        p, t = s.list(), self._list
        m, n = s.len(), self._length
        i, j = 0, 0
        pnext = self.gen_pnext(p)
        while j<n and i<m:
            if i == -1 or t[j] == p[i]:
                j,i = j+1,i+1
            else:
                i = pnext[i]
        if i == m:
            return j-i
        return -1

    @staticmethod
    def gen_pnext(p):
        """生成针对p中各位置i的下一检查位置表"""
        i,k,m=0,-1,len(p)
        pnext = [-1]*m  #pnext[0]=-1
        while i< m-1:
            # if k=-1 pnext=0且往后推
            # if pi=pk pnext = k+1
            if k == -1 or p[i]==p[k]:
                i = i + 1
                k = k + 1
                if p[i]==p[k]:
                    pnext[i]=pnext[k]
                else:
                    pnext[i] = k
            else:
                k = pnext[k]
        # print(pnext)
        return pnext


    def concat(self,s):
        new_list=[]
        for i in range(self._length):
            new_list.append(self._list[i])
        for i in range(s.len()):
            new_list.append(s.list()[i])
        return String(new_list)

    def subst(self,str1,str2):
        m = str1.len()
        str2_list = str2.list()
        str_list = self.list()
        index = self.kmp_match(str1)
        new_str = []
        while index != -1:
            str_list[index:m+index] = str2_list
            new_str = String(str_list)
            index = new_str.kmp_match(str1)
        return new_str

    def __str__(self):
        s = self._list[0]
        for i in range(1,self.len()):
            s += self._list[i]
        return s

def main():
    s0 = "abcdfgjfsghhabbcabcaabbcaanvssgklzxc"
    s1 = "abbcabcaabbcaa"
    s2 = "ab"
    s3 = "xy"
    string0 = String(s0)
    string1 = String(s1)
    string2 = String(s2)
    string3 = String(s3)
    print(string0.is_empty())
    print(string0.char(3))
    print(string0.concat(string1))
    print(string1.kmp_match(string1))
    print(string0)
    print(string0.subst(string2,string3))
if __name__ == '__main__':
    main()
