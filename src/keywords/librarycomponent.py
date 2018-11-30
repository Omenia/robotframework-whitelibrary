import clr
import os
clr.AddReference("TestStack.White")

class LibraryComponent(object):
    def __init__(self, state):
        self.state = state
