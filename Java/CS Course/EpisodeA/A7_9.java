package EpisodeA;

import javax.swing.JOptionPane;

public class A7_9 {
    public static void Question7() {
        double x = Double.parseDouble(JOptionPane.showInputDialog("Enter x"));
        double d = Double.parseDouble(JOptionPane.showInputDialog("Enter d"));
        double s = 0;
        double f = x;
        while (f < 100) {
            s += f;
            f += d;
        }
        System.out.println(s); // This is inaccurate, it should be with graphic message
    }

    public static void Question8() {
        int n = Integer.parseInt(JOptionPane.showInputDialog("How many numbers will you be entering?"));
        int num = Integer.parseInt(JOptionPane.showInputDialog("Enter number 1"));
        for (int i = 0; i < n-1; i++) {
            int new_num = Integer.parseInt(JOptionPane.showInputDialog("Enter number " + i+1));
            if (new_num < num) {
                num = new_num;
            }
        }
        JOptionPane.showMessageDialog(null,"The smallest number you entered is: " + num);
    }

    public static void Question9() {
        int Type = Integer.parseInt(
                JOptionPane.showInputDialog(null, "Enter the type of tower")
        );

        if (Type > 3 || Type < 1) {
            JOptionPane.showMessageDialog(null, "Error, Type must be 1, 2 or 3");
            System.exit(0);
        }


        int Height = Integer.parseInt(
                JOptionPane.showInputDialog(
                        null, "Please enter an height for the tower"
                )
        );

        String Character = JOptionPane.showInputDialog(  // Inaccurate, Edith told me it isn't the standard among the course
                null, "Enter the char of the tower"
        );

        char InputChar = Character.charAt(0);
        String output = "";
        int count = 0;

        if (Type == 1) {
            for (int i = 0; i <= Height; i++) {
                for (int j = 0; j < i; j++) {
                    output += InputChar;
                    count++;
                }
                output += "\n";
            }
        } else if (Type == 2) {
            for (int i = Height; i >= 1; i--) {
                for (int j = 0; j < i; j++) {
                    output += InputChar;
                    count++;
                }
                output += "\n";
            }
        } else {
            if (Height%2 == 0) {
                for (int i = Height/2; i > 0; i--) {
                    for (int j = 0; j < i; j++) {
                        output += InputChar;
                        count++;
                    }
                    output += "\n";
                }
                for (int i = 0; i <=Height/2; i++) {
                    for (int j = 0; j < i; j++) {
                        output += InputChar;
                        count++;
                    }
                    output += "\n";
                }
            } else {
                JOptionPane.showMessageDialog(null, "Error, " +
                        "Height must be even for this type of the tower");
                System.exit(0);
            }
        }

        System.out.println(output);
        JOptionPane.showMessageDialog(null, count);
    }
}
