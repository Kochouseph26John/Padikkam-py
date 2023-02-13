class student:
    def __init__(self,name,branch,year:int,mark:int):
        self.name = name
        self.branch = branch
        self.year = year
        self.mark=mark
    def set_mark(self,mark: int):
        self.mark = mark
        print("Mark Updated")
    def get_mark(self):
        return self.mark
    def display(self):
        print("Name :", self.name)
        print("Branch :", self.branch)
        print("Year :", self.year)
        print("Mark :", self.mark)