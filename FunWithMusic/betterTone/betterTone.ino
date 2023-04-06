
int buzzPin = 8;

void setup(){
    pinMode(buzzPin, OUTPUT);
    playTone(300, buzzPin, 4000);
}
void loop(){
    
}

void playTone(int freq, int pin, int dur){
    unsigned long microsPerPeriod = 1000000/freq;
    unsigned long microsPerHalf = microsPerPeriod / 2;
    unsigned long microsLastSwitch = micros();
    unsigned long millisAtStart = millis();
    boolean state = false;

    while((millis() - millisAtStart) < dur){
        if(micros() - microsLastSwitch >= microsPerHalf){
            state = switchPin(pin, state);
            microsLastSwitch = micros();
        }
    }
}

boolean switchPin(int pin, boolean currentState){
    digitalWrite(pin, currentState ? LOW : HIGH);
    return !currentState;
}