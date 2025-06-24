from typing import List, Dict
import re
from collections import Counter


def word_frequencies(sentences: List[str]) -> Dict[str, int]:
  
    dict = {}
    
    for s in sentences:     
        # TODO:Flatten the list and join all sentences into a single string   
        s = re.sub(r'[^a-zA-Z]', ' ', s)
        # TODO: Tokenization: Split the string into individual words
        # TODO: Word Counting: Count the frequency of each word
        for word in s.split(" "):  
            if word != '':          
                if word.lower() in dict:
                    dict[word.lower()] += 1
                else:
                    dict[word.lower()] = 1

    # TODO: Return the dicitonary of the words and frequencies
    return dict



# Sample code for your reference
sentences = [
    "Python!! is, a popular programming language",
    "I love coding in Python",
    "Java is also a@@ great language"
]

# Get word frequencies
result = word_frequencies(sentences)

# Print the result
print(result)

# Expected Output:
# {'python': 2, 'is': 2, 'a': 2, 'popular': 1, 'programming': 1, 'language': 2, 'i': 1, 'love': 1, 'coding': 1, 'in': 1, 'java': 1, 'also': 1, 'great': 1}

