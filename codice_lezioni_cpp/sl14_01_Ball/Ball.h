class Ball
{
    public:
        Ball(int x0, int y0);
        void move();
        int get_x();
        int get_y();

        static const int ARENA_W = 320;
        static const int ARENA_H = 240;
        static const int W = 20;
        static const int H = 20;

    protected:

    private:
        int x;
        int y;
        int dx;
        int dy;
};

Ball::Ball(int x0, int y0) {
    x = x0; y = y0; dx = 5; dy = 5;
}
void Ball::move() {
    if (!(0 <= x + dx && x + dx <= ARENA_W - W)) dx = -dx;
    if (!(0 <= y + dy && y + dy <= ARENA_H - H)) dy = -dy;
    x += dx; y += dy;
}
int Ball::get_x() {
    return x;
}
int Ball::get_y() {
    return y;
}
