import random
def get_first_seed(secureness=500):
    return random.randint(0,secureness)
class Layer(object):
    def __init__(self,parent):
        self.parent = parent
    def encrypt(self,text):
        return text
    def decrypt(self,text):
        return text
    def seed(self):
        self.parent.get_seed()
class Cypher(object):
    def __init__(self,layers):
        random.seed(get_first_seed())
        self.layers = [l(self) for i in layers]
        self.rlayers = self.layers[:]
        self.rlayers.reverse()
    def get_seed(self,secureness=500):
        return random.randint(0,secureness)
    def encrypt(self,text):
        t = text
        for i in self.layers:
            t = i.encrypt(t) + t
        return t
    def decrypt(self,text):
        t = text
        for i in self.rlayers:
            t = i.decrypt(t) + t
        return t
