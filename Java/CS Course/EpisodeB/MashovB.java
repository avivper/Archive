package EpisodeB;

/*
This file is containing the comments + methods from the Mashov to Episode B
 */

public class MashovB {
    public static void main(String[] args) {
        MashovB1();
    }

    public static void MashovB1() {
        System.out.println("MashovB1");
    }

    // Mashov B2

    // Isn't part from the mashov
    public static int countCharInString(char c, String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == c) {
                count++;
            }
        }
        return count;
    }

    // Question 3

    // This version is from start to end in loop
    public static int lastIndexofCharInString(char c, String s) {
        int index = -1;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == c) {
                index = i;
            }
        }
        return index;
    }
    // Another solution for 2, this version is from last to the start
    public static int lastIndexofCharInString2(char c, String s) {
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == c) {
                return i;
            }
        }
        return -1;
    }

    // Question 4


    // לכל תו במחרוזת הראשונה, נעבור על כל התווים במחרוזת השנייה
    public static boolean isThereCommonChar (String s1, String s2) {
        for (int i = 0; i < s1.length(); i++) {
            for (int j = 0; j < s2.length(); j++) {
                if (s1.charAt(i) == s2.charAt(j)) {
                    return true;
                }
            }
        }
        return false;
    }

    // לכל תו במחרוזת הראשונה, נחפש אותו במחרוזת השניה בעזרת שיטת העזר
    public static boolean isThereCommonChar2(String s1, String s2) {
        for (int i = 0; i < s1.length(); i++) {
            if (s2.indexOf(s1.charAt(i)) != -1) {
                return true;
            }
        }
        return false;
    }


    // Question 5

    // בנית המחרוזת החדשה תו-תו
    public static String eliminateCharFromString(char c, String s) {
        /*
       הבדיקה כאן מה יקרה בלעדיה? הכל יהיה בסדר גם בלעדיה - ולכן היא מיותרת
       יש מקרים שנראים לנו "מיוחדים" ואנחנו ממהרים לטפל בהם בנפרד, אבל בעצם האלגוריתם ה"רגיל" מטפל בהם היטב.
         */

        // vvv הבדיקה הזאת vvv
        if (countCharInString(c, s) == 0) {
            return s;
        }
        String ans = "";

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != c) {
                ans += s.charAt(i);
            }
        }
        return ans;
    }

    // הסרת התו מהמחרוזת הנתונה עצמה
    public static String eliminateCharFromString2(char c, String s) {
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == c) {
                s = s.substring(0, i) + s.substring(i + 1);
                // i--; --> נוריד מאיי אחד כדי לבקר בתו הבא
            }
        }
        return s;
    }
    // השיטה מעל מתעלמת במקרה ואנחנו עוברים על אותו תו פעמיים ברצף
    // כמו למשל חררן, במידה והשיטה תקלוט את התו 'ר'
    // כדי לטפל בזה, נוסיף i--

    // Question 6
    public static String eliminateCharsFromString(String letters, String s) {
        // This method is credited to Liron/Osher/Awoke
        String cenzorizedString = s;
        for (int i = 0; i < letters.length(); i++) {
            cenzorizedString = eliminateCharFromString(letters.charAt(i), cenzorizedString);
        }
        return cenzorizedString;
    }

    public static String eliminateCharsFromString2(String letters, String s) {
        String ans = "";
        for (int i = 0; i < letters.length(); i++) {
            int counter = 0;
            for (int j = 0; j < letters.length(); j++) {
                if (letters.charAt(i) == letters.charAt(j)) {
                    counter++;
                }
            }
            if (counter == 0) {
                ans += s.charAt(i);
            }
        }
        return ans;
    }

    // Improved version to 2

    public static String eliminateCharsFromString3(String letters, String s) {
        String ans = "";
        for (int i = 0; i < letters.length(); i++) {
            boolean found = false; // Instead of counter
            for (int j = 0; j < letters.length(); j++) {
                if (letters.charAt(i) == letters.charAt(j)) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                ans += s.charAt(i);
            }
        }
        return ans;
    }

    // Question 8
    public static String reverseWordsInString(String s) {
        String ans = "";
        int times = countCharInString(' ', s);
        for (int i = 0; i < times; i++) {
            int index = lastIndexofCharInString(' ', s);
            ans += s.substring(index, index + 1) + " ";
            s = s.substring(0, index);
        }
        // כעת מכיוון שמספר הסיבובים הוא כמספר הרווחים, אבל מספר הרווחים קטן באחד
        // ממספר המילים, נשארה המילה הראשונה שלא לקחנו וצריך להוסיף בנפרד
        ans += s;
        return ans;
    }

    public static String reverseWordsInString2(String s) {
        String ans = "";
        String currentWord = "";
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                currentWord += s.charAt(i);
            } else {
                ans = currentWord + " " + ans;
                currentWord = "";
            }
        }
        ans = currentWord + " " + ans;  // המילה האחרונה שליקטנו שאין אחריה רווח
        return ans;
    }

    // Question 9
    public static int indexOfStringInString(String stringToFind, String s) {
        int lengthToFind = stringToFind.length();
        for (int startIndex = 0; startIndex + lengthToFind <= s.length(); startIndex++) {
            boolean isSame = true;
            for (int i = 0; i < lengthToFind; i++) {
                if (s.charAt(startIndex + i) != stringToFind.charAt(i)) {
                    isSame = false;
                    break;
                }
            }
            if (isSame) {
                return startIndex;
            }
        }
        return -1;
    }

    // גרסת ההשוואה עם equals
    public static int indexOfStringInString2(String stringToFind, String s) {
        int lengthToFind = stringToFind.length();
        for (int startIndex = 0; startIndex + lengthToFind <= s.length(); startIndex++) {
            if (s.substring(startIndex, startIndex + lengthToFind).equals(stringToFind)) {
                return startIndex;
            }
        }
        return -1;
    }

    // Question 10
    public static String eliminateStringFromString(String stringToCut, String s) {
        // This method is credited to Daniel and Tohar
        int index = indexOfStringInString(stringToCut, s);
        while (index != -1) {
            s = s.substring(0, index) + s.substring(index + stringToCut.length());
            index = indexOfStringInString(stringToCut, s);
        }
        return s;
    }
}
