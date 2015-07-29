import java.lang.*;

/**
 * Note that Java console applications need to be run through the java runtime
 * by running "java -jar JarFile.jar" in the command line.
 * Java console applications can not be previewed in the Compilr IDE, only applets can.
 */
public class Program
{
    /**
     * This is the main entry point for the application
     */
    public static int bucketFromRandom(int randomNumber) 
    {
        int a[] = new int[10];
        for (int i = 0; i < a.length; i++)
            a[i] = i * randomNumber;
        int index = Math.abs(randomNumber) % a.length;
        return a[index];
    }
    public static void main(String args[]) 
    {
        int n = 0;
        while(true)
        {
            System.out.println(n);
            bucketFromRandom(n++);
        }
    }
}

