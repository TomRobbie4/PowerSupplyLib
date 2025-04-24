//piloteUSART2:
//Historique: 
// 2018-09-30, Yves Roy, creation

//INCLUSIONS
#include "main.h"
#include "Serial.h"

//Definitions privees
#define LEDC_CHANNEL_1 0
#define LEDC_CHANNEL_2 1
#define LEDC_CHANNEL_3 2
#define LEDC_CHANNEL_4 3
#define LEDC_CHANNEL_5 4
#define LEDC_CHANNEL_6 5
#define LEDC_CHANNEL_7 6
#define LEDC_CHANNEL_8 7

//Declarations de fonctions privees:
//pas de fonctions privees

//Definitions de variables privees:

//Definitions de fonctions privees:
//pas de fonctions privees

//Definitions de variables publiques:
// pas de variables publiques

//Definitions de fonctions publiques:
// pas de definitions publiques

//Fonctions publiques:
unsigned char SERIAL_octetDisponible(void)
{
  return Serial.available();
}

unsigned char SERIAL_litUnOctetRecu(void)
{
  return Serial.read();
}

void SERIAL_transmet(unsigned char Octet)
{
  Serial.write(Octet);
}

void SERIAL_initialise(void)
{
  Serial.begin(115200, SERIAL_8N1, SERIAL_RX, SERIAL_TX);
}
