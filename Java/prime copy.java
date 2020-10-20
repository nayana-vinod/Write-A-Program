/* 1.Write a Java program to check if a given number is prime */

public class prime{
    public static void main(final String[] args){

        int n=6,i,k=0;
        for(i=2;i<n/2;i++)
        {

            if(n%i==0)
            {
                System.out.print("The number is not prime");
                k++;
                break;    
            }

       }
       if(k==0)
       {
           System.out.print("The number is prime");
       }

    }
}