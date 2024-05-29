#include "calc.h"
#include "update.h"

class Main : public QMainWindow {
    public:
     Main() : QMainWindow() {
        calculator = new QPushButton("Calculator", this);
        update_button = new QPushButton("Update", this);
        setWindowTitle("Currency Calculator"); // Set title for the GUI
        setFixedSize(400, 455); // Non variable sizes of the Window, 300 is the width value, 355 is the height value
        setLayout(new QGridLayout(this)); // Set layout for the GUI
        ui();
     }

     void ui() {
        calculator->setGeometry(90, 300, 90, 50);
        calculator->connect(calculator, &QPushButton::clicked, this, [this] { launch_calculator(); });
        update_button->connect(update_button, &QPushButton::clicked, this, [this] { update_data(); });
     }

    private:
    int argc;
    char** argv;
    QPushButton* update_button;
    QPushButton* calculator;
};

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    Main* main = new Main();
    main->show();
    app.exec();
    return 0;
}