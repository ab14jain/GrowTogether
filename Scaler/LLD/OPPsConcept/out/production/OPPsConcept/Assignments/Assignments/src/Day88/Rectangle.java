package Day88;

public class Rectangle {
    // write the code of Rectangle class here

    Point topLeft;
    Point bottomRight;

    public Rectangle(int topLeftX, int topLeftY, int bottomRightX, int bottomRightY){


    }

    public Rectangle(Point topLeft, Point bottomRight){
        this.topLeft = topLeft;
        this.bottomRight = bottomRight;

    }

    public Rectangle(Rectangle rect){

        this.topLeft = rect.topLeft;
        this.bottomRight = rect.bottomRight;

    }

    public static void main(String[] args){
        Rectangle r = new Rectangle(1,2,3,4);
    }
}

