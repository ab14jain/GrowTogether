package constructors;

public class Student {
    String name;
    int age;
    String batch;
    float psp;

    public Student(){
        name="Default";
        age=10;
    }

    public Student(String name, int age){
        this.name=name;
        this.age=age;
    }

    void displayName(){
        System.out.println("Student name = " + name);
    }
}
