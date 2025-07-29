import java.util.Random;

public class RandomColors {
    public static void main(String[] args) {
        String[] colors = {"Red", "Green", "Blue", "Yellow", "Purple"};
        Random rand = new Random();

        String pickedColor = colors[rand.nextInt(colors.length)];
        System.out.println("Screen color changed to: " + pickedColor);
    }
}
