import os
import github_note as note
from feature_1 import feature_1

# main functions here
def main_init():
    print("1. this is a project about how to use github")
    pass

def main_process_1():
    print("2. calling feature-1")

def main_process_2():
    print("3. we just called feature-1, which is branched and developed and will merge back later")

# main program
if __name__ == "__main__":
    main_init()
    main_process_1()
    feature_1()
    main_process_2()
    pass