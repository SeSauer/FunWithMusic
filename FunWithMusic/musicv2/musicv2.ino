
short * frequencies;
int * durations;
int * punctuations;
int buzzPin = 8;
int arrayLength;

void setup(){
  Serial.begin(9600);
  Serial.println("initV2");
  decodeNotes();
  playFromArrays();
}

void loop(){

}

void decodeNotes(){
    boolean done = 0;
    initArrays();
    int i = 0;
    while (!done){
      if(Serial.available() > 2){
        if (Serial.peek() == 'X'){
        done = true;
        Serial.print("done reading in")
        break;
        }
        int note = smartStrip(Serial.readStringUntil('#')).toInt();
        int dur = smartStrip(Serial.readStringUntil('#')).toInt();
        int punct = smartStrip(Serial.readStringUntil('#')).toInt();
        if (dur > 10){
        writeToArrays(note, dur, punct, i++);
        }
      }
    }
}

int initArrays(){
  int length = smartStrip(Serial.readStringUntil('#')).toInt();
  arrayLength = length;
  int freq[length];
  frequencies = freq;
  int durs[length];
  durations = durs;
  int pnct[length];
  punctuations = pnct;
}

void writeToArrays(int freq, int dur, int punct, int index){
  frequencies[index] = freq;
  durations[index] = dur;
  punctuations[index] = punct;
  Serial.print("Recieved:");
  Serial.print(freq);
  Serial.print(":");
  Serial.print(dur);
  Serial.print(":");
  Serial.println(punct);
  Serial.flush();
}

String smartStrip(String in){
  String out = in;
  out.replace("b", "");
  out.replace("'", "");
  return out;
}

void playNote(int freq, int dur, int punct){

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

void playFromArrays(){
  for(int i = 0; i < arrayLength; i++){
    playNote(frequencies[i], durations[i], punctuations[i]);
  }
}