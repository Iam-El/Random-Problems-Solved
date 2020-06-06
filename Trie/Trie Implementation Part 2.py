class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.counter = 1  # to keep track of how many times character appeared
        self.word_finished = False  # to check if its a end of the word
        self.childrens={}

    def print_char(self):
        return self.char

    def print_children(self):
        for i in self.children:
            return (i.print_char())

    def add(self, word):
        print(word)
        node = self
        for char in word:
            is_child_found = False
            for child in node.children:
                # print(char, " and ", child.char)
                if child.char == char:
                    is_child_found = True
                    child.counter = child.counter + 1
                    node = child
                    break

            if is_child_found == False:
                childNode = TrieNode(char)
                node.children.append(childNode)
                # for i in node.children:
                #     print(i.print_char())
                node = childNode

        print(node.char)
        node.word_finished = True
        # print(node.word_finished)


    def serach(self, word):
        # print(word)
        node = self
        for char in word:
            is_char_found = False
            for child in node.children:
                if child.char == char:
                    is_char_found = True
                    node = child
                    break

            if is_char_found == False:
                return False
        return True

    def serach_exact_word(self, word):
        print(word)
        node = self
        for char in word:
            is_char_found = False
            for child in node.children:
                if child.char == char:
                    is_char_found = True
                    node = child
                    break
            if is_char_found == False:
                return False
        if is_char_found == True and node.word_finished == True:
            return True
        else:
            return False

    def print(self):
        node = self
        stack = [node]
        visited = []
        while len(stack) >= 1:
            current = stack.pop()
            if current not in visited:
                visited.append(current.char)
                for child in current.children:
                    stack.append(child)
        return visited

    # def serach_suggestion(self, word, res):
    #     node = self
    #     for char in word:
    #
    #         for child in node.children:
    #             if char == child.char:


# create a instance of the Trie data structure
root = TrieNode('*')
root.add("mobile")
root.add("mouse")
root.add("moneypot")
root.add("monitor")
root.add("mousepad")

# Print the trie data structure
print("Trie Data structure!!!!!!")
print(root.print())

# Check if the word mouse exists
# print(root.serach("money"))

# check if the exact word is present
# print(root.serach_exact_word("moneypot"))

# search suggestion system
# root.serach_suggestion("mouse", res=[])
