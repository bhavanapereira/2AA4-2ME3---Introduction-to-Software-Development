/**
 * Author: Bhavna Pereira
 * Revised: 
 * 
 * Description: Class to test AttributeT.java
 */

package src;

import org.junit.*;
import static org.junit.Assert.*;
import java.util.Arrays;

public class TestAttributeT {

	private IndicatorT[] indList;
    private AttributeT attEmpty;
    private AttributeT attTest;

    @Before
    public void setUp(){
    	indList = new IndicatorT[3];
    	indList[0] = IndicatorT.tools;
    	indList[1] = IndicatorT.math;
    	indList[2] = IndicatorT.assumpt;

    	attEmpty = new AttributeT("AttF", new IndicatorT[0]);
    	attTest = new AttributeT("AttS", indList);
    }

    @After
    public void tearDown(){
    	indList = null;
    	attEmpty = null;
    	attTest = null;
    }

    @Test
    public void testGetName(){
    	String expectedName = "AttF";
        assertEquals(expectedName, attEmpty.getName());
    }

    @Test
    public void testGetName2(){
    	String expectedName = "AttS";
        assertNotSame(expectedName, attEmpty.getName());
    }

    @Test
    public void testGetIndicators(){
    	IndicatorT[] expectedArray = {IndicatorT.math, IndicatorT.assumpt, IndicatorT.tools};
    	for (int i = 0; i < indList.length; i++){
    		assertEquals(expectedArray[i], attTest.getIndicators()[i]);
    	}
    }

    @Test
    public void testGetIndicators2(){
    	IndicatorT[] expectedArray = {IndicatorT.tools, IndicatorT.math, IndicatorT.assumpt};
    	for (int i = 0; i < indList.length; i++){
    		assertNotSame(expectedArray[i], attTest.getIndicators()[i]);
    	}
    }

}
