# lets a string is rafi-221003712 here find the name of studrnt and the id 

class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
    
string = "rafi-221003712"
std = student.fromstr(string)
print("Name:",std.name,", ID:",std.id)