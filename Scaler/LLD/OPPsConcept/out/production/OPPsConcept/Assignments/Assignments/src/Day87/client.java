package Day87;

public class client {

    public static void main(String[] args) {

        BankAccount ba = new BankAccount();
        ba.balance = 1312;
        ba.roi = 4;

        System.out.println(ba.getSimpleInterest(4));
        System.out.println(ba.getBalanceWithInterest(4));

//        Rectangle rect = new Rectangle();
//
//        rect.height = 40;
//        rect.width = 20;
//
//        System.out.println(rect.getArea());
//        System.out.println(rect.getPerimeter());
//        System.out.println(rect.getBottomRight());

//        Point topLeft = new Point();
//        topLeft.x = 3;
//        topLeft.y = 4;
//
//        Rectangle rect1 = new Rectangle();
//        rect1.topLeft = topLeft;
//        rect1.height = 6;
//        rect1.width = 5;
//
//        System.out.println("Area: " + rect1.getArea());             // Output: 12
//        System.out.println("Perimeter: " + rect1.getPerimeter());   // Output: 14
//        System.out.println("Bottom Right: " + rect1.getBottomRight().x); // Output: Point(x=6, y=2)
//        System.out.println("Bottom Right: " + rect1.getBottomRight().y); // Output: Point(x=6, y=2)
//
//        Student s1 = new Student();
//        s1.age = 10;
//        s1.name = "A";
//
//        Student s2 = new Student();
//
//        int tempAge = s1.age;
//        s1.age = s2.age;
//        s2.age = tempAge;
//
//
//
//        s2.display();
    }
}
