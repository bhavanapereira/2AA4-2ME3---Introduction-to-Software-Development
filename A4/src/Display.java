/**
 * @file Display.java
 * @author Bhavna Pereira
 * @brief This class is the View Module
 * @date 12/04/2021
 */

package src;

public class Display {
	
	
	/**
	 * @brief The introMessage() method is used to display a message at the beginning of the game
	 * @details The method prints out a welcome message, along with the objective of the game
	 */
	public static void introMessage() {
		System.out.print("Welcome! Can you reach 2048?");
	}
	
	/**
	 * @brief The instructions() method is used to display a message at the beginning of the game
	 * @details The method prints out the appropriate keys the program recognizes and the direction
	 *          they correspond with
	 */
	public static void instructions() {
		System.out.println("Use 'i=up', 'k=down', 'j=left', 'l=right'");
	}
	
	public static void prompt() {
		System.out.println("which direction?");
	}
	
	/**
	 * @brief The errorMessage() method is used to display a message if the user enters an invalid input
	 * @details The method prints out that the user has not entered a recognizable key, and reinforms them of
	 *          the valid inputs.
	 */
	public static void errorMessage() {
		System.out.println("Sorry! Invalid Input! Please use 'i', 'j', 'k', or 'l'");
	}
	
	/**
	 * @brief The winMessage() method is used to display a message if the user has won the game
	 * @details The method prints out a statement that congratulates the user for reaching the objective
	 *          of the game
	 */
	public static void winMessage() {
		System.out.println("Congrats, you won!!");
	}
	
	/**
	 * @brief The loseMessage() method is used to display a message if the user has lost the game
	 * @details The method prints out a message implying they lost and that they should Try Again, since
	 *          the game automatically restarts
	 */
	public static void loseMessage() {
		System.out.println("Uh oh! Try again!");
	}
	
	/**
	 * @brief The print() method is used to print out the game board onto the console
	 * @details This method correctly formats the game board into the shape of a 4x4 grid, with equal spacing
	 *          in between each adjacent cell. Below the game board, the method labels the score and uses the getScore()
	 *          method from BoardT.java to display the accurately updated score. 
	 * @param board
	 */
	
    public static void print(int[][] board){
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[i].length; j++){
                System.out.print(board[i][j] + "  ");
            }
            System.out.println();
        }
        System.out.println("Score:" + BoardT.getScore());
    }
}
