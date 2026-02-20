const int LED_ROSSO = 2;
const int LED_VERDE = 4;
const int LED_BLU = 7;
const int BUTTON = 11;

int led_attuale = 1;
bool stato_precedente = HIGH;

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON, INPUT_PULLUP);
  pinMode(LED_VERDE, OUTPUT);
  pinMode(LED_ROSSO, OUTPUT);
  pinMode(LED_BLU, OUTPUT);
}

void loop() {
  bool stato_attuale = digitalRead(BUTTON);

  if(stato_precedente == HIGH && stato_attuale == LOW){

    digitalWrite(LED_ROSSO, LOW);
    digitalWrite(LED_VERDE, LOW);
    digitalWrite(LED_BLU, LOW);

    if(led_attuale == 1){
      digitalWrite(LED_ROSSO, HIGH);
      Serial.println("rosso");
    }
    if(led_attuale == 2){
      digitalWrite(LED_VERDE, HIGH);
      Serial.println("verde");
    }
    if(led_attuale == 3){
      digitalWrite(LED_BLU, HIGH);
      Serial.println("blu");
    }

    if(led_attuale == 3){
      led_attuale = 1;
    }
    else{
      led_attuale++;
    }
  }

  stato_precedente = stato_attuale;
}
