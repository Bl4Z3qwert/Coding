import java.util.Scanner;

public class CounterApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int count = 0;

        while (true) {
            System.out.print("Press Enter to increase counter...");
            scanner.nextLine();
            count++;
            System.out.println("Counter: " + count);
        }
    }
}
