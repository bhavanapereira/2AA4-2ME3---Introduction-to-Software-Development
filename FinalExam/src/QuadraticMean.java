package src;

import java.util.ArrayList;
import java.lang.Math;

public class QuadraticMean implements MeanCalculator{

	public double meanCalc(ArrayList<Double> t){
		double sum_of_squares = 0;
		for (int i = 0; i < t.size(); i++){
			sum_of_squares += Math.pow(t.get(i), 2);
		}
		return Math.sqrt(sum_of_squares/t.size());
	}
}