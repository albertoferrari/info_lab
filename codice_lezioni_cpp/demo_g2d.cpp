/**
 * @author Alberto Ferrari - https://albertoferrari.github.io/
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 * 
 * demo utilizzo g2d
 */

#include "g2d/canvas.hpp"			//path relativo per g2d

int main() {
	int r,g,b;

	g2d::Point dim = {800,600};		//struct Point coppia interi
	g2d::init_canvas(dim);			//inizializzazione canvas
	r = g2d::randint(0, 255);		//random estremi inclusi
	g = g2d::randint(0, 255);
	b = g2d::randint(0, 255);
	g2d::Color c = {r,g,b};			//struct Color tripla interi
	g2d::set_color(c);				//impostazione colore
	g2d::Point p = {200,300};
	g2d::fill_circle(p,50);			//cerchio (centro, raggio)
	g2d::Rect rett = {400,350,70,120};	//strict Rect quadrupla interi
	g2d::set_color({0,0,255});		//blu
	g2d::fill_rect(rett);				//rettangolo x,y,w,h
	g2d::draw_line({0,0},{600,600});
	g2d::draw_text("hello",{400,300},30);	//testo,posizione,dimensione
	g2d::main_loop();				//loop
}
