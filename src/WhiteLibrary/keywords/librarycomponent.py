import clr
clr.AddReference("TestStack.White")


class LibraryComponent(object):
    def __init__(self, state):
        self.state = state
