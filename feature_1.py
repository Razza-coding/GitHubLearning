def feature_1():
    msg = '''
    This is feature-1 unit test.
    '''
    update_msg_1 = '''
    【feature 1】: init
    【feature 1】: call process-1
    【feature 1】: call process-2
    【feature 1】: end
    '''
    print(msg + update_msg_1)
    pass

if __name__ == "__main__":
    feature_1()