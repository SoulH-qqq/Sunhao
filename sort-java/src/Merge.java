public class Merge {
    public Merge(){};
    public int[] sort(int[] a){
        int low=0,high=a.length-1;
        Mergesort(a,low,high);
        return a;
    }

    private void Mergesort(int[] a,int low, int high) {
        int mid;
        if (low<high){
            mid=(low+high)/2;
            Mergesort(a,low,mid);
            Mergesort(a,mid+1,high);
            merge(a,low,mid,high);
        }

    }

    private void merge(int[] a, int low, int mid, int high) {
        int b[]=new int[high-low+1];
        int p=0,i=low,j=mid+1;
        while (i<=mid&&j<=high){
            b[p++]=(a[i]<=a[j])?a[i++]:a[j++];
        }
        while (i<=mid){
            b[p++]=a[i++];
        }
        while (j<=high){
            b[p++]=a[j++];
        }
        for (p=0,i=low;i<=high;p++,i++){
            a[i]=b[p];
        }

    }

}
