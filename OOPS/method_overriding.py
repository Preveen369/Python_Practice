# method overriding (using inheritance) in PYTHON:

# the child class method's overrides (replaces) the parent class's methods
# when those method's has the same name: [using parent method / super()]

# IMP_NOTE => acc., to MRO (Method resolving order), the most recent 
# derived class method always replaces before existing methods, 
# if they share the same method name [IN OVERRIDING]

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Child(Parent):
    def __init__(self, name, age, college):
        # # accessing a parent class method using super class name:
        # Parent.__init__(self, name, age)
        # accessing a super class's method using super() method:
        super().__init__(name, age)
        self.college = college
    
p = Child("Preveen", 21, "VCET college")
