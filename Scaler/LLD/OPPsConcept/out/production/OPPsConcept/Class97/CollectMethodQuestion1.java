import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class CollectMethodQuestion1 {
    public static void main(String[] args) {
        List<String> fruits = Arrays.asList("apple", "banana", "orange", "grape", "kiwi");

        // What does the following code snippet do?
        String result = fruits.stream()
                .collect(Collectors.joining(", "));

        System.out.println("Result: " + result);
    }
}