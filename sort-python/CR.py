class cr:
    def crsort(self,a):
        for i in range(1,len(a)):
            for j in range(0,i):
                if a[i]<a[j]:
                    tmp=a[i]
                    for k in range(i,j,-1):
                        a[k]=a[k-1]
                    a[j]=tmp
        return a
