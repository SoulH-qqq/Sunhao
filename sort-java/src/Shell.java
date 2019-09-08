public class Shell {
    public Shell(){};
    public int[] sort(int[] a){
        int gap,len;
        len=a.length;
        for (gap=len/2;gap>0;gap=gap/2){
            for (int i=0;i<gap;i++){
                for (int j=i+gap;j<len;j+=gap){
                    if (a[j]<a[j-gap]){
                        int tmp=a[j];
                        int k=j-gap;
                        while (k>=0&&a[k]>tmp){
                            a[k+gap]=a[k];
                            k=k-gap;
                        }
                        a[k+gap]=tmp;
                    }
                }
            }
        }
        return a;
    }
}
