from CR import cr
from Heap import heap
from MP import mp
from Merge import merge
from Quick import quick
from Shell import shell
from XZ import xz

a=[45,35,87,1,99,20]
MP=mp()
XZ=xz()
CR=cr()
Shell=shell()
Merge=merge()
Quick=quick()
Heap=heap()
#b=MP.mpsort(a)
#b=XZ.xzsort(a)
#b=CR.crsort(a)
#b=Shell.shellsort(a)
#b=Merge.mergesort(a)
#b=Quick.quicksort(a)
b=Heap.heapsort(a)
print(b)