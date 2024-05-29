package EpisodeB;

import javax.swing.JOptionPane;

public class B1 {

    public static void main (String[] args) {
        int numberOfGivenExercises = 0;
        int numberOfCorrectAnswers = 0;
        int level = getLevel();
        char operation = getOperation(level);
        boolean again;
        do {
            boolean correct = play (level, operation);
            if (correct)
                JOptionPane.showMessageDialog(null, "Correct!!!");
            numberOfCorrectAnswers++;
            numberOfGivenExercises ++;
            again = wantsAgain();
        } while (again);
        showResults(numberOfGivenExercises, numberOfCorrectAnswers);
    }
    public static int getLevel(){
        int chooseLevel;
        do {
            chooseLevel = Integer.parseInt(JOptionPane.showInputDialog(null, "Choose a level"));
        } while (chooseLevel > 3 || chooseLevel < 1);
        return chooseLevel;
    }
    public static char getOperation(int level) {
        char operation;
        if (level == 1 || level == 2) {
            operation = JOptionPane.showInputDialog(null, "Choose an operation (+ or -)").charAt(0);
            while (operation != '+' && operation != '-') {
                JOptionPane.showMessageDialog(null, "You can choose only + or -");
                operation = JOptionPane.showInputDialog(null, "Choose an operation (+ or -)").charAt(0);
            }
        } else {
            operation = JOptionPane.showInputDialog(null, "Choose an operation (+, - or *)").charAt(0);
            while (operation != '+' && operation != '-' && operation != '*') {
                JOptionPane.showMessageDialog(null, "You can choose only +, - or *");
                operation = JOptionPane.showInputDialog(null, "Choose an operation (+, - or *)").charAt(0);
            }
        }
        return operation;
    }
    public static boolean play(int level, char operation) {
        int max;
        int min = 1;
        int realAnswer;

        if (level==1) {
            max = 20;
        } else if (level==2) {
            max = 50;
        } else {
            max = 101;
            min = 20;
        }
        int numberOne = (int) (Math.random() * (max - min) + min);
        int numberTwo = (int) (Math.random() * (max - min) + min);
        int answer= Integer.parseInt(JOptionPane.showInputDialog(null,"solve:" + numberOne +operation+ numberTwo));
        if (operation=='+') {
            realAnswer = numberOne+numberTwo;

        } else if (operation=='-') {
            realAnswer = numberOne-numberTwo;
        } else {
            realAnswer = numberOne*numberTwo;
        }
        return (answer==realAnswer);
    }//end of play
    // do you want to practice more?
    public static boolean wantsAgain(){
        char play = JOptionPane.showInputDialog(null,"Do you want to play again? choose Y or N").charAt(0);
        return play=='y'|| play=='Y';
    }
    //summarize of the study
    public static void showResults(int givenEx, int rightEx){
        JOptionPane.showMessageDialog(null,"You were given "+givenEx+" exercises");
        JOptionPane.showMessageDialog(null,"You solved "+rightEx+" exercises");
        JOptionPane.showMessageDialog(null,100*rightEx/givenEx+" Precent of the exercises were solved right");
    }
}

