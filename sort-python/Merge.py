def mer(low, mid, high,a):
    pass
    i=low;j=mid+1;p=0
    b=[0]*(high-low+1)
    while i<=mid and j<=high:
        if a[i]<a[j]:
            b[p]=a[i]
            i+=1;p+=1
        else:
            b[p]=a[j]
            j+=1;p+=1
    while i<=mid:
        b[p]=a[i]
        i+=1;p+=1
    while j<=high:
        b[p]=a[j]
        j+=1;p+=1
    m=0
    for n in range(low,high+1):
        a[n]=b[m]
        m+=1


def separate(low, high,a):
    pass
    mid=(low+high)//2
    if low<high:
        separate(low,mid,a)
        separate(mid+1,high,a)
        mer(low,mid,high,a)


class merge :
    def mergesort(self,a):
        low=0
        high=len(a)-1
        separate(low,high,a)
        return a