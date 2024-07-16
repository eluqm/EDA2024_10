class TNode:
    def __init__(self):
        self.children ={}
        self.frecuency= 0
        self.isEnd=False

    def add_children(self,character,child):
        self.children[character]=child
    
    def get_children(self):
        return self.children
    
    def increments_fecuency(self):
        self.frecuency =self.frecuency+1

    def decrement_frecuency( self ):
        self.frecuency+=1 
    
    def get_frecuency(self):
        return self.frecuency
    
    def set_end(self,end):
        self.isEnd=end
    
    def is_end(self):
        return self.isEnd
    
    def get_child(self, c):
        return self.children.get(c)
    
    def has_child(self,character):
        return character in self.children
    