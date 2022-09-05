import java.util.Scanner;

public class HelloGoodbye {
    public static void main(String[] args) {
        try (Scanner myObj = new Scanner(System.in)) {
            System.out.println("Enter both names");
            String name = myObj.nextLine();
            String secondName = myObj.nextLine();

            goodbye(name, secondName);
        }
    }

    public static void goodbye(String name, String secondName) {
        System.out.println("Goodbye, " + name + " and " + secondName + ".");
    }
}