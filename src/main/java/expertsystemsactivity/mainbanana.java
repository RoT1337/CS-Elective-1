package expertsystemsactivity;

import java.util.Scanner;
import java.util.ArrayList;

public class mainbanana {
    static ArrayList<String> strAnswers = new ArrayList<>();
    static ArrayList<String> intlAnswers = new ArrayList<>();
    static ArrayList<String> dexAnswers = new ArrayList<>();
    static ArrayList<String> endAnswers = new ArrayList<>();
    static ArrayList<String> chaAnswers = new ArrayList<>();
    static ArrayList<String> agiAnswers = new ArrayList<>();
    static ArrayList<String> faiAnswers = new ArrayList<>();
    private rulesandstats stats = new rulesandstats();

    public static void main(String[] args) {
        mainbanana main = new mainbanana();
        questions();
        main.incrementStats();
        main.printResults();
    }

    public static void questions() {
        Scanner input = new Scanner(System.in);

        String[] strQuestions = {
            "Do you consider yourself physically strong, able to handle tasks or challenges that require a lot of strength? (Y/N): ",
            "Are you the type of person who steps in to protect others when things get tough, even if it means taking the brunt of the impact? (Y/N): ",
            "When faced with a difficult situation, do you tend to stay calm and grounded, helping others by holding everything together? (Y/N): "
        };

        String[] intQuestions = {
            "Are you someone who enjoys solving complex problems or puzzles, especially when others are stuck? (Y/N): ",
            "Do you often find yourself thinking several steps ahead to anticipate challenges or come up with strategies? (Y/N): ",
            "When faced with new information, do you quickly grasp and apply it to find the best solution? (Y/N): "
        };

        String[] dexQuestions = {
            "Are you good at tasks that require quick reflexes or precise hand-eye coordination, like sports or crafts? (Y/N): ",
            "Do you find yourself being agile or nimble, able to move quickly and efficiently when needed? (Y/N): ",
            "When presented with a challenge that requires finesse or careful handling, are you confident in your ability to perform accurately? (Y/N): "
        };

        String[] endQuestions = {
            "Do you have the ability to keep going through physically or mentally exhausting tasks without giving up easily? (Y/N): ",
            "When faced with long, tough situations, do you tend to push through even when others might quit? (Y/N): ",
            "Do you recover quickly from strenuous activities or challenges, ready to take on the next task without much rest? (Y/N): "
        };

        String[] chaQuestions = {
            "Do you find it easy to connect with others and make a strong impression in social situations? (Y/N): ",
            "Are you able to confidently persuade or influence people when presenting your ideas or opinions? (Y/N): ",
            "Do people often turn to you for guidance or motivation because of your ability to communicate effectively? (Y/N): "
        };

        String[] agiQuestions = {
            "Are you quick on your feet and able to react swiftly in situations that require fast movements? (Y/N): ",
            "Do you excel at tasks that require balance and coordination, like dodging obstacles or adjusting to sudden changes? (Y/N): ",
            "Can you smoothly adapt your movements to unexpected challenges, staying light and nimble under pressure? (Y/N): "
        };

        String[] faiQuestions = {
            "Do you find strength in your beliefs or values, even when facing difficult or uncertain situations? (Y/N): ",
            "Are you the type of person who remains hopeful and optimistic, inspiring others to trust in a greater purpose or outcome? (Y/N): ",
            "When things get tough, do you rely on your inner convictions or a sense of higher meaning to guide your decisions? (Y/N): "
        };

        System.out.println("Welcome to the RPG Class designator.");
        System.out.println("You will be asked a few questions and based on your answer, "
        + "your probable RPG class will be given.");
        System.out.println("-------------------------------------------------------------------------");

        try {
            askQuestions(input, strQuestions, strAnswers);
            askQuestions(input, intQuestions, intlAnswers);
            askQuestions(input, dexQuestions, dexAnswers);
            askQuestions(input, endQuestions, endAnswers);
            askQuestions(input, chaQuestions, chaAnswers);
            askQuestions(input, agiQuestions, agiAnswers);
            askQuestions(input, faiQuestions, faiAnswers);
        } catch(Exception e) {
            System.out.println(e);
        }

        input.close();
    }

    public static void askQuestions(Scanner input, String[] questions, ArrayList<String> answers) {
        for (String question : questions) {
            String answer;
            do {
                System.out.print(question);
                answer = input.nextLine();
                if (!isValidAnswer(answer)) {
                    System.out.println("Invalid input. Please enter a letter (Y/N).");
                }
            } while (!isValidAnswer(answer));
            answers.add(answer);
        }
        System.out.println();
    }

    public static boolean isValidAnswer(String answer) {
        return answer.equalsIgnoreCase("Y") || answer.equalsIgnoreCase("N");
    }

    public void incrementStats() {
        for(String answers: strAnswers) {
            if(answers.equalsIgnoreCase("Y")) {
                stats.setStr(stats.getStr() + 20);
            }
        }

        for(String answers: intlAnswers) {
            if(answers.equalsIgnoreCase("Y")) {
                stats.setIntl(stats.getIntl() + 20);
            }
        }

        for(String answers: dexAnswers) {
            if(answers.equalsIgnoreCase("Y")) {
                stats.setDex(stats.getDex() + 20);
            }
        }

        for(String answers: endAnswers) {
            if(answers.equalsIgnoreCase("Y")) {
                stats.setEnd(stats.getEnd() + 20);
            }
        }

        for(String answers: chaAnswers) {
            if(answers.equalsIgnoreCase("Y")) {
                stats.setCha(stats.getCha() + 20);
            }
        }

        for(String answers: agiAnswers) {
            if(answers.equalsIgnoreCase("Y")) {
                stats.setAgi(stats.getAgi() + 20);
            }
        }

        for(String answers: faiAnswers) {
            if(answers.equalsIgnoreCase("Y")) {
                stats.setFai(stats.getFai() + 20);
            }
        }
    }

    private void printResults() {
        System.out.println("Based on your answers, the following class/es is/are suitable for you: ");
        if(stats.getStr() >= 40 && stats.getEnd() >= 40 || stats.getCha() >= 40) {
            System.out.println("TANK");
        } 
        if (stats.getIntl() >= 40 && stats.getEnd() >= 40) {
            System.out.println("MAGE");
        } 
        if (stats.getDex() >= 40 && stats.getAgi() >= 40 || stats.getCha() >= 40) {
            System.out.println("ROGUE");
        } 
        if (stats.getFai() >= 40 && stats.getEnd() >= 40 || stats.getIntl() >= 40) {
            System.out.println("HEALER");
        }
    }
}