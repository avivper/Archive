#include "calc.h"

class Calculator : public QMainWindow {
    public:
      Calculator() : QMainWindow() {
        frame = new QLabel(this); // Will show the math exercise and result
        pervious_number = new QLabel(this);

        // Creating Buttons objects
        clear_button = new QPushButton("C", this);
        dot_button = new QPushButton(".", this);
        convert_button = new QPushButton("Convert", this);
        reset_button = new QPushButton("Reset", this);

        // Operators
        divine_button = new QPushButton("÷", this);
        multiply_button = new QPushButton("×", this);
        plus_button = new QPushButton("+", this);
        minus_button = new QPushButton("-", this);

        // Numbers
        button_0 = new QPushButton("0", this);
        button_1 = new QPushButton("1", this);
        button_2 = new QPushButton("2", this);
        button_3 = new QPushButton("3", this);
        button_4 = new QPushButton("4", this);
        button_5 = new QPushButton("5", this);
        button_6 = new QPushButton("6", this);
        button_7 = new QPushButton("7", this);
        button_8 = new QPushButton("8", this);
        button_9 = new QPushButton("9", this);

        button_list = { // List of Buttons
            plus_button,
            minus_button,
            multiply_button,
            divine_button,
            button_0,
            button_1,
            button_2,
            button_3,
            button_4,
            button_5,
            button_6,
            button_7,
            button_8,
            button_9,
            dot_button,
            clear_button,
            convert_button,
            reset_button
        };

        value_list = { // List of values
            "+", "-", "×", "÷", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."
        };
        

        ui();
        setWindowTitle("Calculator"); // Set title for the GUI
        setFixedSize(300, 355); // Non variable sizes of the Window, 300 is the width value, 355 is the height value
        setLayout(new QGridLayout(this)); // Set layout for the GUI
      }

      static void circle_style(QPushButton* button) {
        button->setFixedSize(50, 50); // Non variable size of the Button
        button->setFont(QFont("Arial", 10));
        button->setStyleSheet( // Making the button take the shape of circular square
            "QPushButton {"
            "color: black;"
            "font-weight: bold;"
            "font-size: 16px;"
            "padding: 12px 16px;"
            "border-radius: 15px;"
            "background-color: #D3D3D3;"
            "border: 2px solid black;"
            "}"
            "QPushButton:hover {"
            "background-color: #A9A9A9"
            "}"
            "QPushButton:pressed {"
            "background-color: #c6c6c6;"
            "color: #222222;"
            "}"
        );
      }

      std::vector<std::string> read_string(const std::string& math_exercise, char delimiter = ' ') {
        // delimiter checks if there any spaces in the large string, math_exercise is the input from the user
        std::vector<std::string> exercise_values; // List that will contain data from the user
        std::stringstream ss(math_exercise); // This object reads the string letter by letter
        std::string value; // numbers value from the user
        while(getline(ss, value, delimiter)) {
          exercise_values.push_back(value);
        }
        return exercise_values;
      }

      void show_result(float result) {
        QString result_string = QString::number(result);
        frame->setText(result_string);
        pervious_number->clear();
      }

      float calculate() {
          QString value1 = pervious_number->text(); // Gets the fist number from the user
          QString value2 = frame->text(); // Gets the second number from the user
          std::string value1_str = value1.toStdString(); // Convert type from QString to std::string
          std::string value2_str = value2.toStdString(); // Convert type from QString to std::string
          std::vector<std::string> values = read_string(value1_str, ' '); // The list with the data from the user

          if (value1 == "" || value2 == "") {  // If the screen is empty, it will do nothing
              return 0;
          }
          else {
              float num1 = std::stof(values[0]);
              float num2 = std::stof(value2_str);
              float result;
              if (values[1] == value_list[0]) { // Plus
                  result = num1 + num2;
                  show_result(result);
                  return result;
              }
              else if (values[1] == value_list[1]) { // Minus
                  result = num1 - num2;
                  show_result(result);
                  return result;
              }
              else if (values[1] == value_list[2]) { // Multiply
                  result = num1 * num2;
                  show_result(result);
                  return result;
              }
              else if (values[1] == value_list[3]) { // Divine
                  if (num1 == 0 || num2 == 0) {
                      pervious_number->clear();
                      frame->setText("Error: cannot divine by zero");
                      return 0;
                  }
                  else {
                      result = num1 / num2;
                      show_result(result);
                      return result;
                  }
              }
          }
        return 0;
      }

      void input_number(std::string value) {        
        // Error handling
        QString calc_frame = frame->text();
        std::string num = calc_frame.toStdString();
        std::stringstream ss(num);
        while(getline(ss, num, ' ')) { // If there any error, clicking on the number will reset the error
          if(num == "Error" || num == "Error:") {
            reset();
          } 
        }
        QString number_value = QString::fromStdString(value);
        frame->setText(frame->text() + number_value);
      }

      void operate(std::string op) {
          QString calc_frame = frame->text(); // Gets the data from the user
          QString pervious_num = pervious_number->text(); // Gets the data from pervious_number
          QString op_value = QString::fromStdString(op); // Convert type from QString to std::string
          std::string num = calc_frame.toStdString(); // Convert type from QString to std::string
          std::string values = pervious_num.toStdString(); // Convert type from QString to std::string
          std::stringstream ss(num); // This object reads the string letter by letter

          // Error Handling
          while (getline(ss, num, ' ')) {  // If there any error, clicking on any operator will reset the error
              if (num == "Error" || num == "Error:") { 
                  reset();
              }
              else if (values == "") { // Add new number to the left side of the screen but if the left side is cleared
                  pervious_number->setText(frame->text() + " " + op_value + " ");
                  clear_screen(); // Clearing the screen and expecting a new number from the user
              } 
              else { // If there existing number but I want to switch operator, this block will switch the operator
                  int last_op_pos = pervious_num.lastIndexOf(QRegExp("[+\\-×÷]"));
                  if (last_op_pos == -1) { // If no operator found in the string experssion
                      pervious_number->setText(frame->text() + " " + op_value + " ");
                      clear_screen();
                  }
                  else { // Replacing the operator
                      pervious_num.replace(last_op_pos, 1, op_value);
                      pervious_number->setText(pervious_num);
                  }
              }
          }
      }

      void reset() { // Reseting everything
          frame->clear();
          pervious_number->clear();
      }

      void clear_screen() { // Clearing only the frame
          frame->clear(); 
      }

      void ui() {
        // Drawing the gui
        for (int i = 0; i < button_list.size(); i++) {
            button_list[i]->setGeometry(positions[i][0], positions[i][1], positions[i][2], positions[i][3]); // Placing buttons on gui

            if (button_list[i] != convert_button && button_list[i] != reset_button) {
                circle_style(button_list[i]); // Setting style for all buttons execpt convert_button and reset_button
                if(button_list[i] != clear_button) {
                  if (i <= 3) { // It is 3 because the value_list starting from operators (0 to 3)
                    button_list[i]->connect(button_list[i], &QPushButton::clicked, this, [this, i] { // Setting functions to all opeators buttons
                      operate(value_list[i]);
                    });
                  } else {
                    button_list[i]->connect(button_list[i], &QPushButton::clicked, this, [this, i] { // Setting function that will insert number to the screen
                      input_number(value_list[i]);
                    });
                  }
                } else if (button_list[i] == clear_button) { // Building the rest of the GUI
                    //Handling the frame label
                    frame->setGeometry(5, 5, 285, 50);
                    frame->setWordWrap(true);
                    frame->setStyleSheet( // Making the frame using the shape of rectangle
                        "QLabel {"
                        "border: 2px solid black;"
                        "background: white;"
                        "}"
                    );
                    frame->setAlignment(Qt::AlignRight);
                    frame->setFont(QFont("Arial", 15));
                    frame->setText(""); // Assiging string value to frame, didn't want it to be null. Gave me a headache while it was null

                    //Handling the number label
                    pervious_number->setGeometry(8, 5, 285, 50);
                    pervious_number->setWordWrap(true);
                    pervious_number->setAlignment(Qt::AlignLeft);
                    pervious_number->setStyleSheet("color: gray;");
                    pervious_number->setFont(QFont("Arial", 10, QFont::Bold));
                    pervious_number->setText(""); // Same here, like in frame->setText("")'s comment

                    // Handling convert button
                    convert_button->setFont(QFont("Arial", 8));
                    convert_button->connect(convert_button, &QPushButton::clicked, this, [this] {
                      calculate();
                    });

                    // Handling clear button
                    clear_button->connect(clear_button, &QPushButton::clicked, this, [this] {
                      clear_screen();
                    });

                    // Handling reset button
                    reset_button->connect(reset_button, &QPushButton::clicked, this, [this] {
                        reset();
                    });
                }
            }
        }
    }
    private:
      QLabel* frame;
      QLabel* pervious_number;
      QPushButton* reset_button;
      QPushButton* clear_button;
      QPushButton* dot_button;
      QPushButton* convert_button;
      QPushButton* divine_button;
      QPushButton* multiply_button;
      QPushButton* plus_button;
      QPushButton* minus_button;
      QPushButton *button_0;
      QPushButton *button_1;
      QPushButton *button_2;
      QPushButton *button_3;
      QPushButton *button_4;
      QPushButton *button_5;
      QPushButton *button_6;
      QPushButton *button_7;
      QPushButton *button_8;
      QPushButton *button_9;
      std::vector<QPushButton*> button_list;
      std::vector<std::string> value_list;

      int positions[18][4] = {
         {220, 240, 50, 50}, // plus_button
         {220, 180, 50, 50}, // minus_button
         {220, 120, 50, 50}, // multiply_button
         {220, 60, 50, 50}, // divine_button
         {40, 240, 50, 50}, // button_0
         {40, 180, 50, 50}, // button_1
         {100, 180, 50, 50}, // button_2
         {160, 180, 50, 50}, // button_3
         {40, 120, 50, 50}, // button_4
         {100, 120, 50, 50},  // button_5
         {160, 120, 50, 50},  // button_6
         {40, 60, 50, 50},  // button_7
         {100, 60, 50, 50},  // button_8
         {160, 60, 50, 50},  // button_9
         {100, 240, 50, 50}, // dot_button 
         {160, 240, 50, 50}, // clear_button 
         {50, 300, 90, 50}, // convert_button
         {180, 300, 90, 50} // reset_button
      };
};

void launch_calculator() {  // Launching the calculator upon execution
  Calculator* calc = new Calculator();
  calc->show();
}
