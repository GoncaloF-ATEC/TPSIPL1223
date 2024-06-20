//
//  main.c
//  demo
//
//  Created by Gonçalo Feliciano on 05/06/2024.
//

#include <stdio.h>


typedef struct myStructure {
  int myNum;
  char myLetter;
} teste;



typedef char* Texto;

Texto nome;


int main(int argc, const char * argv[]) {
  
    
    nome = "bla bla bla bla";
    printf("%s\n", nome);
    
    return 0;
}
