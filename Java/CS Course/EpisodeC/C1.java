package EpisodeC;

public class C1 {
    public static void main(String[] args) {
        System.out.println(sHelper(345));
    }
    public static int helper (int n) {
        int m=1;
        n = n/10; // 34
        while (n>0) {
            m = m*10;
            n = n/10; // (1) 3 (2) 0

        }
        return m;
    }

    public static int rHelper(int n) {
        if (n/10 == 0) {
            return 1;
        }
        int m = 0;
        m++;
        n = rHelper (n/10);
        m = n*10;
        return m;
    }

    public static int sHelper(int n) {  // 345
        if (n < 10) {
            return 1;
        }
        return 10 * sHelper(n / 10);
    }

    public static int h(int n) {
        int m = 0;
        if (n/10 == 0) {
            return 1;
        }
        m++;
        n = rHelper(n/10);
        return n*10;
    }

    /*

def rectail(n):
    if n == 0:
        return
    else:
        print(n)
    rectail(n - 1)

     */
    public static int targ (int n) {  // 1: 1948  2: 948  3: 48
        if (n/10 == 0) { // <==
            return n;
        }
        int m = helper (n);  // 1: 1000  2: 100 3: 10 4: 10
        int ans = 10 * targ(n%m) + n/m;  // ==> 84


        // The run of the recursion
        // 1: 10 * targ(1948%1000) + 948 = 10 * targ(948) + 1 = 10 * 849 + 1 = 8491 <== Return ans as 849
        // 2: 10 * targ(948%100) + 9 = 10 * targ(48) + 9 = 10 * 84 + 9 = 849  <== Returns ans as 84
        // 3: 10 * targ(48%10) + 4 = 10 * targ(8) + 4 = 10 * 8 + 4 = 84

        return ans;
    }

}

//  פעולת השיטה Targ לקלט N היא לקחת אותו ולמזער אותו עד שהוא ספרה אחת (ספרת האחדות) לאחר מכן היא מחזירה אותו. היא חוזרת על הפעולה הזאת עד שהקלט הפך את עצמו.
// השיטה הופכת את הספרות במספר כל עוד הקלט שונה ממספר פחות מ10. כאשר המספר קטן מ10 הפונקציה תחזיר את התו