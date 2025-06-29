
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class AnimalSorter {

    public static List<String> sortAnimalsByLengthDescending(List<String> animals) {
        return animals.stream()
                //.sorted((a, b) -> Integer.compare(b.length(), a.length())) // Sort by length in descending order
                //add your code here
                .sorted((a, b) -> b.length() - a.length()) // Sort by length in descending order
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        List<String> animals = Arrays.asList("zebra", "lion", "tiger", "elephant", "giraffe");
        List<String> sortedAnimals = sortAnimalsByLengthDescending(animals);
        System.out.println(sortedAnimals);

        animals = Arrays.asList("cat","dog","animal-x","elephant","mouse");
        sortedAnimals = sortAnimalsByLengthDescending(animals);
        System.out.println(sortedAnimals);

        animals = Arrays.asList();
        sortedAnimals = sortAnimalsByLengthDescending(animals);
        System.out.println(sortedAnimals);

        animals = Arrays.asList("a","b","d","c","a");
        sortedAnimals = sortAnimalsByLengthDescending(animals);
        System.out.println(sortedAnimals);
    }
}