#ifndef PWM_CHANNEL_H
#define PWM_CHANNEL_H

//MODULE: PWM_Channel
//DESCRIPTION:

//HISTORIQUE:
// 2021-04-04, Yves Roy, creation

//DEFINITIONS REQUISES PAR LE MODULE:
//Dependances materielles
//(copiez et adaptez ce qui suit dans "main.h")
//#define INTERFACEHCSR04_FREQUENCE_DES_LECTURES_EN_HZ
//#define INTERFACEHCSR04_TEMPS_ECHO_MAX_MS 40

//Dependances logicielles
//(copiez et adaptez ce qui suit dans "main.h")
//#define INTERFACEHCSR04_PHASE 0
//#define INTERFACEHCSR04_SEUIL_ERREUR 38
/*#define LEDC_TIMER_12_BIT 12
#define LEDC_BASE_FREQ 9750  // 40MHz / (2^12 - 1) = 9768Hz

#define CH1_recept_byte '1'
#define CH2_recept_byte '2'
#define CH3_recept_byte '3'
#define CH4_recept_byte '4'
#define CH5_recept_byte '5'
#define CH6_recept_byte '6'
#define CH7_recept_byte '7'
#define CH8_recept_byte '8'

#define OUT_CH1_PIN 4
#define OUT_CH2_PIN 5
#define OUT_CH3_PIN 6
#define OUT_CH4_PIN 7
#define OUT_CH5_PIN 15
#define OUT_CH6_PIN 16
#define OUT_CH7_PIN 17
#define OUT_CH8_PIN 18*/

//INFORMATION PUBLIQUE:
//Definitions publiques:

typedef struct
{
  unsigned char number;
  bool status;  
  int duty;
} PWMChannel;

//Fonctions publiques:
void PWM_Channel_initialise(void);
void PWM_Channel_updateValue(byte channel_number, bool channel_status, int channel_duty);
void Channel_updateStatus(byte channel_number, bool channel_status);
void Channel_updateDuty(byte channel_number,int channel_duty);
void Channel_traiteLesDonneesRecus(byte channel_number);

//Variables publiques
extern PWMChannel CH1;
extern PWMChannel CH2;
extern PWMChannel CH3;
extern PWMChannel CH4;
extern PWMChannel CH5;
extern PWMChannel CH6;
extern PWMChannel CH7;
extern PWMChannel CH8;

#endif
