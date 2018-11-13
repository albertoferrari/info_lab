#include "Ball.h"

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
