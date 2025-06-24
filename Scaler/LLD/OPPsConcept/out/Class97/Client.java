import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Client {

    public static void main(String[] args) {

        System.out.println(Client.getOdd(Stream.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)));
        System.out.println(Client.areAllEven(Stream.of(2,4,6,8,10)));
        System.out.println((Stream.of(2,4,6,8,10).findFirst()));

        Stream.iterate(1, i -> i <=20, i -> i*2)
            .forEach(System.out::println);
    
    }

    static List<Integer> getOdd(Stream<Integer> stream){
        // write code here

        return stream.filter(num -> num % 2 != 0).collect(Collectors.toList());                                   
        
    }

    static boolean areAllEven(Stream<Integer> stream){

        // write code here
        return stream.allMatch(num -> num % 2 == 0);
    }
    
}