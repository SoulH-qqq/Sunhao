class xz:
    def xzsort(self,a):
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                if a[i]>a[j]:
                    tmp=a[j]
                    a[j]=a[i]
                    a[i]=tmp
        return a