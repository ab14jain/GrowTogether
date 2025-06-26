import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class SentenceProcessor {
    public static int processSentences(List<String> sentences) {
        //code here
        int avg_len = sentences.stream()
        .filter(s -> s.contains("Java"))
        .map(s-> s.length())
        .reduce(0, (a, b) -> a + b);

        List<String> stt = sentences.stream()
                .filter(s -> s.toLowerCase().contains("java"))
                .collect(Collectors.toList());                
                
        if (stt.isEmpty()) {
            return 0;
        }
        return avg_len/stt.size();
    }

    public static void main(String[] args) {
        List<String> sentences = Arrays.asList(
                "Java is a programming language.",
                "Python is also a good language.",
                "Java stream processing is powerful.",
                "C++ is not as popular as Java."
        );

        int averageLength = SentenceProcessor.processSentences(sentences);
        System.out.println(averageLength);

        sentences = Arrays.asList(
                "Python is a programming language.",
                "JS is used for web development.",
                "Ruby is known for its simplicity.",
                "java is good"
        );

        averageLength = SentenceProcessor.processSentences(sentences);
        System.out.println(averageLength);
    }
}