package src;


import java.util.ArrayList;

public class Seq1D{

	private ArrayList<Double> s;
	private MeanCalculator meanCalculator;

	public Seq1D(ArrayList<Double> x, MeanCalculator m){
		if (x.size() == 0){
			throw new IllegalArgumentException("Invalid sequence size; must be greater than zero");
		}
		this.s = x;
		this.meanCalculator = m;
	}

	public void setMeanCalculator(MeanCalculator m){
		meanCalculator = m;
	}

	public double mean(){
		return meanCalculator.meanCalc(s);
	}

}