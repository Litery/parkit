/* File: simulation.i */
%module simulation

%{
#define SWIG_FILE_WITH_INIT
#include "simulation.h"
%}

class Rectangle {
public:
    int width, height;
    void set_values (int x, int y);
    int area (void);
};