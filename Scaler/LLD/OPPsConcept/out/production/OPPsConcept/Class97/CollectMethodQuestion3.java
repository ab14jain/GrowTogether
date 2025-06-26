import java.util.Arrays;
import java.util.List;
import java.util.Set;

public class CollectMethodQuestion3 {
    
    public static void main(String [] args){
        List<String> fruits = Arrays.asList("apple", "banana", "orange", "grape", "kiwi");
        Set<String> uniqueFruits = fruits.stream()
                .collect(java.util.stream.Collectors.toSet());
        System.out.println("Unique fruits: " + uniqueFruits);}
}
