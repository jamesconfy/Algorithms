import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args) {
        try (Scanner myObj = new Scanner(System.in)) {
            System.out.println("Enter both names");
            String name = myObj.nextLine();
            String secondName = myObj.nextLine();

            HelloWelcome(name, secondName);
        }
    }

    public static void HelloWelcome(String name, String secondName) {
        System.out.println("Hello, " + name + " and " + secondName + ".");
    }
}
