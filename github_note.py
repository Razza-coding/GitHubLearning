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

def lesson_3():
    lesson_msg = '''
    [ How to branch out a feature develop branch and merge back to main ]

    git checkout:
        Use git checkout to create or move into to a new branch for feature developing.
        We use "git checkout feature-1" as example.
        After this command, our branch will become feature-1

        Anything deveiop inside feature-1 branch is separate to the main branch, so you can try any wild idea here.

    git switch:
        Simple version of git checkout, only do branch switching, very safe to use.
    
    develop feature-1:
        Now we start changing code inside feature-1
        We'll add a init process and 2 item calls in feature-1
    
    develop main while feature-1 is also in development
        Use git checkout main to swith back to main branch.
        Now all the things we added and changed will disapear (cause we are back to main).
        Next, we shall add a part where feature-1 is gonna be called in main.
        In the mean time, we also optimize some of the main functions.
        remeber too commit after all the changes is done

        note:
            Calling feature-1 in main should be done in feature-1 branch, cause we dont want to break the main code
            But here we mimic the develop process of other poeple changing main, so we change the main process here.

    merge feature-1 into main after it's done
        First, update the "main" branch before doing any merging using git pull (from github)
        Next, we move to main branch using "git checkout main" to start our merging process.
        And then we call the merge command "git merge feature-1"
        
        What will happen?
            feature-1 and main have different main.py code. And only feature-1 have feature_1.py
            feature_1.py will merge in by auto merge process without a question.
            but there will be a confict at main.py
        Resolve confict:
            the message will show you 3 windows
            1. form feature-1 branch (incoming)
            2. from main branch (current)
            3. merge result

            There will be 3 options each section
            1. use the income code
            2. keep the current code
            3. merge both (auto gather code from both side with alot of difference)

            There's also a manual option, you can just edit int merge result window.
        
        After comform, you need to leave a message, just like commiting.
        And this is all.     
    '''
    print(lesson_msg)
    pass

def lesson_4():
    lesson_msg = '''
    [ How to reset merge and commit when we forgot to add something ] 

    We need to roll back to preivous commit to change the code, and then commit/merge it back using the same process.
    git reflog:
        Use git reflog to see the commit records, find the commit you want to go back
    
    git reset:
        Use git reset to roll back all the commit we did.
        For example "git reset --hard main@{3}", main@{3} denote the commit we want to roll back in the "git reflog" graph.
        The flage "--hard" means we will completely reset the commit, which includes following changes:
            1. HEAD move to main@{3}
            2. Stage will be cleared
            3. remove all the files that added after main@{3} commit
        Some other mode we can use:
            1. --soft: keeps Stage and Files
            2. --mixed: keeps Files only
    
    How to reset the "reset command"
        1. you can use git reflog to reset a reset operation
        2. you can see your log noted that HEAD@{A} moved to HEAD{B}
        3. just select the HEAD before you do the reset command, then you'll be fine
    '''
    print(lesson_msg)
    pass

def lesson_5():
    lesson_msg = '''
    [ How to check old commits and run old code ] 

    Entering detached HEAD:
        In this state, we are not in any branch
        Only checking previous commits
    
    How to enter old commits in detached mode:
        use "git checkout <commit-hash>" or "git switch --detach <commit-hash>" to select specfic commit
            
        How to find commit hash:
            use "git log --oneline"

    How to check if we are in detached HEAD:
        use "git status", it'll say "HEAD is detached at <commit-head>"
        using "git branch" will not display any branch

    Can we commit a detached HEAD:
        No, detached HEAD have no relationship with orignal project any more
        If you do a commit and create a branch, it is same as creating a new main branch for new project
    '''
    print(lesson_msg)
    pass