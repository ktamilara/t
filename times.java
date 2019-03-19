import java.util.*;
import java.lang.*;
import java.io.*;

class times
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner s = new Scanner (System.in);
		int n = s.nextInt();
		int hr,min;
		hr=n/60;
		min=n%60;
		System.out.print(hr + " " +min);
	}
}
