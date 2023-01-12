// Define stepper motor connections:
#define dirPin1 2
#define stepPin1 3

#define dirPin2 6
#define stepPin2 7

// Define limit switches
#define xLimit 9
#define yLimit 10


void setup() {
  pinMode(stepPin1, OUTPUT);
  pinMode(dirPin1, OUTPUT);

  pinMode(stepPin2, OUTPUT);
  pinMode(dirPin2, OUTPUT);
}

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
void loop() {
  // put your main code here, to run repeatedly:

}
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

// ~~~~~ Converts cm to motor steps ~~~~~
int distToStep(float cm) {
  return int(cm*0.009);
}

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// ~~~~~ Move Y ~~~~~
void moveY(float currPos, float newPos) {
  float vector = currPos - newPos; //Calculates Y vector

  //Specifies up or down
  int direction = ( abs(vector) - vector) / abs(2*vector);
  digitalWrite(dirPin1, direction);
  digitalWrite(dirPin2, ~direction);

  //Move the device
  int numSteps = distToStep(vector);
  for(int i=0;i<numSteps;i++) {
    digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin2, HIGH);
    delayMicroseconds(50);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    delayMicroseconds(50);
  }
}

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// ~~~~~ Move X ~~~~~
void moveX(float currPos, float newPos) {
  float vector = currPos - newPos; //Calculates Y vector

  //Specifies up or down
  int direction = ( abs(vector) - vector) / abs(2*vector);
  digitalWrite(dirPin1, direction);
  digitalWrite(dirPin2, direction);

  //Move the device
  int numSteps = distToStep(vector);
  for(int i=0;i<numSteps;i++) {
    digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin2, HIGH);
    delayMicroseconds(50);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    delayMicroseconds(50);
  }
}


// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// ~~~~~ Zero the unit ~~~~~
void goToZero() {
  //Move slightly down first
  digitalWrite(dirPin1, 0);
  digitalWrite(dirPin2, 1);

  for(int i=0;i<100;i++) {
    digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin2, HIGH);
    delayMicroseconds(50);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    delayMicroseconds(50);
  }

  //Move slightly to the right
  digitalWrite(dirPin1, 0);
  digitalWrite(dirPin2, 0);

  for(int i=0;i<100;i++) {
    digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin2, HIGH);
    delayMicroseconds(50);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    delayMicroseconds(50);
  }

  //Move Y until it hits the switch
  digitalWrite(dirPin1, 1);
  digitalWrite(dirPin2, 0);

  while(digitalRead(yLimit) == 0) {
    digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin2, HIGH);
    delayMicroseconds(200);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    delayMicroseconds(200);    
  }

  //Move X until it hits the switch
  digitalWrite(dirPin1, 1);
  digitalWrite(dirPin2, 1);

  while(digitalRead(xLimit) == 0) {
    digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin2, HIGH);
    delayMicroseconds(200);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    delayMicroseconds(200);    
  }

  //Move slightly down
  digitalWrite(dirPin1, 0);
  digitalWrite(dirPin2, 1);

  for(int i=0;i<100;i++) {
    digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin2, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    delayMicroseconds(500);
  }

  //Move slightly to the right
  digitalWrite(dirPin1, 0);
  digitalWrite(dirPin2, 0);

  for(int i=0;i<100;i++) {
    digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin2, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    delayMicroseconds(500);
  }

  //Move up really slowly same distance as it was moved down in the last step
  digitalWrite(dirPin1, 1);
  digitalWrite(dirPin2, 0);

  for(int i=0;i<100;i++) {
    digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin2, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    delayMicroseconds(500);
  }

  //Move left really slowly same distance as it was moved right in the last step
  digitalWrite(dirPin1, 1);
  digitalWrite(dirPin2, 1);

  for(int i=0;i<100;i++) {
    digitalWrite(stepPin1, HIGH);
    digitalWrite(stepPin2, HIGH);
    delayMicroseconds(500);
    digitalWrite(stepPin1, LOW);
    digitalWrite(stepPin2, LOW);
    delayMicroseconds(500);
  }

  //restart calibration if the pad is not zeroed
  if(digitalRead(yLimit) == 0 || digitalRead(xLimit) == 0){
    goToZero();
  }
}