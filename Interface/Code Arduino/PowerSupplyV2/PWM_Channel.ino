#include "main.h"
#include "PWM_Channel.h"

////////////////////////////////////
#include "Wire.h"
#include "DFRobot_MCP4725.h"
#define  REF_VOLTAGE    3300

#define SDA_PIN 39
#define SCL_PIN 40

DFRobot_MCP4725 DAC;
DFRobot_MCP4725 DACCH1;

uint16_t OUTPUT_VOLTAGE = 0;        // unit : mV 

////////////////////////////////////////////////

#define LEDC_CHANNEL_1 0
#define LEDC_CHANNEL_2 1
#define LEDC_CHANNEL_3 2
#define LEDC_CHANNEL_4 3
#define LEDC_CHANNEL_5 4
#define LEDC_CHANNEL_6 5
#define LEDC_CHANNEL_7 6
#define LEDC_CHANNEL_8 7

PWMChannel CH1;
PWMChannel CH2;
PWMChannel CH3;
PWMChannel CH4;
PWMChannel CH5;
PWMChannel CH6;
PWMChannel CH7;
PWMChannel CH8;

//Fonctions publiques:
void PWM_Channel_initialise(void)
{
  ////////////////////////
  Wire.begin(SDA_PIN, SCL_PIN);
  DAC.init(MCP4725A0_IIC_Address0, REF_VOLTAGE);
  DACCH1.init(MCP4725A0_IIC_Address1, REF_VOLTAGE);
  DAC.outputVoltageEEPROM(0);
  DACCH1.outputVoltageEEPROM(0);
  ///////////////////////////
  CH1.number = CH1_recept_byte;
  CH1.duty = 0;
  CH1.status = False;
  
  CH2.number = CH1_recept_byte;
  CH2.duty = 0;
  CH2.status = False;
  
  CH3.number = CH1_recept_byte;
  CH3.duty = 0;
  CH3.status = False;
  
  CH4.number = CH1_recept_byte;
  CH4.duty = 0;
  CH4.status = False;
  
  CH5.number = CH1_recept_byte;
  CH5.duty = 0;
  CH5.status = False;
  
  CH6.number = CH1_recept_byte;
  CH6.duty = 0;
  CH6.status = False;

  CH7.number = CH1_recept_byte;
  CH7.duty = 0;
  CH7.status = False;
  
  CH8.number = CH1_recept_byte;
  CH8.duty = 0;
  CH8.status = False;

  ledcAttachChannel(OUT_CH1_PIN, LEDC_BASE_FREQ, LEDC_TIMER_12_BIT, LEDC_CHANNEL_1);
  ledcAttachChannel(OUT_CH2_PIN, LEDC_BASE_FREQ, LEDC_TIMER_12_BIT, LEDC_CHANNEL_2);
  ledcAttachChannel(OUT_CH3_PIN, LEDC_BASE_FREQ, LEDC_TIMER_12_BIT, LEDC_CHANNEL_3);
  ledcAttachChannel(OUT_CH4_PIN, LEDC_BASE_FREQ, LEDC_TIMER_12_BIT, LEDC_CHANNEL_4);
  ledcAttachChannel(OUT_CH5_PIN, LEDC_BASE_FREQ, LEDC_TIMER_12_BIT, LEDC_CHANNEL_5);
  ledcAttachChannel(OUT_CH6_PIN, LEDC_BASE_FREQ, LEDC_TIMER_12_BIT, LEDC_CHANNEL_6);
  ledcAttachChannel(OUT_CH7_PIN, LEDC_BASE_FREQ, LEDC_TIMER_12_BIT, LEDC_CHANNEL_7);
  ledcAttachChannel(OUT_CH8_PIN, LEDC_BASE_FREQ, LEDC_TIMER_12_BIT, LEDC_CHANNEL_8);

  setChannelDuty(LEDC_CHANNEL_1, 0);
  setChannelDuty(LEDC_CHANNEL_2, 0);
  setChannelDuty(LEDC_CHANNEL_3, 0);
  setChannelDuty(LEDC_CHANNEL_4, 0);
  setChannelDuty(LEDC_CHANNEL_5, 0);
  setChannelDuty(LEDC_CHANNEL_6, 0);
  setChannelDuty(LEDC_CHANNEL_7, 0);
  setChannelDuty(LEDC_CHANNEL_8, 0);
}

void Channel_traiteLesDonneesRecus(byte channel_number)
{
  switch(channel_number)
      {
        case CH1_recept_byte: 
          if(CH1.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_1, CH1.duty);
            
            DACCH1.outputVoltageEEPROM((uint16_t)round((CH2.duty * 3300) / 4096));
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_1, 0);
            DACCH1.outputVoltageEEPROM(0);
          }
          break;

        case CH2_recept_byte: 
          if(CH2.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_2, CH2.duty);
            /////////////////////////////
            DAC.outputVoltageEEPROM((uint16_t)round((CH2.duty * 3300) / 4096));
            //////////////////////////////////////////////
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_2, 0);
            DAC.outputVoltageEEPROM(0);
          }
          break;
        
        case CH3_recept_byte: 
          if(CH3.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_3, CH3.duty);
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_3, 0);
          }
          break;
        
        case CH4_recept_byte: 
          if(CH4.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_4, CH4.duty);
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_4, 0);
          }
          break;

        case CH5_recept_byte: 
          if(CH5.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_5, CH5.duty);
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_5, 0);
          }
          break;

        case CH6_recept_byte: 
          if(CH6.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_6, CH6.duty);
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_6, 0);
          }
          break;

        case CH7_recept_byte: 
          if(CH7.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_7, CH7.duty);
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_7, 0);
          }
          break;

        case CH8_recept_byte: 
          if(CH8.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_8, CH8.duty);
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_8,0);
          }
          break;
      }
}

void Channel_updateStatus(byte channel_number, bool channel_status)
{
  switch(channel_number)
      {
        case CH1_recept_byte: 
          CH1.status = channel_status;
          break;

        case CH2_recept_byte: 
          CH2.status = channel_status;
          break;
        
        case CH3_recept_byte: 
          CH3.status = channel_status;
          break;
        
        case CH4_recept_byte: 
          CH4.status = channel_status;
          break;

        case CH5_recept_byte: 
          CH5.status = channel_status;
          break;

        case CH6_recept_byte: 
          CH6.status = channel_status;
          break;

        case CH7_recept_byte: 
          CH7.status = channel_status;
          break;

        case CH8_recept_byte: 
          CH8.status = channel_status;
          break;
      }
}

void Channel_updateDuty(byte channel_number, int channel_duty)
{
  switch(channel_number)
      {
        case CH1_recept_byte: 
          CH1.duty = channel_duty;
          break;

        case CH2_recept_byte: 
          CH2.duty = channel_duty;
          break;
        
        case CH3_recept_byte: 
          CH3.duty = channel_duty;
          break;
        
        case CH4_recept_byte: 
          CH4.duty = channel_duty;
          break;

        case CH5_recept_byte: 
          CH5.duty = channel_duty;
          break;

        case CH6_recept_byte: 
          CH6.duty = channel_duty;
          break;

        case CH7_recept_byte: 
          CH7.duty = channel_duty;
          break;

        case CH8_recept_byte: 
          CH8.duty = channel_duty;
          break;
      }
}

void PWM_Channel_updateValue(byte channel_number, bool channel_status, int channel_duty)
{
  switch(channel_number)
      {
        case CH1_recept_byte: 
          CH1.status = channel_status;
          CH1.duty = channel_duty;
          if(CH1.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_1, CH1.duty);
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_1, 0);
          }
          break;

        case CH2_recept_byte: 
          CH2.status = channel_status;
          CH2.duty = channel_duty;
          if(CH2.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_2, CH2.duty);
            DAC.outputVoltageEEPROM((uint16_t)(((3.3 / 4096) * CH2.duty)*1000));
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_2, 0);
          }
          break;
        
        case CH3_recept_byte: 
          CH3.status = channel_status;
          CH3.duty = channel_duty;
          if(CH3.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_3, CH3.duty);
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_3, 0);
          }
          break;
        
        case CH4_recept_byte: 
          CH4.status = channel_status;
          CH4.duty = channel_duty;
          if(CH4.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_4, CH4.duty);
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_4, 0);
          }
          break;

        case CH5_recept_byte: 
          CH5.status = channel_status;
          CH5.duty = channel_duty;
          if(CH5.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_5, CH5.duty);
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_5, 0);
          }
          break;

        case CH6_recept_byte: 
          CH6.status = channel_status;
          CH6.duty = channel_duty;
          if(CH6.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_6, CH6.duty);
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_6, 0);
          }
          break;

        case CH7_recept_byte: 
          CH7.status = channel_status;
          CH7.duty = channel_duty;
          if(CH7.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_7, CH7.duty);
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_7, 0);
          }
          break;

        case CH8_recept_byte: 
          CH8.status = channel_status;
          CH8.duty = channel_duty;
          if(CH8.status == True)
          {
            setChannelDuty(LEDC_CHANNEL_8, CH8.duty);
          }
          else
          {
            setChannelDuty(LEDC_CHANNEL_8,0);
          }
          break;
      }
}

void setChannelDuty(char channel, int duty)
{
  ledcWriteChannel(channel, duty);
  // Can change to DAC...
}
