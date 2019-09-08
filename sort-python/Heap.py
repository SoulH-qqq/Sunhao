def swap(a, max, i):
    pass
    tmp=a[max]
    a[max]=a[i]
    a[i]=tmp

def buildMaxHeap(a,length, i):
    pass
    left=i*2+1
    right=i*2+2
    max=i
    if left<length and a[max]<a[left]:
        max=left
    if right<length and a[max]<a[right]:
        max=right
    if max!=i:
        swap(a,max,i)
        buildMaxHeap(a,length,max)

def sort(a):
    pass
    k=len(a)//2
    for i in range(k,-1,-1):
        buildMaxHeap(a,len(a),i)


class heap:
    def heapsort(self,a):
        sort(a)
        for i in range(len(a)-1,0,-1):
            swap(a,i,0)
            buildMaxHeap(a,i,0)
        return a