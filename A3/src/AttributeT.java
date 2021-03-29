package src;

import java.util.Arrays;
import java.util.HashSet;


public class AttributeT {

	private String name;
	private HashSet<IndicatorT> s;

	public AttributeT (String attribName, IndicatorT[] indicators){
		 this.name = attribName;
		 s = new HashSet<IndicatorT>();
		 for (int i = 0; i < indicators.length; i++){
		 	s.add(indicators[i]);
		 }
	}

	public String getName(){
		return name;
	}
	
	public IndicatorT[] getIndicators(){
		return s.toArray(new IndicatorT[0]);
	}
}