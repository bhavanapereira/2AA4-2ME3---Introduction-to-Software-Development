/**
 * Author: 
 * Revised: 
 * 
 * Description: 
 */

package src;

import org.junit.*;
import static org.junit.Assert.*;

public class TestLOsT{
	private String name;
	private String name2;
   	private int n_blw;
    private int bad_n_blw;
    private int zero_n_blw;
    private int n_mrg;
    private int zero_n_mrg;
    private int n_mts;
    private int zero_n_mts;
    private int n_exc;
    private int zero_n_exc;
	private LOsT goodLOsT;
	private LOsT goodLOsT2;
	private LOsT badLOsT;
	private LOsT zeroLOsT;
	private final double tolerance = 1e-3;

    @Before
    public void setUp(){
    	name = "Good";
    	name2 = "Bad";
    	n_blw = 1;
    	bad_n_blw = -1;
    	zero_n_blw = 0;
    	n_mrg = 2;
    	zero_n_mrg = 0;
    	n_mts = 3;
    	zero_n_mts = 0;
    	n_exc = 4;
    	zero_n_exc = 0;

    	goodLOsT = new LOsT(name, n_blw, n_mrg, n_mts, n_exc);
    	goodLOsT2 = new LOsT(name2, n_blw, n_mrg, n_mts, n_exc);

    }

    @After
    public void tearDown(){
    	goodLOsT = null;
    	goodLOsT2 = null;
    	badLOsT = null;
    	zeroLOsT = null;
    }

    @Test (expected = IllegalArgumentException.class)
    public void testNegativeIntExceptionRaise(){
    	LOsT badLOsT = new LOsT(name, bad_n_blw, n_mrg, n_mts, n_exc);      
    }

    @Test (expected = IllegalArgumentException.class)
    public void testZeroIntExceptionRaise(){
    	LOsT zeroLOsT = new LOsT(name, zero_n_blw, zero_n_mrg, zero_n_mts, zero_n_exc);     
    }


    @Test
    public void testGetName(){
    	String expectedName = "Good";
    	assertEquals(expectedName, goodLOsT.getName());
    }

    @Test
    public void testGetName2(){
    	String expectedName = "Good";
    	assertNotSame(expectedName, goodLOsT2.getName());
    }

    @Test
    public void testEqual(){
    	LOsT sameLOsT = new LOsT(name, n_blw, n_mrg, n_mts, n_exc);
    	assertTrue(goodLOsT.equals(sameLOsT));
    }

    @Test
    public void testNotEqual(){
    	LOsT sameLOsT = new LOsT(name2, n_blw, n_mrg, n_mts, n_exc);
    	assertFalse(goodLOsT.equals(sameLOsT));
    }

    @Test
    public void testMeasures(){
    	Norm.setNLOs(false);
    	int[] array = {1,2,3,4};
    	for (int i = 0; i < array.length; i++){
    		assertEquals(array[i], goodLOsT.measures()[i], tolerance);
    	}
    }

}
