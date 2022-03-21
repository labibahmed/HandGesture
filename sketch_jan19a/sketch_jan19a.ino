int f0,f1,f2,f3,f4;
bool isRecording = false;
void setup() {
  // put your setup code here, to run once:
pinMode(A0, INPUT);
pinMode(A1, INPUT);
pinMode(A2, INPUT);
pinMode(A3, INPUT);
pinMode(A4, INPUT);
Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');

    Serial.print("Command: ");
    Serial.println(command);

    // if user sent "record", start recording
    if (command.equals("record")) {
      Serial.println("Start recording...");
      isRecording = true;
    }
    // otherwise stop recording
    else {
      Serial.println("Stop recording...");
      isRecording = false;
    }
  }
  if (!isRecording){
    return;}
   
f0 = analogRead(A1);
f1 =analogRead(A2);
f2 = analogRead(A3);
f3 = analogRead(A4);
f4 = analogRead(A5);
Serial.print(f0);
Serial.print(",");
Serial.print(f1);
Serial.print(",");
Serial.print(f2);
Serial.print(",");
Serial.print(f3);
Serial.print(",");
Serial.println(f4);
delay(1000);
Serial.flush();
}
