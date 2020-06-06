class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.last = False

    def check_last_char(self):
        return self.last

    def print_children(self, char):
        for child in self.children[char]:
            return child

    def print(self):
        for child in self.children:
            print(child, end=" ")

    def get_children(self):
        return self.children


class Trie:
    def __init__(self):
        self.root = TrieNode('*')
        self.wordList = []

    def add(self, products):
        for words in products:
            node = self.root
            for char in words:
                if char not in node.children:
                    node.children[char] = TrieNode(char)
                print("node-chldren", end=" ")
                node.print()
                print("node character", node.char, "child", node.children[char].char)
                node = node.children[char]
                print("Children size", len(node.get_children()))
            print("lsts", node.char)
            node.last = True
            print("------scscscscscscscscscscscccs---------")

    def print(self):
        self.dfs(self.root, "")

    def dfs(self, node, prefix=""):
        if node.char is not '*':
            prefix += node.char
        for child in node.children:
            self.dfs(node.children[child], prefix)
        if node.last:
            print(prefix)
            return

    def serach(self, word):
        node = self.root
        for char in word:
            is_word_found = False
            if char in node.children:
                is_word_found = True
            else:
                return False
            node = node.children[char]
        if is_word_found and node.last:
            return True
        else:
            return False

    def serach_word(self, word):
        print(word)
        prev = ""
        result = []

        for char in word:
            list1 = []
            prev = prev + char
            print("------------previous value-------------", prev)
            self.autoSuggestion(self.root, list1, prev, "")
            result.append(list1)
            # print(result)

    def autoSuggestion(self, node, list1, char, prefix=""):
        if node.char is not '*':
            prefix += node.char
        for child in node.children:
            self.autoSuggestion(node.children[child], list1, char, prefix)
        if node.last:
            if prefix.startswith(char):
                list1.append(prefix)
                print(prefix)
                return


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
myObj = Trie()
myObj.add(products)
# myObj.print()
# print(myObj.serach("monepot"))

# find auto suggestion
myObj.serach_word("mouse")
