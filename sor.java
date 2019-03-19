import java.util.*;
public class sor
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b[]=new int[a];
        for(int i=0;i<b.length;i++)
        {
            b[i]=sc.nextInt();
        }
        for(int j=0;j<b.length;j++)
        {
            System.out.println(b[j]+" "+j);
        }
    }
}
