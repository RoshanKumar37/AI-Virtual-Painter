#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10 //RX slave select 
#define RST_PIN 9

MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance.

byte card_ID[4]; //card UID size 4byte
byte Name1[4]={0x13, 0x9B, 0xB8, 0x97};//first UID card
byte Name2[4]={0x35, 0xB1,0x61, 0xC9};//second UID card

int NumbCard[2];
int j=0;        

int const RedLed=6;
int const GreenLed=5;
int const Buzzer=8;

String Name;
long Number;
int n ; 

void setup() {
  Serial.begin(9600); 
  SPI.begin();  
  mfrc522.PCD_Init(); 
  
  Serial.println("CLEARSHEET");                 
  Serial.println("LABEL,Date,Time,Name,Roll Number");

  pinMode(RedLed,OUTPUT);
  pinMode(GreenLed,OUTPUT);
  pinMode(Buzzer,OUTPUT);

  }
    
void loop() {
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
  return;
}

if ( ! mfrc522.PICC_ReadCardSerial()) {
  return;
}

for (byte i = 0; i < mfrc522.uid.size; i++) {
    card_ID[i]=mfrc522.uid.uidByte[i];

      if(card_ID[i]==Name1[i]){
      Name="Roshan";
      Number=1;
      j=0;
      }
      else if(card_ID[i]==Name2[i]){
      Name="Sanku";
      Number=2;
      j=1;
      }
      else{
          digitalWrite(GreenLed,LOW);
          digitalWrite(RedLed,HIGH);
          goto cont;
    }
}
      if(NumbCard[j] == 1){
      //Serial.println("Already Exist");
      }
      else{
      NumbCard[j] = 1;
      n++;
      Serial.print("DATA,DATE,TIME," + Name);
      Serial.print(",");
      Serial.println(Number);
      digitalWrite(GreenLed,HIGH);
      digitalWrite(RedLed,LOW);
      digitalWrite(Buzzer,HIGH);
      delay(30);
      digitalWrite(Buzzer,LOW);
      Serial.println("SAVEWORKBOOKAS,Names/WorkNames");
      }
      delay(1000);
cont:
delay(2000);
digitalWrite(GreenLed,LOW);
digitalWrite(RedLed,LOW);
}
