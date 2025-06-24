package Day88;

public class Point {
    // write the code of point class here

    int x;
    int y;

    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }

    public Point(Point cc){
        this.x = cc.x;
        this.y = cc.y;
    }
}
