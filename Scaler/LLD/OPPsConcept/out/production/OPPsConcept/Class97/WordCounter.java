import java.util.Arrays;
import java.util.List;

// import java.util.stream.Stream;

public class WordCounter {
    public static long countWords(List<String> sentences) {

        return sentences.stream()
                // Step 1: Filter sentences containing "Java"
                .filter(sentence -> !sentence.contains("Java"))

                // Step 2: Map to a list of unique words (split by whitespace)
                .map(sentence -> {
                    String[] words = sentence.split("\\s+");
                    return Arrays.stream(words)
                                 .distinct()
                                 .toArray(String[]::new);
                })

                // Step 3: Flatten the stream of arrays into a single stream of words
                .flatMap(Arrays::stream)

                // Step 4: Count total number of words
                .count();
    }

    public static void main(String[] args) {
        List<String> sentences = Arrays.asList(
                "Python is a programming language.",
                "JaDSvaScript is used for web development.",
                "Ruby is known for its simplicity."
        );

        // List<String> sentences = Arrays.asList(
        //         "Java is a programming language.",
        //         "Python is also a good language.",
        //         "Java stream processing is powerful.",
        //         "C++ is not as popular as Java."
        // );

        // List<String> sentences = Arrays.asList();
        long wordCount = WordCounter.countWords(sentences);
        System.out.println(wordCount);
    }
}