#include <vector>

class Rectangle {
public:
    int width, height;

    void set_values(int x, int y);

    int area() { return width * height; };
};

class Polygon {
public:
    Polygon(std::vector<double> x_vertices, std::vector<double> y_vertices);
    std::vector<double> x_vertices;
    std::vector<double> y_vertices;
    int any_inside(Polygon & polygon);
};

int pnpoly(std::vector<double> vertx, std::vector<double> verty, double testx, double testy);