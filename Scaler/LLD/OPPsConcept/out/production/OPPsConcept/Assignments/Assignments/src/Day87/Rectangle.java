package Day87;

public class Rectangle {
    Point topLeft;
    int height;
    int width;


    int getArea(){
        return this.height*this.width;
    }

    int getPerimeter(){
        return 2*(this.height+this.width);
    }

    Point getBottomRight(){
        Point p = new Point();
        p.x = this.topLeft.x + this.width;
        p.y = this.topLeft.y - this.height;
        return p;
    }

}
