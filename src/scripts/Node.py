
TERMINAL = 'TERMINAL'
FUNCTION = 'FUNCTION'


class Node:
   def __init__(self, data,  type: str):
        self.children = [Node]
        self.data = data
        self.type = type

    def PrintTree(self):
        print(self.data)
        for child in self.children:
            child.PrintTree()

    def insert(self, data, fatherId: int):
        if id(self) == fatherId:
            self.children.append(data)
        else:
            for child in self.children:
                self.insert(data, fatherId)

    def evaluate(self):
        # Recurtion cases
        # Base case 1
        # I am a terminal
        if self.type == 'TERMINAL':
            return
        # Base case 2
        # All my nodes are terminals
        hasFunctions = False
        for child in self.children:
            if child.type == FUNCTION:
                hasFunctions = True

        # Can evaluate now
        if hasFunctions == False:
            if self.data == '>=':
                return self.children[0].data >= self.children[1].data
            elif self.data == 'if':
                if self.children[0]:
                    return self.children[1].data
                else: 
                    return self.children[2].data
        else:
            for child in self.children:
                if type == FUNCTION:
                    return child.evaluate()
