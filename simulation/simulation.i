/* File: simulation.i */
%module simulation
%include "carrays.i"
%array_class(double, DoubleArray);

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
int pnpoly(int nvert, double *vertx, double *verty, double testx, double testy);