class base_class:

    def __init__(self):        
        pass

    def __del__(self):
        pass

    def flow_controller(self):
        ### Comment and uncomment the following lines to execute the examples
        self.hello_world()
        self.if_example()
        self.if_else_ample()
        self.if_elif_example()
        self.for_loop_with_integers_example()
        self.for_loop_with_strings_example()
        self.while_do_loop_example()

    def hello_world(self):
        print("Hello Python World")

    def if_example(self):
        #play with the value of variable "somevalue" to see the other code path execute
        somevalue=35
        if(somevalue<40):
            print("Fuck You 1")

    def if_else_ample(self):
        #play with the value of variable "somevalue" to see the other code path execute
        somevalue=35
        if(somevalue<40):
            print("Fuck You 2")
        else:
            print("Fuck You Again 3")

    def if_elif_example(self):
        #play with the value of variable "somevalue" to see the other code path execute
        somevalue=70
        if(somevalue<69):
            print("Fuck You 5")
        elif(somevalue>69):
            print("Fuck You Again 6")

    def for_loop_with_integers_example(self):
        #print a santa greating
        for x in range(0,3):
            print("Ho!")

    def for_loop_with_strings_example(self):
        #print a bad santa greating
        santa_talk =["Santa","likes","his","hoes!"]
        for x in santa_talk:
            print(x)

    def while_do_loop_example(self):
        #print a bad santa greating
        x = 0
        while x<3:
            print("Hoe!")
            x+=1


def main():
    controller = base_class()
    controller.flow_controller()

if __name__ == "__main__": main()