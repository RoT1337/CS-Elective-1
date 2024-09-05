package expertsystemsactivity;

import java.util.Scanner;
import java.util.ArrayList;

public class rulesandstats {
    static ArrayList<String> strAnswers = new ArrayList<>();
    static ArrayList<String> intlAnswers = new ArrayList<>();
    static ArrayList<String> dexAnswers = new ArrayList<>();
    static ArrayList<String> endAnswers = new ArrayList<>();
    static ArrayList<String> chaAnswers = new ArrayList<>();
    static ArrayList<String> agiAnswers = new ArrayList<>();
    static ArrayList<String> faiAnswers = new ArrayList<>();
    public static void main(String[] args) {
        questions();
        incrementStats();
    }

    public static void questions() {
        Scanner input = new Scanner(System.in);

        String answer;

        System.out.println("Welcome to the RPG Class designator.");
        System.out.println("You will be asked a few quetions and based on your answer, "
        + "your probable RPG class will be given.");
        System.out.println("-------------------------------------------------------------------------");

        // Strength Questions
        System.out.print("Do you consider yourself physically strong, able to handle tasks or challenges that require a lot of strength? (Y/N): ");
        answer = input.nextLine();
        strAnswers.add(answer);
        answer = "";
        System.out.print("Are you the type of person who steps in to protect others when things get tough, even if it means taking the brunt of the impact? (Y/N): ");
        answer = input.nextLine();
        strAnswers.add(answer);
        answer = "";
        System.out.print("When faced with a difficult situation, do you tend to stay calm and grounded, helping others by holding everything together? (Y/N): ");
        answer = input.nextLine();
        strAnswers.add(answer);
        answer = "";

        // Intelligence Questions
        System.out.print("Are you someone who enjoys solving complex problems or puzzles, especially when others are stuck? (Y/N): ");
        answer = input.nextLine();
        intlAnswers.add(answer);
        answer = "";
        System.out.print("Do you often find yourself thinking several steps ahead to anticipate challenges or come up with strategies? (Y/N): ");
        answer = input.nextLine();
        intlAnswers.add(answer);
        answer = "";
        System.out.print("When faced with new information, do you quickly grasp and apply it to find the best solution? (Y/N): ");
        answer = input.nextLine();
        intlAnswers.add(answer);
        answer = "";

        // Dexterity Questions
        System.out.print("Are you good at tasks that require quick reflexes or precise hand-eye coordination, like sports or crafts? (Y/N): ");
        answer = input.nextLine();
        dexAnswers.add(answer);
        answer = "";
        System.out.print("Do you find yourself being agile or nimble, able to move quickly and efficiently when needed? (Y/N): ");
        answer = input.nextLine();
        dexAnswers.add(answer);
        answer = "";
        System.out.print("When presented with a challenge that requires finesse or careful handling, are you confident in your ability to perform accurately? (Y/N): ");
        answer = input.nextLine();
        dexAnswers.add(answer);
        answer = "";

        // Endurance Questions
        System.out.print("Do you have the ability to keep going through physically or mentally exhausting tasks without giving up easily? (Y/N): ");
        answer = input.nextLine();
        endAnswers.add(answer);
        answer = "";
        System.out.print("When faced with long, tough situations, do you tend to push through even when others might quit? (Y/N): ");
        answer = input.nextLine();
        endAnswers.add(answer);
        answer = "";
        System.out.print("Do you recover quickly from strenuous activities or challenges, ready to take on the next task without much rest? (Y/N): ");
        answer = input.nextLine();
        endAnswers.add(answer);
        answer = "";

        // Charisma Questions
        System.out.print("Do you find it easy to connect with others and make a strong impression in social situations? (Y/N): ");
        answer = input.nextLine();
        chaAnswers.add(answer);
        answer = "";
        System.out.print("Are you able to confidently persuade or influence people when presenting your ideas or opinions? (Y/N): ");
        answer = input.nextLine();
        chaAnswers.add(answer);
        answer = "";
        System.out.print("Do people often turn to you for guidance or motivation because of your ability to communicate effectively? (Y/N): ");
        answer = input.nextLine();
        chaAnswers.add(answer);
        answer = "";

        // Agility Questions
        System.out.print("Are you quick on your feet and able to react swiftly in situations that require fast movements? (Y/N): ");
        answer = input.nextLine();
        agiAnswers.add(answer);
        answer = "";
        System.out.print("Do you excel at tasks that require balance and coordination, like dodging obstacles or adjusting to sudden changes? (Y/N): ");
        answer = input.nextLine();
        agiAnswers.add(answer);
        answer = "";
        System.out.print("Can you smoothly adapt your movements to unexpected challenges, staying light and nimble under pressure? (Y/N): ");
        answer = input.nextLine();
        agiAnswers.add(answer);
        answer = "";

        // Faith Questions
        System.out.print("Do you find strength in your beliefs or values, even when facing difficult or uncertain situations? (Y/N): ");
        answer = input.nextLine();
        faiAnswers.add(answer);
        answer = "";
        System.out.print("Are you the type of person who remains hopeful and optimistic, inspiring others to trust in a greater purpose or outcome? (Y/N): ");
        answer = input.nextLine();
        faiAnswers.add(answer);
        answer = "";
        System.out.print("When things get tough, do you rely on your inner convictions or a sense of higher meaning to guide your decisions? (Y/N): ");
        answer = input.nextLine();
        faiAnswers.add(answer);
        answer = "";

        input.close();
    }

    public static void incrementStats() {
        for(String answers: strAnswers) {
            if(answers.toUpperCase() == "Y") {
            }
        }
    }
}
