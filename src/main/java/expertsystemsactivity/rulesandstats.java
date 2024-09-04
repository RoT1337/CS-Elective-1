package expertsystemsactivity;

import java.util.Scanner;
import java.util.ArrayList;

public class rulesandstats {
    static ArrayList<String> answers = new ArrayList<>();
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String answer;

        System.out.println("Welcome to the RPG Class designator.");
        System.out.println("You will be asked a few quetions and based on your answer, "
        + "your probable RPG class will be given.");
        System.out.println("-------------------------------------------------------------------------");
        System.out.println("Testingsz");
        System.out.println("-------------------------------------------------------------------------");
        System.out.print("Do you lift? (Y/N): ");
        answer = input.nextLine();
        answers.add(answer);
        answer = "";
        System.out.print("Do you read? (Y/N): ");
        answer = input.nextLine();
        answers.add(answer);
        answer = "";
        System.out.print("Do you run? (Y/N): ");
        answer = input.nextLine();
        answers.add(answer);
        answer = "";
        System.out.print("When pushed, do you feel like you give up easily? (Y/N): ");
        answer = input.nextLine();
        answers.add(answer);
        answer = "";
        System.out.print("Do people laugh at your jokes? (Y/N): ");
        answer = input.nextLine();
        answers.add(answer);
        answer = "";
        System.out.print("Do you climb? (Y/N): ");
        answer = input.nextLine();
        answers.add(answer);
        answer = "";
        System.out.print("Do you pray? (Y/N): ");
        answer = input.nextLine();
        answers.add(answer);
        answer = "";

        System.out.println("-------------------------------------------------------------------------");
        for (String ans: answers) {
            System.out.print(ans + ", ");
        }
    }
}
