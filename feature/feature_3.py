def feature_3():
    msg = '''
    This is feature-3 unit test.
    '''
    update_msg_1 = '''
    【feature 3】: init
    【feature 3】: read file B
    【feature 3】: update UI
    【feature 3】: write file B
    【feature 3】: end
    '''
    print(msg + update_msg_1)
    pass

if __name__ == "__main__":
    feature_3()