#include "main.h"
#include "PWM_Channel.h"
#include "Serial.h"

// LED Pin for controlling via serial input
int ledPin = 13;  // Broche de la LED

bool data_flag = 0;
byte channel;

void setup() {
  // Initialiser la communication série à 115200 bauds
  SERIAL_initialise();
  PWM_Channel_initialise();
  //Serial.begin(115200);

  // Initialiser les broches LED comme une sortie
  pinMode(ledPin, OUTPUT);
}

void loop() {

  // Vérifier si des données sont disponibles sur le port série
  if (SERIAL_octetDisponible() >= 3) {  // S'assurer qu'il y a au moins 3 octets
    // Lire le premier octet (qui devrait être '$')
    char receivedChar = Serial.read();

    // Vérifier si le caractère reçu est un '$'
    if (receivedChar == CARACTERE_DEPART) {

      channel = SERIAL_litUnOctetRecu();  // Lire le premier octet du nombre
      byte fonction = SERIAL_litUnOctetRecu();
      if(fonction == FONCTION_STATE)
      {
        byte status = SERIAL_litUnOctetRecu();
        Channel_updateStatus(channel, (bool)status);
      }
      if(fonction == FONCTION_DUTY)
      {
        byte highByte = SERIAL_litUnOctetRecu();  // Lire le premier octet du nombre
        byte lowByte = SERIAL_litUnOctetRecu();   // Lire le deuxième octet du nombre
        int number = (highByte << 8) | lowByte;  // Décoder les deux octets en un entier
        Channel_updateDuty(channel, number);
        Serial.write(number);
      }
      
      data_flag = True;
      //Serial.write(channel);
      //Serial.write(status);

      //PWM_Channel_updateValue(channel, (bool)status, number);
    }
  }
  if(data_flag == True)
  {
    
    Channel_traiteLesDonneesRecus(channel);
    data_flag = False;
  }
}
