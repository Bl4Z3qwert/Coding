import java.util.ArrayList;
import java.util.Scanner;

public class ShoppingList {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        String item;

        while (true) {
            System.out.print("Add item (type 'done' to finish): ");
            item = scanner.nextLine();
            if (item.equalsIgnoreCase("done")) break;
            list.add(item);
        }

        System.out.println("Your Shopping List:");
        for (int i = 0; i < list.size(); i++) {
            System.out.println((i + 1) + ". " + list.get(i));
        }
    }
}
