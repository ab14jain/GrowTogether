package constructors;

public class Client {
    public static void main(String[] args) {
        Student std = new Student();
        Student std2 = new Student("Abhi", 23);

        std2 = std;
        System.out.println("DEBUG");
    }

}
