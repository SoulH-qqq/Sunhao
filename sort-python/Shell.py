class shell:
    def shellsort(self,a):
        gap=len(a)//2
        while gap>0:
            for i in range(0,gap):
                for j in range(i+gap,len(a),gap):
                    if a[j]<a[j-gap]:
                        tmp=a[j]
                        k=j-gap
                        while k>=0 and a[k]>tmp:
                            a[k+gap]=a[k]
                            k=k-gap
                        a[k+gap]=tmp
            gap=gap//2
        return a
