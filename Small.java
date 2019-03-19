import java.util.Scanner;
public class Small{
	public static void main(String argd[]){
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int temp;
		int[] a=new int[n];
		int[] c=new int[n];
		int i,b=0,j=0,k=0;
		for(i=0;i<n;i++){
			a[i]=sc.nextInt();
		}
		
		for(i=0;i<n;i++){
			for(j=i+1;j<n;j++){
				if(a[i]>a[j]){
					temp=a[i];
				a[i]=a[j];
				a[j]=temp;
				}
				}
		}	
			for(k=0;k<1;k++){
			     System.out.println(a[k]);
		}
		
			}
		
		}
