class calculation:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self,type,value,traceback):
        if type == None:
            print("exit")
        else:
            print("Error")
            return True
            

    def sum(self):
        return self.a + self.b
    
    def link(self):
        return int(str(self.a) + str(self.b))
    
    def test1(self):
        return self.link() + self.b
    
    def test2(self,x):
        return self.link() + x
    
    def test3(self,x):
        return self.a / x


if __name__ == "__main__":
    with calculation(2,3) as cal:
        print(cal.test3(1))
    print()
    with calculation(3,3) as cal:
        print(cal.test3(0))