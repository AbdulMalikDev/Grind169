class Node:
    def __init__(self,char=None):
        self.char = char
        self.letters = defaultdict(Node)
        self.isEnd = False
        
class Trie:

    def __init__(self):
        self.root = Node('*')

    def insert(self, word: str) -> None:
        if self.root is None: return False
        
        chars = list(word)
        self.insertHelper(self.root,chars)
        
    def insertHelper(self,node,chars):
        
        if chars[0] not in node.letters:
            node.letters[chars[0]] = Node(chars[0])
            
        if len(chars) == 1:
            node.letters[chars[0]].isEnd = True
            return
        
        self.insertHelper(node.letters[chars[0]],chars[1:])
            
    def search(self, word: str) -> bool:
        
        return self.searchHelper(word,self.root)
    
    def searchHelper(self, word, node):
        
        if len(word)==0 or word[0] not in node.letters:
            return False
        
        elif len(word)==1:
            return node.letters[word[0]].isEnd
        
        return self.searchHelper(word[1:],node.letters[word[0]])

    def startsWith(self, prefix: str) -> bool:
        return self.startsWithHelper(list(prefix),self.root)
    
    def startsWithHelper(self,prefix,node):
        
        if len(prefix)==0:
            return True
        
        elif prefix[0] not in node.letters:
            return False
        
        return self.startsWithHelper(prefix[1:],node.letters[prefix[0]])
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)