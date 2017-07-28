#import <Servo.h>
int IRpin = 4;
int IRstate = 1;
int IRsensor = 8;
int IRsensorState = 1;

Servo servoRight;
Servo servoLeft;



void setup() {
  // put your setup code here, to run once:

 //wait 1 second before starting
  delay(1000);

  //set up the whiskers to get input
  pinMode(IRpin, INPUT);
  pinMode(IRsensor, INPUT);

  //initialize the serial
  Serial.begin(9600);
  //pins attached to servos
  servoLeft.attach(12);
  servoRight.attach(13);
}

void loop() {
  digitalWrite(IRpin, HIGH);
 

  if (IRsensor == 0) {
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
  }


}
