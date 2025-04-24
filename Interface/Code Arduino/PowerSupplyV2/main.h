#ifndef MAIN_H
#define MAIN_H

#define True 1
#define False 0

// Serial
#define SERIAL_RX 44
#define SERIAL_TX 43

// PWM_Channel
#define LEDC_TIMER_12_BIT 12
#define LEDC_BASE_FREQ 9750  // 40MHz / (2^12 - 1) = 9768Hz

#define OUT_CH1_PIN 4
#define OUT_CH2_PIN 5
#define OUT_CH3_PIN 6
#define OUT_CH4_PIN 7
#define OUT_CH5_PIN 15
#define OUT_CH6_PIN 16
#define OUT_CH7_PIN 17
#define OUT_CH8_PIN 18

// Define pour la communication

#define CARACTERE_DEPART '$'

#define CH1_recept_byte 1
#define CH2_recept_byte 2
#define CH3_recept_byte 3
#define CH4_recept_byte 4
#define CH5_recept_byte 5
#define CH6_recept_byte 6
#define CH7_recept_byte 7
#define CH8_recept_byte 8

#define FONCTION_STATE 'S'
#define FONCTION_DUTY 'D'

#define OPEN_CHANNEL 1
#define CLOSE_CHANNEL 0



#endif