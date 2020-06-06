class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_finished = False  # to check if its a last characxter of the word
        self.counter = 1  # how many times this character apperared

    def get_char(self):
        print(self.char)

    def get_node(self):
        for i in self.children:
            print(i)


def add(root, word):
    node = root
    for char in word:
        # print(node.counter)
        found_in_child = False
        for child in node.children:
            # print("child+++++++++++++++++++char", child.char)
            # print("-------")
            # print("heregvggvgvgvgvgvgvgvgvgvgvgvg", char)
            if child.char == char:
                # print("gvgvgvgvgv")
                child.counter = child.counter + 1
                node = child
                found_in_child = True
                break
        #
        # print(found_in_child)
        # we did not find the word so add the new child
        if found_in_child == False:
            # print("chratacter", char)
            new_node = TrieNode(char)
            node.children.append(new_node)
            for i in node.children:
                i.get_char()
            # point the node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True


def search(root, str):
    node = root
    for char in str:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False

    return True


root = TrieNode('*')
add(root, "hackathon")
add(root, 'hack')
add(root, 'htck')

print(search(root, 'hacka'))
