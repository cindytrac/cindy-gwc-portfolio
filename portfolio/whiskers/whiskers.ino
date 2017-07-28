#include <Servo.h>

int rightWhiskerPin = 5;
int leftWhiskerPin = 7;
int IRdetector = 8;


int rightWhiskerState = 1;
int leftWhiskerState = 1;
int IRstate = 1;

Servo servoRight;
Servo servoLeft;





void setup() {

  //wait 1 second before starting
  delay(1000);

  //set up the whiskers to get input
  pinMode(rightWhiskerPin, INPUT);
  pinMode(leftWhiskerPin, INPUT);

  //initialize the serial
  Serial.begin(9600);

  //pins attached to servos
  servoLeft.attach(12);
  servoRight.attach(13);

  //servos start not moving
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);
  

}

void loop() {
  rightWhiskerState = digitalRead(rightWhiskerPin);
  leftWhiskerState = digitalRead(leftWhiskerPin);

  if ((rightWhiskerState == 0) and (leftWhiskerState == 0)) {
    servoLeft.writeMicroseconds(1700);
    servoRight.writeMicroseconds(1300);
    delay(1000); 
    servoLeft.writeMicroseconds(1500);
    servoRight.writeMicroseconds(1300);
    delay(750);
  }
  
  else if (leftWhiskerState == 0) {
    servoLeft.writeMicroseconds(1700);
    servoRight.writeMicroseconds(1300); 
    delay(1000);
    servoLeft.writeMicroseconds(1500);
    servoRight.writeMicroseconds(1300);
    delay(750);
  }
  else if (rightWhiskerState == 0) {
    servoLeft.writeMicroseconds(1700);
    servoRight.writeMicroseconds(1300); 
    delay(1000);
    servoLeft.writeMicroseconds(1500);
    servoRight.writeMicroseconds(1300);
    delay(750);
  } 
    }

 /* else if (IRstate == 0) {
    servoLeft.writeMicroseconds(1700);
    delay(10);
    servoLeft.writeMicroseconds(3000);
    delay(10);
    servoLeft.writeMicroseconds(1500); 

    servoRight.writeMicroseconds(1700);
    delay(10);
    servoRight.writeMicroseconds(3000);
    delay(10);
    servoRight.writeMicroseconds(1500); 
  }*/

  else {
    servoLeft.writeMicroseconds(1300);
    servoRight.writeMicroseconds(1700); 
  }
}
