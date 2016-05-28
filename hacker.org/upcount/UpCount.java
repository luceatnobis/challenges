import java.lang.System;

public class UpCount {
	private long calc(int depth) {
		if (depth == 0) return 1;
		long cc = calc(depth - 1);
		return cc + (depth % 7) + ((((cc ^ depth) % 4) == 0) ? 1 : 0); 
	}
	private long ncalc(int depth) {
                
		if (depth == 0) return 1;
		long cc = ncalc(depth - 1);
                long m = ((((cc ^ depth) % 4) == 0) ? 1 : 0);
                System.out.println(depth + " " + m);

		return cc + (depth % 7) + m; 
	}
	public static void main(String[] args) {
		UpCount uc = new UpCount();
		UpCount nc = new UpCount();
		// System.out.println(uc.calc(11589));
		// System.out.println(uc.calc(150));
		System.out.println(uc.ncalc(150));
	}
}
