/**
 * @file BoardT.java
 * @author Bhavna Pereira
 * @brief This class Model the game board
 * @date 12/04/2021
 */
package src;
import java.lang.Math;

/**
 * @brief This BoardT type instantiates a double array of integers to simulate a Game board
 *        for the 2048 game
 *@details This class allows for the manipulation and calculations done within the board, to 
 *         alter the game board based on user input. it spawns new numbers onto the board when
 *         necessary, and keeps track of the score as the game progresses
 */
public class BoardT {
	
	private int[][] grid;
	int span = 4;
	private static int score;
	
	/**
	 * @brief This constructor creates an initial game board, prior to any user input
	 * @details This constructor initializes a 4x4 grid with values of 0 in each cell and
	 *          initiates a score of 0
	 */

	public BoardT(){
        this.grid = new int[][]{{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};
        this.score = 0;
	}
	
	/**
	 * @brief The getGrid() method is a getter
	 * @details The method references the grid at any point within the game
	 * @return A grid of type int[][]
	 */
	public int[][] getGrid(){
		return grid;
	}
	
	/**
	 * @brief The getScore() method is a static getter method
	 * @details The method references the score at any point within the game 
	 * @return An integer representing the score.
	 */

	public static int getScore(){
		return score;
	}

    /**
     * @brief The newGrid() method is used to create the beginning state of the board
     * @details This method spawns two numbers on an empty board by calling the newNumber() method
     *          twice
     */
    public void newGrid() {
    	this.newNumber();
    	this.newNumber();		
    }
    
    /**
     * @brief The newNumber() method is used to spawn a number onto the board
     * @details The method creates a boolean value true and generates two random integers between 0 
     *          and 4 to represent a random row and a random column, respectively. It also creates
     *          a random double value. If the cell at the randomly decided position has the value of 0
     *          and the double value is less than 0.1, it will overwrite the cell's value to become 4
     *          and indicates that the cell is no longer empty. Otherwise if the cell has a value of 0, 
     *          it will overwrite it to have a value of 2 and once again indicate that the cell is
     *          no longer empty.      
     */

	public void newNumber(){
		boolean empty = true;
		while (empty){
			int i = (int)(Math.random() * 4);
			int j = (int)(Math.random() * 4);
			double k = Math.random();
			if (grid[i][j] == 0){
				if (k < 0.1){
					grid[i][j] = 4;
					empty = false;
				}
				else{
					grid[i][j] = 2;
					empty = false;
				}
			}
		}
	}
	
	/**
	 * @brief The wonGame() method checks the user has won the game
	 * @details This method iterates through every cell in the grid and checks to see if has a cell
	 *          with the value of 2048. If it does, the user has won. If it does not, the user has not won
	 * @return A boolean value 'true' if the user has won or a boolean value 'false'  if the user has
	 *         not won
	 */

    public boolean wonGame(){
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[i].length; j++){
                if (grid[i][j] == 2048){
                    return true;
                }
            }
        }
        return false;
    }
    
    /**
     * @brief The lostGame() method checks to see if the user has lost the game
     * @details This method iterates through every cell. if any cell value is 0, or has a cell
     *          above, below, or next to it in either direction with the same value as it, the user has
     *          not yet lost. If none of these cases are met, then the user has lost the game.
     * @return A boolean value 'true' if the user has lost the game or a boolean value 'false'
     *         if the user has not lost the game
     */
    public boolean lostGame() {
		for (int i = 0; i < grid.length; i++) {
			for (int j = 0; j < grid[i].length; j++) {
				if (grid[i][j] == 0) {
					return false;
				}
				if (i > 0 && grid[i-1][j] == grid[i][j]) {
					return false;
				}
				if (i < 3 && grid[i+1][j] == grid[i][j]) {
					return false;
				}
				if (j > 0 && grid[i][j-1] == grid[i][j]) {
					return false;
				}
				if (j < 3 && grid[i][j+1] == grid[i][j]) {
					return false;
				}
			}
		}
		return true;
    }
    /**
     * @brief The up() method calls the move() and add() in order to move each cell upward
     * @details The method passes on the necessary parameter "i" of type String to indicate
     *          in which direction the move() and add() methods should slide and combine values
     *          appropriately
     */
    public void up() {
    	move("i");
    	add("i");
    	move("i");
    }
    
    /**
     * @brief The down() method calls the move() and add() in order to move each cell downward
     * @details The method passes on the necessary parameter "k" of type String to indicate
     *          in which direction the move() and add() methods should slide and combine values
     *          appropriately
     */   
    public void down() {
    	move("k");
    	add("k");
    	move("k");
    }

    /**
     * @brief The left() method calls the move() and add() in order to move each cell left
     * @details The method passes on the necessary parameter "j" of type String to indicate
     *          in which direction the move() and add() methods should slide and combine values
     *          appropriately
     */ 
    public void left() {
    	move("j");
    	add("j");
    	move("j");
    }
    
    /**
     * @brief The right() method calls the move() and add() in order to move each cell left
     * @details The method passes on the necessary parameter "l" of type String to indicate
     *          in which direction the move() and add() methods should slide and combine values
     *          appropriately
     */ 
    public void right() {
    	move("l");
    	add("l");
    	move("l");
    }

    /**
     * @brief The move() method moves each cell in a direction specified by its input parameter
     * @details The method moves each cell up if the parameter is equal to "i", down if the parameter is
     *          equal to "k", left if the parameter is equal to "j", or right if the parameter is equal to "l"
     *          It only moves cells over if the adjacent cell in that direction is equal to 0, to avoid overwriting
     *          previously existing values.
     * @param Direction of type String
     */

    private void move(String direction) {
    	if (direction.equals("i")) {
    		for (int i = 0; i < span; i++) {
    			for (int j = 0; j < span; j++) {
    				if(i > 0) {
    					if(grid[i][j] != 0 && grid[i-1][j] == 0) {
    						grid[i-1][j] = grid[i][j];
    						grid[i][j] = 0;
    						move("i");
    					}
    				}
    			}
    		}
    	}
    	else if (direction.equals("k")){
    		for (int i = 0; i < span; i++) {
    			for (int j = 0; j < span; j++) {
    				if(i < 3) {
    					if(grid[i][j] != 0 && grid[i+1][j] == 0) {
    						grid[i+1][j] = grid[i][j];
    						grid[i][j] = 0;
    						move("k");
    					}
    				}
    			}
    		}
    	}
    	else if (direction.equals("j")) {
    		for (int i = 0; i < span; i++) {
    			for (int j = 0; j < span; j++) {
    				if (j > 0) {
    					if(grid[i][j] != 0 && grid[i][j-1] == 0) {
    						grid[i][j-1] = grid[i][j];
    						grid[i][j] = 0;
    						move("j");
    					}
    				}
    			}
    		}
    	}
    	else if (direction.equals("l")) {
    		for (int i = 0; i < span; i++) {
    			for (int j = 0; j < span; j++) {
    				if (j < 3) {
    					if(grid[i][j] !=  0 && grid[i][j+1] == 0) {
    						grid[i][j+1] = grid[i][j];
    						grid[i][j] = 0;
    						move("l");
    					}
    				}
    			}
    		}
    	}
    } 

    
    /**
     * @brief The add() method adds two adjacent cells together if their values are equal, and updates the score.
     * @details If the specified parameter is equal to "i", it will check the value of cell above it and add their 
     *          values if they're equal to one another. It will then overwrite the current cell's value to be 0.
     *          The process of adding values together is the same, except the direction of the adjacent cell differ
     *          based on the input parameter; it checks the left adjacent cell if the parameter is equal to "j", the cell
     *          below it if the parameter is equal to "k", and the right adjacent cell if the parameter is equal to "l" For each
     *          added together value, this method updates the score by the adding to it the same value as the sum of two cells.
     * @param Direction of type string
     */
    private void add(String direction) {
    	if (direction.equals("i")) {
    		for (int i = 1; i < span; i++) {
    			for (int j = 0; j < span; j++) {
    				if (grid[i-1][j] == grid[i][j]) {
    					grid[i-1][j] = 2 * grid[i][j];
    					grid[i][j] = 0;
    					score += grid[i-1][j];
    				}
    			}
    		}
    	}
    	else if (direction.equals("k")){
    		for (int i = 2; i >= 0; i--) {
    			for (int j = 0; j < span; j++) {
    				if (grid[i+1][j] == grid[i][j]) {
    					grid[i+1][j] = 2 * grid[i][j];
    					grid[i][j] = 0;
    					score += grid[i+1][j];
    				}
    			}
    		}
    	}
    	else if (direction.equals("j")){
    		for (int i = 0; i < span; i++) {
    			for (int j = 1; j < span; j++) {
    				if (grid[i][j-1] == grid[i][j]) {
    					grid[i][j-1] = 2 * grid[i][j];
    					grid[i][j] = 0;
    					score += grid[i][j-1];
    				}
    			}
    		}
    	}
    	else if (direction.equals("l")) {
    		for (int i = 0; i < span; i++) {
    			for (int j = 2; j >= 0; j--) {
    				if (grid[i][j+1] == grid [i][j]) {
    					grid[i][j+1] = 2 * grid[i][j];
    					grid[i][j] = 0;
    					score += grid[i][j+1];
    				}
    			}
    		}
    	}
    }
}
