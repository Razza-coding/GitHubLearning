import os
import github_note as note
from feature_1 import feature_1
from feature_2 import feature_2
from feature_3 import feature_3

# main functions here
def main_init():
    print("1. this is a project about how to use github")
    pass

def main_process_1():
    print("2. calling feature-1")

def main_process_2():
    print("3. we just called feature-1, which is branched and developed and will merge back later")

def main_process_3():
    print("4. calling feature-2")

def main_process_4():
    print("5. we just called feature-2")

def main_process_5():
    print("6. calling feature-3")

def main_process_6():
    print("7. we just called feature-3, UI is updated")

def main_process_7():
    print("8. feature-2 and feature-3 ended")

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
    
    pass