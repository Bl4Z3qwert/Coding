import java.util.Scanner;
import java.util.Random;

public class DiceRoller {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int clicks = 0;

        while (true) {
            System.out.print("Press Enter to roll dice...");
            scanner.nextLine();
            clicks++;

            if (clicks % 2 == 0) {
                int diceValue = random.nextInt(6) + 1;
                System.out.println("Dice rolled: " + diceValue);
            } else {
                System.out.println("Dice paused on odd click.");
            }
        }
    }
}
