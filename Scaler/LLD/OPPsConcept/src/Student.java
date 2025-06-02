public class Student {
    int age;
    String name;

    void display(){
        System.out.println("My name is "+ name + ". I am "+age+" years old");
    }

    void sayHello(String string){
        System.out.println(this.name + " says hello to " + string);
    }
}


