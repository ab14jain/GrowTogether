

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
// import java.util.stream.Stream;

public class WordCounter {
    public static long countWords(List<String> sentences) {

        Stream<Object> sd = sentences.stream()
        .filter(s -> !s.contains("Java"))
        .map(s -> s.split(" "))
        .distinct()
        .flatMap(s -> Arrays.stream(s.split(" ")));
        //.collect(Collectors.toList());
        sd.forEach(s -> System.out.println(s));
        // System.out.println(sd);
        return -1L;
    }

    public static void main(String[] args) {
        List<String> sentences = Arrays.asList(
                "Python is a programming language.",
                "JavaScript is used for web development.",
                "Ruby is known for its simplicity."
        );

        long wordCount = WordCounter.countWords(sentences);
        System.out.println(wordCount);
    }
}