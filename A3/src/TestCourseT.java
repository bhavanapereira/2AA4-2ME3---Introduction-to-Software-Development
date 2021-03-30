/**
 * Author: Bhavna Pereira
 * Revised: 
 * 
 * Description:
 */

package src;

import org.junit.*;
import static org.junit.Assert.*;
import java.util.HashSet;
import java.util.Arrays;

public class TestCourseT{

	private String name;
	private String lo1;
	private String lo2;
	private String lo3;
	private CourseT course;
	private IndicatorT[] indList;
	private HashSet<LOsT> learnO;

	@Before
    public void setUp(){
    	name = "LinAlg";
    	indList = new IndicatorT[4];
    	indList[0] = IndicatorT.tools;
    	indList[1] = IndicatorT.math;
    	indList[2] = IndicatorT.assumpt;
    	indList[3] = IndicatorT.modelSelect;

    	lo1 = "Be nice";
    	lo2 = "Have fun";
    	lo3 = "Stay safe";


    	course = new CourseT(name, indList);
    	LOsT one = new LOsT(lo1, 2, 4, 1, 6);
    	LOsT two = new LOsT(lo2, 6, 8, 9, 7);
    	LOsT three = new LOsT(lo3, 5, 7, 3, 4);

    	HashSet<LOsT> learnO = new HashSet<LOsT>();
    	learnO.add(one);
    	learnO.add(two);
    	learnO.add(three);
    }


    @After
    public void tearDown(){
    	indList = null;
    	course = null;
    	learnO = null;
    }

	@Test
    public void testGetName(){
    	String expectedName = "LinAlg";
    	assertEquals(expectedName, course.getName());
    }

    @Test 
    public void testNotGetName(){
    	String expectedName = "LinAlg1";
    	assertNotSame(expectedName, course.getName());
    }

    // @Test
    // public void testGetIndicators(){
    // 	HashSet<IndicatorT> expectedArray = new HashSet<IndicatorT>(Arrays.asList(new IndicatorT[] {IndicatorT.tools, IndicatorT.math, IndicatorT.assumpt, IndicatorT.modelSelect}));
    // 	for (IndicatorT i; course.getIndicators()){
    // 		assertTrue(expectedArray.contains(i));
    // 	}
    // }

    @Test
    public void testGetLOsFalse(){
    	LOsT[] empty = new LOsT[0];
    	for (int i = 0; i < empty.length; i++){
    		assertEquals(empty[i], course.getLOs(IndicatorT.openEnded)[i]);
    	}
    }

    @Test
    public void testGetLOsTrue(){
    	LOsT[] list = new LOsT[]{IndicatorT.tools, IndicatorT.math, IndicatorT.assumpt, IndicatorT.modelSelect};
    	for (int i = 0; i < list.length; i++){
    		assertEquals(list[i], course.getLOs(IndicatorT.openEnded)[i]);
    	}
    }
}
