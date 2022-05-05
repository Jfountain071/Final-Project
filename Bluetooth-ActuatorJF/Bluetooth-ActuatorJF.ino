#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE    // module to use with the dabble programing
#include <Dabble.h>           // dabble library (the bluetooth module)
int enA = 9;
int in1 = 8;
int in2 = 7;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(250000);      // make sure your Serial Monitor is also set at this baud rate.
  Dabble.begin(9600);      // enter baudrate of your bluetooth.Connect bluetooth on Bluetooth port present on evive
  pinMode(enA, OUTPUT);   // these pins are for the motor driver
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(13, INPUT);   // this is the button detection pin
  pinMode(4, OUTPUT);   // this is the pin for the 
  digitalWrite(in1, LOW); // sets the default state for the motor pins
  digitalWrite(in2, LOW);
}

void loop() {
  Dabble.processInput();             //this function is used to refresh data obtained from the smartphone
  analogWrite(enA, 255);    // the motor will spin at maximum speed
  int switch1 = digitalRead(13);
  if (GamePad.isUpPressed())
  {
    Serial.println("Actuated");   // debug statement to ensure the functionality of the button
    digitalWrite(4, HIGH);
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    delay(1500);        // travels some distance downwards
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    delay(500);       // travels upwards a small distance to relieve pressure on the tube
  }

  if (GamePad.isDownPressed())
  {
    Serial.println("Actuated"); // debug statement to ensure the functionality of the button
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    delay(10000);     // the roller will travel up a long ways to enable the customer to replace the tube
  }

  if (switch1 == 1)
  {
    digitalWrite(4, HIGH);  // this is the pin sending the signal to the RasPi
    Serial.println("Actuated"); // debug statement to ensure the functionality of the button
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    delay(1500);
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    delay(500);
  }
  
  else
  {
    digitalWrite(in1, LOW);   // defualt status is no movement
    digitalWrite(in2, LOW);

  }
}
