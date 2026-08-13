class Solution:
    def longestWord(self, words: list[str]) -> str:
   
        words.sort()
        
       
        valid_prefixes = set([""])
        best_word = ""
        
        for word in words:
          
            if word[:-1] in valid_prefixes:
                valid_prefixes.add(word)
                
                
                if len(word) > len(best_word):
                    best_word = word
                    
        return best_word
