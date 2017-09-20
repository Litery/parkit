#include <iostream>
#include "simulation.h"

using namespace std;

void Rectangle::set_values(int x, int y) {
    width = x;
    height = y;
}

Polygon::Polygon(std::vector<double> x_vertices, std::vector<double> y_vertices) {
    this->x_vertices = x_vertices;
    this->y_vertices = y_vertices;
}

int Polygon::point_inside(double x, double y) {
    return pnpoly(x_vertices, y_vertices, x, y);
}

int Polygon::any_inside(Polygon & polygon) {
    int inside = 0, size = x_vertices.size();
    for (int i = 0; i < size && !inside; i++) {
        inside = polygon.point_inside(x_vertices[i], y_vertices[i]);
    }
    return inside;
}

int Polygon::collides(Polygon & polygon) {
    return any_inside(polygon) || polygon.any_inside(*this);
}

int pnpoly(std::vector<double> & vertx, std::vector<double> & verty, double testx, double testy) {
    int i, j, c = 0, nvert = vertx.size();
    for (i = 0, j = nvert - 1; i < nvert; j = i++) {
        if (((verty[i] > testy) != (verty[j] > testy)) &&
            (testx < (vertx[j] - vertx[i]) * (testy - verty[i]) / (verty[j] - verty[i]) + vertx[i]))
            c = !c;
    }
    return c;
}