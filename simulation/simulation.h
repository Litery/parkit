class Rectangle {
public:
    int width, height;

    void set_values(int x, int y);

    int area() { return width * height; };
};

int pnpoly(int nvert, double *vertx, double *verty, double testx, double testy);