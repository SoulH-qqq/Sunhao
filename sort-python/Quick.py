def sort(low, high, a):
    pass
    if low<high:
        i=low
        j=high
        k=a[i]
        while i<j:
            while i<j and a[j]>=k:
                j-=1
            if i<j:
                a[i]=a[j];i+=1
            while i<j and a[i]<k:
                i+=1
            if i<j:
                a[j]=a[i];j-=1
        a[i]=k
        sort(low,i-1,a)
        sort(i+1,high,a)

class quick:
    def quicksort(self,a):
        low=0
        high=len(a)-1
        sort(low,high,a)
        return a