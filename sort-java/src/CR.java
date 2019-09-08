public class CR {
    public CR(){};
    public int[] sort(int[] a){
        for (int i=1;i<a.length;i++){
            for (int j=0;j<i;j++){
                if (a[i]<a[j]){
                    int tmp=a[i];
                    for (int k=i;k>j;k--){
                        a[k]=a[k-1];
                    }
                    a[j]=tmp;
                }
            }
        }
        return a;
    }
}
