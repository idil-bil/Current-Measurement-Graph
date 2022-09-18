
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define one_shot_time 10
#define loop_time 100
#define A_READ_PIN 34
#define VDD 3.3
#define R_ohm 1000

void setup() {
  Serial.begin(115200);
}

void loop() {
  float average_v;
  double current;

  average_v = avg();
  current = (VDD - average_v)/R_ohm;

  Serial.println(current,8); //8 sig figs
}

float avg(void) {
  int sum = 0;
  float average_v = 0.0;
  
  for(int n=0; n<loop_time; n++){ 
    unsigned long t0 = millis();
    sum += analogRead(A_READ_PIN);
     
    while ((millis()-t0) < one_shot_time); // Wait up to 100ms passed
   }
   
  average_v =  (float)sum/loop_time;

  return average_v * (3.3 / 4096.0);
}
