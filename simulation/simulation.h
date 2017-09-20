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
    int any_inside(Polygon & polygon);
    int point_inside(double x, double y);
    int collides(Polygon & polygon);
private:
    std::vector<double> x_vertices;
    std::vector<double> y_vertices;
};

int pnpoly(std::vector<double> & vertx, std::vector<double> & verty, double testx, double testy);