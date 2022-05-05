/*
   Gamepad module provides three different mode namely Digital, JoyStick and Accerleometer.

   You can reduce the size of library compiled by enabling only those modules that you want to
   use. For this first define CUSTOM_SETTINGS followed by defining INCLUDE_modulename.

   Explore more on: https://thestempedia.com/docs/dabble/game-pad-module/
*/
#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE
#include <Dabble.h>           // Dabble library (the bluetooth module)
int enA = 9;
int in1 = 8;
int in2 = 7;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(250000);      // make sure your Serial Monitor is also set at this baud rate.
  Dabble.begin(9600);      //Enter baudrate of your bluetooth.Connect bluetooth on Bluetooth port present on evive.
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(13, INPUT);
  pinMode(4, OUTPUT);

  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
}

void loop() {
  Dabble.processInput();             //this function is used to refresh data obtained from the smartphone
  analogWrite(enA, 255);
  int switch1 = digitalRead(13);
  if (GamePad.isUpPressed())
  {
    Serial.println("Actuated");
    digitalWrite(4, HIGH);
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    delay(1500);
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    delay(500);
  }

  if (GamePad.isDownPressed())
  {
    Serial.println("Actuated");
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    delay(10000);
  }

  if (switch1 == 1)
  {
    digitalWrite(4, HIGH);
    Serial.println("Actuated");
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    delay(1500);
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    delay(500);
  }
  
  else
  {
    digitalWrite(in1, LOW);   // Defualt status is no movement
    digitalWrite(in2, LOW);

  }
}