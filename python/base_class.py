class base_class:

    def __init__(self):        
        pass

    def __del__(self):
        pass

    def flow_controller(self):
        # self.lesson_1()
        self.lesson_2()

    def lesson_1(self):
        print("Hello World")

    def lesson_2(self):
        somevalue=35
        if(somevalue<40):
            print("Fuck You")
        else:
            print("Fuck You Again")

def main():
    controller = base_class()
    controller.flow_controller()

if __name__ == "__main__": main()