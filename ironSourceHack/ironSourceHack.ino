int sensorPin = A0; // select the input pin for LDR
int sensorValue = 0; // variable to store the value coming from the sensor
int inPin = 2;   // choose the input pin (for a pushbutton)
bool val = false;     // variable for reading the pin status

void setup() {
  pinMode(inPin, INPUT);
  Serial.begin(19200); //sets serial port for communication
}

void loop() {
  val = digitalRead(inPin);
  sensorValue = analogRead(sensorPin); // read the value from the sensor
  Serial.println(sensorValue); //prints the values coming from the sensor
  if (val == HIGH) {
    Serial.println("True");
  }
}
