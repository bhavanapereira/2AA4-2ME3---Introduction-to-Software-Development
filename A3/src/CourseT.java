/** 
* @file BodyT.py
* @author Bhavna Pereira
* @brief Class implementation of BodyT with the use of Shape.py
* @date 16/02/2021
*/

package src;

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;

/**
* @brief This type instantiates the course, along with the 
*        learning outcomes that are associated with it
* @details This class allows for the manipulation of course properties
*          based on the name of the Course and the Indicators and Learning outcomes
*/
public class CourseT{

	private String name;
	private HashMap<IndicatorT, HashSet<LOsT>> m;

	/**
	* @brief This constructor initializes properties of a course
	* @details The constructor instantiates the course Name, and adds keys
	*          referencing course indicators of type IndicatorT and values
	*          referencing learning outcomes associated with the indicator
	* @param courseName of type String
	* @param indicator of type IndicatorT
	*/

	public CourseT(String courseName, IndicatorT[] indicators){
		this.name = courseName;
		for (int i = 0; i < indicators.length; i++){
			m.put(indicators[i], new HashSet<LOsT>());
		} 
	}

	/**
	* @brief The getName() method is a getter method
	* @details The method references Course Name
	* @returns The method returns the Course Name of type String
	*/
	public String getName(){
		return name;
	}

    /**
    * @brief The getIndicators() method is a getter method the Indicators
    * @details The method converts the set of keys in the given HashMap
    *          into an Array of type IndicatorT
    * @returns The method returns an Array of type IndicatorT
    */
	public IndicatorT[] getIndicators(){
		IndicatorT[] indicators = m.keySet().toArray(new IndicatorT[0]);
		return indicators;
	}

	/**
	* @brief The getLOs() method is a getter method to reference the Learning outcomes 
	*        associated with a specific indicator
	* @details If the provided indicator is in the existing HashMap, if the indicator
	*          is not in the HashMap, it returns an empty Array, otherwise it returns an 
	*          Array listing the learning outcomes associated with that indicator.
	* @param indicator of type IndicatorT
	* @returns an Array of type LOsT
	*/
	public LOsT[] getLOs(IndicatorT indicator){
		if (!m.containsKey(indicator)){
			return new LOsT[0];
		}
		else{
			return set_to_seq(m.get(indicator));
		}
	}

	/**
	* @brief The method addLO() adds a learning outcome to a specific indicator
	* @details If the indicator passed exists within the HashMap, the method adds the inputted
	*          learning out come to the indicator's associated learning outcomes
	* @param indicator of type IndicatorT
	* @param outcome of type LOsT
	*/
	public void addLO(IndicatorT indicator, LOsT outcome){
		if (m.containsKey(indicator)){
			m.get(indicator).add(outcome);
		}
	}

	/**
	* @brief The method delLO() deletes a learning outcome to a specific indicator
	* @details If the indicator passed exists within the HashMap, the method deletes the inputted
	*          learning out come from the indicator's associated learning outcomes
	* @param indicator of type IndicatorT
	* @param outcome of type LOsT
	*/
	public void delLO(IndicatorT indicator, LOsT outcome){
		if (m.containsKey(indicator)){
			m.get(indicator).remove(outcome);
		}	
	}

	/**
	* @brief The method member() returns whether or not a list of learning outcomes is associated with a certain indicator
	* @details If the inputted indicator exists within the HashMap. If it does, it checks if the length of 
	*          the inputted array is equal to the size of the HashSet of learning outcomes associated with the indicator. 
	*          If it is not equal, it returns false. If it does, it iterates through the values of both lists to check if they're
	*          the same. If they are not, the method will return false. If neither case is met, the method returns true, indicating
	*          that the learning outcomes passed are only and exactly the ones associated with the indicator.
	* @param indicator of type IndicatorT
	* @param outcomes , an Array of type LOsT
	* @returns a boolean value, either true or false.
	*/

	public boolean member(IndicatorT indicator, LOsT[] outcomes){
		if (m.containsKey(indicator)){
			if (outcomes.length != m.get(indicator).size()){
				return false;
			}
			for (int i = 0; i < outcomes.length; i++){
				if (!m.containsValue(outcomes[i])) {
					return false;
				}
			}
		}
		return true;
	}

    /**
    * @brief The method measures() checks to see if the Operation is supported
    */
	public double[] measures(){
		throw new UnsupportedOperationException("UnsupportedOperationException");
	}

    /**
    * @brief The method measures()
    */
	public double[] measures(IndicatorT ind){
		if (getLOs(ind).length == 0){
			return new double[] {0,0,0,0};
		}
		else{
			double[] measureInd = new double[4];
			if (Norm.getNInd() == true){
				double[] arr1 = {0,0,0,0};
				for (int i = 0; i < getLOs(ind).length; i++){
					double[] arr2 = getLOs(ind)[i].measures();
					measureInd = sumMeas(arr1, arr2);
					arr1 = measureInd;
				}
				Services.normal(measureInd);		
			}
			else{
				double[] arr1 = {0,0,0,0};				
				for (int i = 0; i < getLOs(ind).length; i++){
					double[] arr2 = getLOs(ind)[i].measures();
					measureInd = sumMeas(arr1, arr2);
					arr1 = measureInd;
				}
			}
			return measureInd;
		}
	}

	public double[] measures(AttributeT att){
		if (getIndicators().length == 0){
			return new double[] {0,0,0,0};
		}
		else{
			double[] measureInd = new double[4];
			if (Norm.getNAtt() == true){
				double[] arr1 = {0,0,0,0};
				for (int i = 0; i < att.getIndicators().length; i++){
					double[] arr2 = measures(att.getIndicators()[i]);
					measureInd = sumMeas(arr1, arr2);
					arr1 = measureInd;
				}
				Services.normal(measureInd);
			}
			else{
				double[] arr1 = {0,0,0,0};
				for (int i = 0; i < att.getIndicators().length; i++){
					double[] arr2 = measures(att.getIndicators()[i]);
					measureInd = sumMeas(arr1, arr2);
					arr1 = measureInd;
				}			
			}
			return measureInd;	
		}
	}

	public LOsT[] set_to_seq(HashSet<LOsT> s){
		return s.toArray(new LOsT[s.size()]);
	}

	public double[] sumMeas(double[] a, double[] b){
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

