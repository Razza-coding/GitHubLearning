def feature_2():
    msg = '''
    This is feature-2 unit test.
    '''
    update_msg_1 = '''
    【feature 2】: init
    【feature 2】: read file A
    【feature 2】: run test
    【feature 2】: write file A
    【feature 2】: end
    '''
    print(msg + update_msg_1)

if __name__ == "__main__":
    feature_2()