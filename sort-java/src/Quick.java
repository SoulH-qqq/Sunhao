public class Quick {
    public Quick(){};
    public int[] sort(int[] a){
        int low=0,high=a.length-1;
        QuickSort(a,low,high);
        return a;
    }

    private void QuickSort(int[] a, int low, int high) {
        if(low<high){
            int i=low;
            int j=high;
            int k=a[i];
            while (i<j){
                while (i<j&&a[j]>k){
                    j--;
                }
                if (i<j){
                    a[i++]=a[j];
                }
                while (i<j&&a[i]<k){
                    i++;
                }
                if (i<j){
                    a[j--]=a[i];
                }
            }
            a[i]=k;
            QuickSort(a,low,i-1);
            QuickSort(a,i+1,high);
        }


    }
}
