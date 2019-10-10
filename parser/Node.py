class Node:

    def __init__(self):
        self.target = None
        self.children = []

    def root(self):
        return self

    def parse(self, context):
        pass

    def set_target(self, target):
        self.target = target

    def get_children(self):
        return self.children

