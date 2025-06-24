package Day88;

public class Person {

    int age;
    String name;

    Person(int age, String name){
        this.age = age;
        this.name = name;
    }

    public static void main(String[] args) {
        Person p = new Person(33, "sdf");
    }
}
