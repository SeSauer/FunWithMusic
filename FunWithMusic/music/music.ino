int incoming = 0;
int buzzPin = 8;

void setup(){
  Serial.begin(9600);
  pinMode(A0, OUTPUT);
  Serial.println("init");
}


String smartStrip(String in){
  String out = in;
  out.replace("b", "");
  out.replace("'", "");
  return out;
}

void playNote(int freq, int dur, int punct){
  //if(dur > 2000) {analogWrite(A0, 200);}
  analogWrite(A0, 200);
  int diff = calcDiff(dur, punct);
  int actDur = dur - diff;
  if (freq != 0){
    tone(buzzPin, freq);
  }
  delay(actDur);
  if (punct >= 0){
    noTone(buzzPin);
  }
  delay(diff);
  analogWrite(A0, 0);
  Serial.print(freq);
  Serial.print(":");
  Serial.print(dur);
  Serial.print(":");
  Serial.println(punct);
  Serial.flush();
}

int calcDiff(int dur, int punct){
  if (punct == 0){        //default
    return min(20, dur * 0.1);
  } if (punct < 0){       //long / continuous
    return 0;
  } if (punct > 0){       //short / staccato
    return max(0, dur - 80);
  }
}

void loop(){
  if(Serial.available() > 2){
  int note = smartStrip(Serial.readStringUntil('#')).toInt();
  int dur = smartStrip(Serial.readStringUntil('#')).toInt();
  int punct = smartStrip(Serial.readStringUntil('#')).toInt();
  if (dur > 10){
    playNote(note, dur, punct);
  }
  }
}