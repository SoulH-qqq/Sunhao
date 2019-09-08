class mp:
    '冒泡排序'
    def mpsort(self,a):
        for i in range(len(a)-1):
            for j in range(len(a)-1-i):
                if a[j]>a[j+1]:
                    tmp=a[j+1]
                    a[j+1]=a[j]
                    a[j]=tmp
        return a