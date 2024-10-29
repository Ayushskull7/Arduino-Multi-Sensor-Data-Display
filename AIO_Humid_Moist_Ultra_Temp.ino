#include <SimpleDHT.h>

const int trigPin = 9;
const int echoPin = 10;
const int pinDHT11 = 8;
int sensorPin = A0;

SimpleDHT11 dht11(pinDHT11);
float duration, distance;
int sensorValue = 0;
int percentvalue = 0;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // Trigger the ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the duration and calculate the distance
  duration = pulseIn(echoPin, HIGH);
  distance = (duration * 0.0343) / 2;

  // Send ultrasonic data over Serial
  Serial.print("Ultrasonic Distance: ");
  Serial.println(distance);
  delay(500);

  // DHT-11 sensor reading
  byte temperature = 0;
  byte humidity = 0;
  int err;

  err = dht11.read(&temperature, &humidity, NULL);
  if (err != SimpleDHTErrSuccess) {
    Serial.print("DHT11 read error: ");
    Serial.println(err);
    return;
  }

  // Send temperature data over Serial
  Serial.print("Temperature: ");
  Serial.print((int)temperature);
  Serial.print("*C");

  // Send humidity data over Serial
  Serial.print("\nHumidity: ");
  Serial.print((int)humidity);
  Serial.print("%");

  // Soil moisture sensor reading
  sensorValue = analogRead(sensorPin);
  percentvalue = map(sensorValue, 1023, 200, 0, 100);
  
  // Send soil moisture data over Serial
  Serial.print("\nPercentvalue: ");
  Serial.print((int)percentvalue);
  Serial.print("%");

  delay(1000);
}
