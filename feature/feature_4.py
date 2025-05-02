def feature_4():
    msg = '''
    This is feature-4 unit test.
    '''
    update_msg_1 = '''
    【feature 4】: init
    【feature 4】: read file B
    【feature 4】: update UI
    【feature 4】: write file B
    【feature 4】: end
    '''
    print(msg + update_msg_1)
    pass

if __name__ == "__main__":
    feature_4()