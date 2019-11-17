/**
 * @author Alberto Ferrari - https://albertoferrari.github.io/
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "g2d/canvas.hpp"

auto x = 50, y = 50, dx = 5, dy = 0;
auto ARENA_W = 480, ARENA_H = 360;
auto image = g2d::load_image("ball.png");

void tick() {
	if (g2d::key_pressed("LeftButton")) {
		dx = -dx;
	}
	g2d::clear_canvas();
	g2d::draw_image(image, {x, y});
	x = (x + dx) % ARENA_W;
	if (x<0) 
		x = ARENA_W;
}

int main() {
	g2d::init_canvas({ARENA_W, ARENA_H});
	g2d::main_loop(tick);
}
