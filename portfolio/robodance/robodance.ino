#include <Servo.h>
Servo servoRight;
Servo servoLeft;

void turn() {
  servoLeft.writeMicroseconds(1700);   
  delay(10);
  servoRight.writeMicroseconds(1700);
  delay(10);  
}
void reverse() {
  servoRight.writeMicroseconds(1300);
  delay(10);
  servoLeft.writeMicroseconds(1300);   
  delay(10);  
}

void clap() {
    turn();
    delay(490);
    reverse();
    delay(490);
}

void hop() {
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1300);
  servoLeft.writeMicroseconds(1700);
  delay(300);
  servoRight.writeMicroseconds(1500);
  servoLeft.writeMicroseconds(1500);
  
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1300);
  delay(1000);
}

void rightStomp() {
   servoLeft.writeMicroseconds(1700);   
  delay(250);
  servoRight.writeMicroseconds(1700);
  delay(250);  

}

void leftStomp() {
  servoLeft.writeMicroseconds(1300);   
  delay(250);
  servoRight.writeMicroseconds(1300);
  delay(250);  
}

void chacha(){
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1300);
  servoLeft.writeMicroseconds(1700);
  delay(1000);
  servoRight.writeMicroseconds(1500);
  servoLeft.writeMicroseconds(1500);
  
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1300);
  delay(1000);
  
}
void setup() {
  servoLeft.attach(12);
  servoRight.attach(13);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1500);

}


void loop() {
  clap();
  clap();
  clap();
  clap();
  clap();
  clap();
  clap();
  clap();
  clap();
  clap();
  delay(650);
  servoLeft.writeMicroseconds(1300);
  delay(1000);
  servoLeft.writeMicroseconds(1500);
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1300);
  delay(1000);
  servoRight.writeMicroseconds(1500);
  servoLeft.writeMicroseconds(1500);
  delay(1000);
  hop();
  rightStomp();
  rightStomp();
  leftStomp();
  leftStomp();
  servoRight.writeMicroseconds(1500);
  servoLeft.writeMicroseconds(1500);
  delay(1500);
  chacha();
  chacha();
  chacha();
  turn();
  delay(1000);
  servoLeft.writeMicroseconds(1300);
  delay(1000);
  servoRight.writeMicroseconds(1700);
  delay(10);
  servoLeft.writeMicroseconds(1700);   
  delay(1500);
  hop();
  delay(1000);
  rightStomp();
  rightStomp();
  leftStomp();
  leftStomp();
  servoRight.writeMicroseconds(1500);
  servoLeft.writeMicroseconds(1500);
  delay(500);
  chacha();
  chacha();
  turn();
  delay(1000);
   servoLeft.writeMicroseconds(1300);   
  delay(10);
  servoRight.writeMicroseconds(1300);
  delay(10); 
  turn();
  delay(2750);
  
}
