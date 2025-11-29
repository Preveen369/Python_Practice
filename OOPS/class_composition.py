# class compositions in PYTHON;

# the class comoposition is a concept where the members of one class
# are passed to the members of the other different classes
# makes the code more flexible and well organized

class Engine:
    def __init__(self):
        self.engine_name = "Qualcomm XSpeed"

    def start(self):
        print("The engine is starting...")

class Train:
    def __init__(self):
        # an instance(object) of another class is assigned as a
        # value to the current class's instance attribute 
        self.engine = Engine() 
    
    def move(self):
        print(f"Engine name is: {self.engine.engine_name}")
        self.engine.start()
        print("The train is moving now...")

expressTrain = Train()
expressTrain.move()