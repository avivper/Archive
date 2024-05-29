package EpisodeA;

import javax.swing.JOptionPane;

public class MashovA {
    public static void Question7() {
        double x = Double.parseDouble(JOptionPane.showInputDialog("x  = ?"));
        double d = Double.parseDouble(JOptionPane.showInputDialog("d  = ?"));

        double sum = 0;
        while (x <= 100) {
            sum += x;
            x += d;
        }
        JOptionPane.showMessageDialog(null, "the answer is " + sum);
    }

    public static void Question8() {
        // Names of the variables aren't readable
        int x = Integer.parseInt(JOptionPane.showInputDialog("How many numbers?"));
        double y = Double.parseDouble(JOptionPane.showInputDialog("Num 1 = ?"));
        for (int i = 1; i < x; i++) {  // Non standard loop
            double z = Double.parseDouble(JOptionPane.showInputDialog("Num " + (i+1)+ " = ?"));
            if (z < y) {
                y = z;
            }
        }
        JOptionPane.showMessageDialog(null, "the smallest number is " + y);
    }

    public static void Question8Tzlil() {
        // The solution is credited to Tzlil
        int min = 99999999;  // There can be bigger number than this value.
        // Solution: Integer.MAX_VALUE (The biggest number assign for the computer)
        int numbers = Integer.parseInt(JOptionPane.showInputDialog("How many numbers?"));
        for (int i = 1; i < numbers; i++) {
            int num = Integer.parseInt(JOptionPane.showInputDialog("Enter number"));
            if (num < min) {
                min = num;
            }
            JOptionPane.showMessageDialog(null, min);
        }
    }
}
