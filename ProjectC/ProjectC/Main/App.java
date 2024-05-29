package Main;

import javafx.application.Application;
import javafx.stage.Stage;

public class App extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage mainMenu) throws Exception {
        mainMenu.setWidth(800);
        mainMenu.setWidth(600);
        mainMenu.show();
    }

}


/* todo: OPENGL (?), Maybe JSON, LAN (?)
   todo: graphics, design, decide on data structures
   todo: Board.Java, White.Java, Black.Java, Rook,Queen,Pawn,etc.Java

   Board Structure: (I think about implement it like x,y axis in Math)
       A B C D E F G H   <---- Ideas: Array for A,B,C or
       1 2 3 4 5 6 7 8   <---- [][] Array that will contain A,B,C and 1-8
*/

