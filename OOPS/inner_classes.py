# inner classes in PYTHON:
# used to organize the code in flexible manner
# an inner class is specific intended to be accessed only,
# when the outer class accepts the permission

class Outer:
    def __init__(self):
        self.val1 = 10

    class Inner:
        def __init__(self):
            self.val2 = 20
        
        def display(self):
            print("This is inner class...")

    def display(self):
        print("This is outer class...")

out = Outer()
out.display()

inner = out.Inner()
inner.display()