from abc import ABC, abstractmethod

class ChessPiece(ABC):

    def draw(self):
        print("Drew a chess piece")
    
    def colour(self):
        print("Orange")

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def length(self):
        print("none")


class Queen(ChessPiece):
    def move(self):
        print("Moved Queen to e2e4")
    
    def length(self):
        print("from 1 to 7")


class Horse(ChessPiece):
    def move(self):
        print("Moved Horse to a1b4")
    
    def length(self):
        print("2.24")
