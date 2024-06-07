'''
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"'''

# Brute force
def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        list_sen = sentence.split(" ")
        for i in range(len(list_sen)):
            s = ''
            for j in list_sen[i]:
                s += j
                if s in dictionary:
                    list_sen[i] = s
                    break
            
        return ' '.join(list_sen)
        

# Optimal use Trie

class Node:
        def __init__(self):
            self.links = [None] * 26
            self.flag = False
        
        def get(self, ch):
            return self.links[ord(ch) - ord('a')]

        def containskey(self, ch):
            return self.links[ord(ch)-ord('a')]

        def put(self, ch):
            self.links[ord(ch)-ord('a')] = Node()

        def setkey(self):
            self.flag = True

            
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for i in word:
            if not node.containskey(i):
                node.put(i)
            node = node.get(i)
        node.setkey()

    def find_prefix(self, word):
        node = self.root
        s = ''
        for i in word:
            if node.containskey(i):
                s += i
                node = node.get(i)
                if node.flag == True:
                    break
            else:
                break
        if node.flag == True:
            return s
        else:
            return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for i in dictionary:
            trie.insert(i)

        list_sen = sentence.split(" ")
        for i in range(len(list_sen)):
            s = trie.find_prefix(list_sen[i])
            if s != '':
                list_sen[i] = s
        return " ".join(list_sen)
        # list_sen = sentence.split(" ")
        # for i in range(len(list_sen)):
        #     s = ''
        #     for j in list_sen[i]:
        #         s += j
        #         if s in dictionary:
        #             list_sen[i] = s
        #             break
            
        # return ' '.join(list_sen)
        