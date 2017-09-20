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

class Polygon {
public:
    Polygon(std::vector<double> x_vertices, std::vector<double> y_vertices);
    int any_inside(Polygon & polygon);
    int point_inside(double x, double y);
    int collides(Polygon & polygon);
private:
    std::vector<double> x_vertices;
    std::vector<double> y_vertices;
};

bool pnpoly(std::vector<double> & vertx, std::vector<double> & verty, double testx, double testy);