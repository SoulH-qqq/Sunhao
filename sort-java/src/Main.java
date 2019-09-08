public class Main {

    public static void main(String[] args) {
        MP m=new MP();
        XZ x=new XZ();
        CR c=new CR();
        Shell s=new Shell();
        Merge mer=new Merge();
        Quick q=new Quick();
        Heap h=new Heap();
        int a[]={4,6,2,1,9,5,7};
        //int b[]=m.sort(a);
        //int b[]=x.sort(a);
        //int b[]=c.sort(a);
        //int b[]=s.sort(a);
        //int b[]=mer.sort(a);
        //int b[]=q.sort(a);
        int b[]=h.sort(a);
        for (int i: b){
            System.out.println(i);
        }
    }
}
