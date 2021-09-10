"""A lion"""
import animal
class Lion(animal.Animal):
    def __init__(self):
        self.kind = 'lion'
    def get_kind(self):
        return self.kind
