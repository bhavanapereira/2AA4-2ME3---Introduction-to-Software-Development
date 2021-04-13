/**
 * @file Controller.java
 * @author Bhavna Pereira
 * @brief This is the Controller Module
 * @date 12/04/2021
 */


package src;
import src.Display;
import src.Game;
import java.util.Scanner;

/**
 * @brief This class classifies appropriate user input
 * @details This class takes in user input and ensures it is valid. It also runs the game.
 */

public class Controller {
	
	/**
	 * @brief The getUserInput() method takes in and classifies the user input
	 * @details The method prompts the user to specify in which direction they would like to move the cell values. If the input is not 
	 *          equal to "i", "k", "j", or "l", it displays a message informing the user that their input is not valid. Otherwise it passes
	 *          the input to the Game.java module to execute the necessary steps according to the user input
	 */
	
	public static void getUserInput(){
		Display.prompt();
		Scanner input = new Scanner(System.in);
		String direction = input.nextLine();
		if (!direction.equals("i") && !direction.equals("k")  && !direction.equals("j") && !direction.equals("l")) {
			Display.errorMessage();
		}
		else {
			Game.whereToGo(direction);
		}
		
	}
	
	/**
	 * @brief The runGame() method start the Game when called
	 * @details The method displays the introduction message and the instructions for the game. it resets the grid using the Game.java
	 *          module to ensure it is a valid board for the user to begin playing with. This method ensures that at all times, the program
	 *         displays the grid and prompts the user for their input.
	 */
	public static void runGame() {
		Display.introMessage();
		System.out.println();
		Display.instructions();
		Game.resetGame();
		while(true) {
			Display.print(Game.getBoard().getGrid());
			getUserInput();
		}
			
	}

}
