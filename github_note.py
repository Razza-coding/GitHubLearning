def lesson_1():
    '''
    [ Difference between git add, git commit, git push ]

    git add:
        Save your added/modified files into "staged" zone
        Files saved in "staged" will be commit later
        Can select which file to add in "staged"
        Use "git status" to see all the current added/modified file

        You CAN NOT commit file isn't added inside "staged"

    git commit:
        Save you file add/modify records that is in "staged" into branch, commit will become a branch node
        You should type in all the change message when commit
        After commit, you can check update message using "git log --oneline"

    git push:
        update your code to remote side (GitHub)
    '''