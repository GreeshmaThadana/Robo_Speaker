import os

if __name__ == '__main__':
    print("Welcome to robo speaker 1.1 created by Greesh")
    while(True):
        x = input("enter what you want to say: ")
        if x == "q":
            os.system("say 'bye bye friend, end of talking'")
            break
        command = f"Say {x}"
        os.system(command)
print("End of talking")