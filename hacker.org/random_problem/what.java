public class what{
	public static void main(String[] args){
		for(int i = 2147483647;i<=1000000000;i++){
			System.out.println(bucketFromRandom(i));
		}
	}
	public static int bucketFromRandom(int randomNumber) {
		int a[]	= new int[10];
		for (int i = 0; i < a.length; i++)
			a[i] = i * randomNumber;
		int index = Math.abs(randomNumber) % a.length;
		return a[index];
	}
}
