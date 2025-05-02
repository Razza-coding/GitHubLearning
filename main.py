import os
from feature.feature_1 import feature_1
from feature.feature_2 import feature_2
from feature.feature_3 import feature_3
from feature.feature_4 import feature_4

# main functions here
def main_init():
    print("1. this is a project about how to use github")
    pass

def main_process_1():
    print("2. calling feature-1 (branch out and merge back example)")

def main_process_2():
    print("3. feature-1 finished")

def main_process_3():
    print("4. calling feature-2 (multiple branch developing example)")

def main_process_4():
    print("5. feature-2 finished")

def main_process_5():
    print("6. calling feature-3 (multiple branch developing example)")

def main_process_6():
    print("7. feature-3 finished")

def main_process_7():
    print("8. feature-2 and feature-3 finished")

def main_process_8():
    print("9. calling feature-4")

def main_process_9():
    print("10. we just called feature-4")

# main program
if __name__ == "__main__":
    main_init()
    # feature-1
    main_process_1()
    feature_1()
    main_process_2()
    # feature-2
    main_process_3()
    feature_2()
    main_process_4()
    # feature-3
    main_process_5()
    feature_3()
    main_process_6()
    # end of feature-2 and feature-3
    main_process_7()
    # feature 1~3 message is updated
    # now feature 4 execute rebase
    
    pass