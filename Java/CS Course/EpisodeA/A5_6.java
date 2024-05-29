package EpisodeA;

import javax.swing.JOptionPane;

public class A5_6 {

    // Contains only Question 6
    public static void Question6() {
        int PsychometricGrade = Integer.parseInt(
                JOptionPane.showInputDialog("What is your psychometry?")
        );

        if (PsychometricGrade < 400) {
            JOptionPane.showMessageDialog(null,
                    "you should greatly imrpove your psychometry");
        } else {
            int BagrutGrade = Integer.parseInt(
                    JOptionPane.showInputDialog("What is your Bagrut's Grade?")
            );

            if (PsychometricGrade < 700) {
                if (BagrutGrade < 97) {
                    JOptionPane.showMessageDialog(null, "You should improve psychometry");
                } else {
                    JOptionPane.showMessageDialog(null, "You should go to the mechina");
                }
            } else {
                if (BagrutGrade > 90) {
                    JOptionPane.showMessageDialog(null, "You got accepted!");
                } else {
                    JOptionPane.showMessageDialog(null, "go to the mechina");
                }
            }
        }
    }
}
