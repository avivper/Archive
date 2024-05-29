package EpisodeA;

import javax.swing.JOptionPane;

public class A1_4 {
    public static void question_1() {
        String future = JOptionPane.showInputDialog(null, "I can tell your Future!" +
                "\nHow many years ahead?");
        int years = Integer.parseInt(future);

        String years_old = JOptionPane.showInputDialog(null, "How old are you?");
        int age = Integer.parseInt(years_old);

        JOptionPane.showMessageDialog(null, "Your future:\n" +
                "In 7 years you'll be 32 years old");
    }

    public static void question_2() {
        double sum = 0;
        String name = JOptionPane.showInputDialog(null, "What's your name?");
        int numGrades = 4;

        for (int i = 0; i < numGrades; i++) {
            String rawInput = JOptionPane.showInputDialog(null, "Hello " + name +
                    " Enter the " + (i+1) + " of " +
                    numGrades + " grades to calculate the average:\n");
            double grade = Double.parseDouble(rawInput);
            sum += grade;
        }

        double average = sum/4;
        JOptionPane.showMessageDialog(null, "The Average is: " + average);
    }


    public static void question_3() {
        // f(0) = x
        // f(1) = x+d
        // f(n) = x+n(d)

        String element_one = JOptionPane.showInputDialog(null, "Enter the value of x");
        double x = Double.parseDouble(element_one);

        String element_two = JOptionPane.showInputDialog(null, "Enter the value of d");
        double d = Double.parseDouble(element_two);

        double n1 = x;
        double n2 = n1 + d;
        double n3 = n2+d;

        JOptionPane.showMessageDialog(null, n1 + ", " + n2 + ", " + n3 + ", ");

    }

    public static void question_4() {
        String word = JOptionPane.showInputDialog(null, "Word! please?");
        JOptionPane.showMessageDialog(null,
                "Gimme " + word.charAt(0) + " !"
                        + "\nGimme " + word.charAt(1) + " !"
                        + "\nGimme " + word.charAt(2) + " !"
                        + "\nGimme " + word.charAt(3) + " !"
                        + "\nGimme " + word.charAt(0) + " "
                        + word.charAt(1) + " "
                        + word.charAt(2) + " "
                        + word.charAt(3) + " !"
        );
    }

}
