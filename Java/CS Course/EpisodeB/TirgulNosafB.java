package EpisodeB;

public class TirgulNosafB {
    public static void main(String[] args) {
        int a = 5;
        int b = 6;
        System.out.println("a = " + a + ", b = " + b);
        exchange(a, b);
        System.out.println("a = " + a + ", b = " + b);
    }

    public static void exchange(int a, int b) {
        int c = a;
        a = b;
        b = c;
    } // Why it doesn't work? Because it doesn't return any value
}
