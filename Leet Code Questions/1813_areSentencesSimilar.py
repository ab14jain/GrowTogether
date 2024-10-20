class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        s1 = sentence1.split()
        s2 = sentence2.split()


        if len(s1) < len(s2):
            s1, s2 = s2, s1

        i,j = 0, len(s1)-1
        k,l = 0, len(s2)-1
        
        while k < len(s2) and i < len(s1) and s1[i] == s2[k]:            
            i += 1
            k += 1
        
        while l >= k and s1[j] == s2[l]:              
            j -= 1
            l -= 1
        
        if l < k:
            return True 
        
        return False

        
    
s = Solution()
print(s.areSentencesSimilar("C D", "A B C D")) # True

# print(s.areSentencesSimilar("Ogn WtWj HneS", "Ogn WtWj HneS")) # True
# print(s.areSentencesSimilar("My name is Haley", "My Haley")) # True
# print(s.areSentencesSimilar("of", "A lot of words")) # False
# print(s.areSentencesSimilar("Eating right now", "Eating")) # True
# print(s.areSentencesSimilar("Luky", "Lucccky")) # False
# print(s.areSentencesSimilar("Luky", "Luky")) # True
# print(s.areSentencesSimilar("Hello Jane", "Hello my name is Jane")) # True
# print(s.areSentencesSimilar("Frog cool", "Frogs are cool")) # False


# print(s.areSentencesSimilar("A B C", "A C")) # True
# print(s.areSentencesSimilar("A B C", "A D")) # False
# print(s.areSentencesSimilar("A B", "A B C D")) # True
# print(s.areSentencesSimilar("C D", "A B C D")) # True
# print(s.areSentencesSimilar("eTUny i b R UFKQJ EZx JBJ Q xXz", "eTUny i R EZx JBJ xXz")) # True
