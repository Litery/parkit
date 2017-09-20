/* File: simulation.i */
%module simulation
%include "carrays.i"
%array_class(double, DoubleArray);

%{
#define SWIG_FILE_WITH_INIT
#include "simulation.h"
%}

%include "std_vector.i"
// Instantiate templates used by example
namespace std {
   %template(IntVector) vector<int>;
   %template(DoubleVector) vector<double>;
}

class Rectangle {
    public:
    int width, height;
    void set_values (int x, int y);
    int area (void);
};

bool pnpoly(std::vector<double> vertx, std::vector<double> verty, double testx, double testy);