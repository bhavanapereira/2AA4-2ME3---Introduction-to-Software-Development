package src;

import java.util.HashSet;

public class ProgramT{

	private HashSet<CourseT> s;

	public double[] measures(){
		throw new UnsupportedOperationException;
	}

	public double[] measures(IndicatorT int){
		throw ne UnsupportedOperationException
	}

	public double[] measurs(AttributeT att){
		double[] arr1 = {0,0,0,0};
		for (int i = 0; i < s.size(); i++){
			double[] arr2 = measures(att)[i].measures();
			double[] measureInd = sumMeas(arr1, arr2);
			arr1 = measureInd;					
		}
		Services.normal(measureInd);
	}
}




