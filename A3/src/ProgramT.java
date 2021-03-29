package src;

import java.util.HashSet;

public class ProgramT extends HashSet<CourseT> implements Measures{

	private HashSet<CourseT> s;

	public double[] measures(){
		throw new UnsupportedOperationException("UnsupportedOperationException");
	}

	public double[] measures(IndicatorT ind){
		throw new UnsupportedOperationException("UnsupportedOperationException");
	}

	public double[] measures(AttributeT att){
		double[] array = {0,0,0,0};
		for (CourseT i : this){
			array = sumMeas(array, i.measures(att));
		}
		return Services.normal(array);
	}


	private double[] sumMeas(double[] a, double[] b){
		double[] sum = new double[a.length];
		for (int i = 0; i < a.length; i++){
			sum[i] = a[i];
		}
		for (int j = 0; j < b.length; j++){
			sum[j] = sum[j] + b[j];
		}
		return sum;
	}
}




