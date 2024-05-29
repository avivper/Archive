package EpisodeA;

import javax.swing.*;

public class TirgulNosafA {
    public static void main(String[] args) {
        Question2();
    }

    public static void Question1() {
        int sum = 5;
        int a = Integer.parseInt(JOptionPane.showInputDialog("Enter a number"));
        int b;
        boolean c = true;
        for (int i = 1; i < sum; i++) { // B: 5 times it will run from 1 to 5
            b = Integer.parseInt(JOptionPane.showInputDialog("Enter a number"));  // C: 2 times
            if (a > b) {
                c = false;  // D: a = 5, b = 2, c will be false
                a = b;
            }
        }
        if (c) { // E: b = 5, a = 3, c will be true
            JOptionPane.showMessageDialog(null, "OK");
        } else {
            JOptionPane.showMessageDialog(null, "NOT OK");
        }   // F: the software will ask from the user 2 numbers and it will
        // }   // output a message "OK" and "NOT OK" based on the user's input
    }
    public static void Question2() {
        int inputNumber = Integer.parseInt(JOptionPane.showInputDialog(null, "Enter a number"));
        int counter = 0;
        for (int i = 0; i < inputNumber; i++) {
            inputNumber/=2;
            counter++;
            if (inputNumber <= 1) {
                JOptionPane.showMessageDialog(null, counter);
                return;
            }
        }
    }
}