#ifndef SERIAL_H
#define SERIAL_H

//MODULE: Serial
//DESCRIPTION: Fonction pour utiliser la communication SERIAL
//HISTORIQUE:
// 2025-03-25 Thomas Robert

//DEFINITIONS REQUISES PAR LE MODULE:
//Dependances materielle
//pas de dépendances matérielles

//Dependances logicielles
//(copiez et adaptez ce qui suit dans "main.h")
//#define SERIAL_RX 16
//#define SERIAL_TX 17

//INFORMATION PUBLIQUE:
//Definitions publiques:
#define SERIAL_DISPONIBLE  1
#define SERIAL_PAS_DISPONIBLE 0
#define SERIAL_TRANSMIS 0
#define SERIAL_PAS_TRANSMIS 1

//Fonctions publiques:
void SERIAL_initialise(void);
unsigned char SERIAL_octetDisponible(void);
unsigned char SERIAL_litUnOctetRecu(void);
void SERIAL_transmet(unsigned char Octet);


#endif
