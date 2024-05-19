#include <stdio.h>
#include "stdlib.h"

int getStatus(){
    return 0;
}

int main(void)
{
    char variable[512];
    char * paraAsignar = "Mundo";
    snprinf(variable, sizeof(variable), "Hola %s", paraAsignar);
    printf(variable);
    return getStatus();
}