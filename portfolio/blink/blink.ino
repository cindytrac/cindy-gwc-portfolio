int led1 = 13;
int led2 = 12; //RED
int led3 = 11;
int led4 = 10;


void white1() {
  digitalWrite(led1, HIGH);
  delay(200);
  digitalWrite(led1, LOW);
  delay(200);
}

void red() {
  digitalWrite(led2, HIGH);
  delay(50);
  digitalWrite(led2, LOW);
  delay(50);
}

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  
  delay(100);
}

void loop() {
  white1();
  red();
  red();
  delay(50);
  white1();
  red();
  white1();
  digitalWrite(led3, HIGH);
  delay(50);
  digitalWrite(led3, LOW);
  delay(50);
  digitalWrite(led4, HIGH);
  delay(50);
  digitalWrite(led4, LOW);
  delay(50);
  digitalWrite(led1, HIGH);
  digitalWrite(led3, HIGH);
  digitalWrite(led4, HIGH);
  delay(1000);
  digitalWrite(led1, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(led4, LOW);
  white1();
  red();
  red();
  delay(50);
  white1();
  red();
  white1();
  digitalWrite(led3, HIGH);
  delay(50);
  digitalWrite(led3, LOW);
  delay(50);
  digitalWrite(led4, HIGH);
  delay(50);
  digitalWrite(led4, LOW);
  delay(50);
  digitalWrite(led1, HIGH);
  digitalWrite(led3, HIGH);
  digitalWrite(led4, HIGH);
  delay(1000);
  digitalWrite(led1, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(led4, LOW);
  digitalWrite(led1, HIGH);
  delay(500);
  digitalWrite(led3, HIGH);
  delay(500);
  digitalWrite(led4, HIGH);
  delay(500);
}
