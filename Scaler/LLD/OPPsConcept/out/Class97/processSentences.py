# TODO: Complete the given function
from collections import defaultdict


def processSentences(sentences):
    # Code here

    def filter_python(s):   
        return 'python' in s
    
    def sentence_len(s):
        return len(s)
    
    
    
    f_sent = filter(filter_python, sentences)
    
    sum_s = 0
    for s in f_sent:
        sum_s += len(s)

    f__new_sent = filter(filter_python, sentences)
    total_sentences = len(list(f__new_sent))
    if total_sentences == 0:
        return 0
    return sum_s//total_sentences


print(processSentences(["python is a programming language.",
                "Pythosdn is also a good language.",
                "python stream processing is powerful.",
                "C++ is not as popular as python."]))

# Sample code for your reference
sentences = [
    "Python!! is, a popular programming language",
    "I love coding in Python",
    "Java is also a@@ great language"
]

# Get word frequencies
result = processSentences(sentences)

# Print the result
print(result)