import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class CalendarClock {
    public static void main(String[] args) {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter dateFormat = DateTimeFormatter.ofPattern("EEEE, MMM dd, yyyy");
        DateTimeFormatter timeFormat = DateTimeFormatter.ofPattern("hh:mm:ss a");

        System.out.println("Date: " + now.format(dateFormat));
        System.out.println("Time: " + now.format(timeFormat));
    }
}
