package Main;

public class Board {

    public Object[][] BoardIndex() {
        Object[][] Index = new Object[8][2];
        for (int i = 0; i < 8; i++) {
            Index[i][0] = (char) ('A' + i);
            Index[i][1] = i+1;
        }
        return Index;
    }
}

