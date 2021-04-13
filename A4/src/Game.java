/**
 * @file Game.java
 * @author Bhavna Pereira
 * @brief This class takes information from the controller and passes it to the model
 * @date 12/04/2021
 */
package src;
import src.Display;
import src.BoardT;
import java.util.Arrays;

/**
 * @brief This class is a module that refers to the input provided by Controller.java
 *        and calls on the necessary methods from BoardT.java to accomplish the appropriate
 *        modeling of the grid. it instantiates a new object of type BoardT, which serves as
 *        the board the user plays on.
 */

public class Game {
	
	private static BoardT b = new BoardT(); 
	
	
	/**
	 * @brief The getBoard() method is a static getter method
	 * @details This method references the game board at any state within the game
	 * @return The board of type BoardT
	 */
	public static BoardT getBoard() {
		return b;
	}
	
	/**
	 * @brief The same() method duplicates a given double array of integers
	 * @details This creates a new double array of the same size as the double array passed into the method. It then
	 *          makes every cell's value of the created double array equal to the value of the corresponding cell of the
	 *          double array passed into the method.
	 * @param grid, a double array of integers.
	 * @return a double array of integers
	 */
	
	public static int[][] same(int[][] grid) {
		int[][] after = new int[grid.length][grid.length];
		for (int i = 0; i < grid.length; i++) {
			for (int j = 0; j < grid[i].length; j++) {
				after[i][j] = grid[i][j];
			}
		}
		return after;
	}
	
	/**
	 * @brief The whereToGo() method calls on the appropriate method in BoardT.java to move the cells 
	 *        of the grid in the direction specified by the user input
	 * @details The method creates new double array of integers equal to the grid prior to moving the cells. It then
	 *          calls on the up() method in BoardT.java if the String passed into the function is equal to "i",
	 *          the down() method in BoardT.java if the String passed in is equal to "k", the left() in BoardT.java
	 *           method if the String passed in is equal to "j", or the right() method if the String passed in is
	 *           equal to "l". It then creates another double array of integers equal to the grid after calling one of
	 *           these methods. It compares the two created double arrays; if they are not the same, it will spawn a
	 *           new number onto the grid. After each move, it will check the game status to see if the user has won or
	 *           lost after their latest move.
	 * @param direction of type String.
	 */
	public static void whereToGo(String direction){
		int[][] before = same(b.getGrid());
		if (direction.equals("i")) {
			b.up();
		}
		else if (direction.equals("k")){
			b.down();
		}
		else if (direction.equals("j")){
			b.left();
		}
		else if (direction.equals("l")){
			b.right();
		}
		int[][] after = same(b.getGrid());
		if (!Arrays.equals(before, after)) {
			b.newNumber();
		}
		checkGameStatus();
	}


	/**
	 * @brief The restGame() method creates a fresh board to play on
	 * @details This method assigns the created grid to a new BoardT object and then calls on 
	 *          the newGrid() method from BoardT.java to spawn two new numbers onto the grid.
	 */
	public static void resetGame() {
		b = new BoardT();
		b.newGrid();
	}
	
	/**
	 * @brief The checkGameStatus() method used BoardT.java to check if the user has lost or won the game,
	 *        display a message to notify the user accordingly and reset the game board
	 * @details The method checks to see if the user has won using the wonGame() method from BoardT.java.
	 *          if the returned boolean is 'true', this method will display the winMessage() from Display.java
	 *          it then resets the game using resetGame(). If the user has not won, the method checks to see
	 *          if the user has lost the game using the lostGame() method from BoardT. if the returned boolean
	 *          is 'true', this method will display the loseMessage() 
	 */
	public static void checkGameStatus() {
		if (b.wonGame()) {
			Display.winMessage();
			resetGame();
		}
		else if (b.lostGame()) {
			Display.loseMessage();
			resetGame();
		}
	}
		


}
