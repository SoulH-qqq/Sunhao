public class XZ {
    public XZ(){};
    public int[] sort(int[] a){
        for (int i=0;i<a.length-1;i++){
            for (int j=i+1;j<a.length;j++){
                if(a[i]>a[j]){
                    int tmp=a[j];
                    a[j]=a[i];
                    a[i]=tmp;
                }
            }
        }
        return a;
    }
}
