import java.util.Scanner;

public class hello {
    public static void main(String[] args) {
        try (Scanner myObj = new Scanner(System.in)) {
            String name = myObj.nextLine();
            String secondName = myObj.nextLine();

            HelloWorld();
            HelloWelcome(name, secondName);
            HelloGoodbye(name, secondName);
        }
    }

    public static void HelloWelcome(String name, String secondName) {
        System.out.println("Hello, " + name + " and " + secondName + ".");
    }

    public static void HelloWorld() {
        System.out.println("Hello World!");
    }

    public static void HelloGoodbye(String name, String secondName) {
        System.out.println("Goodbye, " + name + " and " + secondName + ".");
    }
}
    