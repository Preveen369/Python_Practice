# classes and methods in PYTHON:
# types of methods:
# 1. instance methods
# 2. static methods
# 3. class methods

class College:
    college_name = "VCET College"
    place = "Viraganoor"
    pincode = 625009

    def __init__(self, rollno, name, dept, phone):
        self.rollno = rollno
        self.name = name
        self.dept = dept
        self.phone = phone

    # this is an instance method: used to operate on instances, 
    # recieves self(current instance) arg by default(implicit)
    def display(self):
        print(f"student {self.rollno} details => {self.name}, {self.dept}, {self.phone}")

    # this is a class method: used to operate on classes (not instances), 
    # recieves class arg by default(implicit) similar to instance methods
    @classmethod
    def getCollegeDetails(cls):
        return [cls.college_name, cls.place, cls.pincode]
    
    # this is a static method: used to operate neither on classes nor instances
    # they are not passed implicitly as the first argument to the method.
    @staticmethod
    def eligiblityCheck(grade):
        return "PASS" if (grade >= 7.0) else "FAIL"
    

stud1 = College(1, "Preveen S", "IT", 9488960369)
stud1.display() # or else, College.display(stud1)
details = College.getCollegeDetails()
print(details , "\n")  # display the value of classmethod

stud2 = College(2, "Praneshwar MB", "CSE", 9488970707)
stud2.display()
details = College.getCollegeDetails()
print(details , "\n")

gradeResult = College.eligiblityCheck(8.0)
print(f"eligibility status: {gradeResult}")