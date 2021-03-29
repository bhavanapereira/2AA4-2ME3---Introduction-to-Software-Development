package src;


public class Services{

	public static double[] normal(double[] v){
		double[] arr = new double[v.length];
		for (int j = 0; j < v.length; j++){
			arr[j] = v[j] / sum(v);
		}
		return arr;
	}

	private static double sum(double[] v){
		double sum = 0;
		for (int i = 0; i < v.length; i++){
			sum += v[i];
		}
		return sum;
	}
}
