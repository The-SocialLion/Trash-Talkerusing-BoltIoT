#include <Ultrasonic.h>/* library to access the function distance read*/ 

 Ultrasonic ultrasonic(12, 13);/*trig-12,echo-13*/ 

 void setup() {/* setting up the sensor to work*/ 

  Serial.begin(9600); /* initializing the frequency to run the sensor*/ 

  } 

 void loop() {/* initializing the loop*/ 

 Serial.println(ultrasonic.distanceRead());/* prints the distance measure by the sensor on the serial monitor also transmits these values to the bolt wifi module*/ 

  delay (4000) ;/* time taken between two consecutive readings*/ 

} 
