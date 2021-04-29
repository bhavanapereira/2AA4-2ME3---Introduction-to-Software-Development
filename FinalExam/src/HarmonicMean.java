package src;

import java.util.ArrayList;

public class HarmonicMean implements MeanCalculator{


	public double meanCalc(ArrayList<Double> s){
		double sum = 0;
		for (int i = 0; i < s.size(); i++){
			sum += 1/s.get(i);
		}
		return s.size()/sum;
	}
}