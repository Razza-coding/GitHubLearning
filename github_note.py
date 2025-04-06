def lesson_1():
    lesson_msg = '''
    [ Difference between git add, git commit, git push ]

    git add:
        Save your added/modified files into "staged" zone
        Files saved in "staged" will be commit later
        Can select which file to add in "staged"
        Use "git status" to see all the current added/modified file
        If git add is called twice, only the latest version will be saved in "staged"

        You CAN NOT commit file isn't added inside "staged"

    git commit:
        Save you file add/modify records that is in "staged" into branch, commit will become a branch node
        You should type in all the change message when commit
        After commit, you can check update message using "git log --oneline"

    git push:
        update your code to remote side (GitHub)
    '''
    print(lesson_msg)
    pass

def lesson_2():
    lesson_msg = '''
    [ Difference between git status, git log, git branch ]

    git status:
        Check current status of: modified file, branch version between local and remote, what is file not added/commited
        Very useful before Add/Commit/Push/Branch Change, basicly the one command check before doing anything
    
    git log:
        Shows your commit message.
        git log itself is very long, remeber to add --oneline for simplify message.

    git branch:
        Shows what branch we currently have, both locally and remotely.
        This helps you delete unused and trash branch.
        "note to self, add in what will happen if you branch out a feature and merge back in"
    '''
    print(lesson_msg)
    pass