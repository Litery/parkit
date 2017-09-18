#include <iostream>
#include "simulation.h"

using namespace std;

void Rectangle::set_values(int x, int y) {
    width = x;
    height = y;
}

int pnpoly(int nvert, double *vertx, double *verty, double testx, double testy) {
    int i, j, c = 0;
    for (i = 0, j = nvert - 1; i < nvert; j = i++) {
        if (((verty[i] > testy) != (verty[j] > testy)) &&
            (testx < (vertx[j] - vertx[i]) * (testy - verty[i]) / (verty[j] - verty[i]) + vertx[i]))
            c = !c;
    }
    return c;
}