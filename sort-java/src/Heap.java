public class Heap {
    public Heap(){};
    public int[] sort(int[] a){
        heapSort(a);
        for (int i=a.length-1;i>=1;i--){
            swap(a,0,i);
            buildMaxHeap(a,i,0);
        }

        return a;
    }

    private void heapSort(int[] a) {
        int k=a.length/2;
        for (int i=k;i>=0;i--){
            buildMaxHeap(a,a.length,i);
        }
    }

    private void buildMaxHeap(int[] a, int length, int i) {
        int left=2*i+1;
        int right=2*i+2;
        int max=i;
        if (left<length&&a[left]>a[max]){
            max=left;
        }
        if (right<length&&a[right]>a[max]){
            max=right;
        }
        if (max!=i){
            swap(a,max,i);
            buildMaxHeap(a,length,max);
        }
    }

    private void swap(int[] a, int max, int i) {
        int tmp=a[max];
        a[max]=a[i];
        a[i]=tmp;
    }
}
