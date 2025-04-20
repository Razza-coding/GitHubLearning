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


def lesson_6():
    lesson_msg = '''
    [ How to ignore trash/cache/personal files ] 

    create a ".gitignore" file to list all the unwanted files/folders
    for example:
        __pycache__/
        *.pyc
        .env
        logs/
        outputs/
        keys/

    ".gitignore" only effect the files that is not track
    if we accidently add unwanted files in git history, remove it

    How to remove file/folder tracking:
        use "git rm --cached <file or folder>" to remove traching, and then commit the remove action
        after removing it, ".gitignore" will effect the files
    '''
    print(lesson_msg)
    pass

def lesson_7():
    lesson_msg = '''
    [ How to merge multiple features ] 

    Lets say we have "feature-2" and "feature-3" need to be add in project
    And main branch will be developing during the feature development process, we'll call it "main-org" and "main-updated" as different commits of main branch
    
    1. Branch out from main-org
        We do not want to update main branch, it should be a stable version of our project
        We'll start with creating 2 branches, that is feature-2 and feature-3
        Different features will be develop in seprate branches, merge comflict will be handled later

    2. Develop feature-2 and feature-3
        Add whatever we feature want
        Main.py, feature_2.py,  feature_3.py is expected to be modified/created
        Merge conflict might occur in main.py, but we'll try to complete new feature 1st
    
    3. Merge main-updated to feature-2 and feature-3 branches seperately
        Some bus fix is commited while we develop features
        We should try to merge main-updated into feature-2 and feature-3 first, handle the conflict from main 1st

        DO NOT merge feature-2 and feature-3 before merging main-updated, this will create more conflict

    4. Create a branch for merging feature-2 and feature-3
        We assume feature-2 and feature-3 have merged main-updated and completed their developments
        Create a new branch to merge feature-2 and feature-3 now, we'll use feature-2 to create a new branch

        This is where we handle most conflict between feature-2 and feature-3
        Conflict example:
            Different Main process
            Same function name with different usage
            Same or similar variable names
            Comments
        
        We can try to run the code during merging, and then complete the merge
        Make sure feature will work after merging, and then we optimize the code in this branch
            
    5. Merge feature-2-3 into main branch
        After merging feature-2 and feature-3, it's time to merge into main
        Switch to main branch and merge feature-2-3, we should have no problem merging since we already update changes from "main-updated"
    '''
    print(lesson_msg)
    pass

def lesson_8():
    lesson_msg = '''
    [ How to restore changes ] 

    Use "git restore" to restore file changes
    "git restore"          : restore your files/code to last commit, but staged files will not change
    "git restore --staged" : restore your staged files, but files/code will not change

    If we want restore both "staged files" and current files, we should run both commands
    '''
    print(lesson_msg)
    pass

def lesson_9():
    lesson_msg = '''
    [ How to Read Commit Messages ]

    Use `git show <hash>` to display commit details.

    (Basic Information):
        Unique ID   : Commit SHA string
        Merge       : Shows which two commits were merged
        Author      : Person who made the commit
        Date        : Timestamp of the commit
        Commit Msg  : Message below the Date line

    (Merge Diff Header):
        a/main.py   : File before the merge (base/original)
        b/main.py   : File after the merge (result)

    (Merge Details - Diff Section):
        Example     : @@@ -1,7 -1,7 +1,8 @@@
        @@@         : Indicates a diff block (merge conflict hunk)
        -1,7 (left) : Left-side parent range (start line and line count)
        -1,7 (right): Right-side parent range
        +1,8        : Resulting merged block (start line and line count)

    (Merge Symbols):
        +           : Line added in the result
        -           : Line removed from the original
        ++          : Line added from one of the branches during merge
        --          : Line removed from one of the branches during merge
        +++         : Multiple lines added (visual emphasis)
        ---         : Multiple lines deleted (visual emphasis)
    '''
    print(lesson_msg)
    pass

def lesson_10():
    lesson_msg = '''
    [ How Add Version Tags ]

    Use `git tag <tag> <hash>` to add version tags.
    git tag v1.0 abc1234 means commit abc1234 has been tag as v1.0

    View all tags in commits:
        git tag
    
    Show commit message bt tag:
        git show <tag>

    Remove a tag from commit
        git tag -d <tag>

    Note that we can not delete commit by using tags
    '''
    print(lesson_msg)
    pass

def lesson_11():
    lesson_msg = '''
    [ How Search Keyword In any Commit ]

    Use `git grep <keyword> <tag/hash/HEAD@>` to serach for key word in specfic commit
    When using `git grep` without targeting commit, git use current commit

    git grep supports regular expression, for example:
        git grep "How to.*merge.*"
    '''
    print(lesson_msg)
    pass

def lesson_12():
    lesson_msg = '''
    [ Binary Search For Bug Searching ]

    "git bisect" is a test tool that searches the first broken commits within multiple commits

    Core usage:
    1. Enter bisect mode
        - "git bisect start"
    2. Set a commit search range, noted good and bad commit
        - "git bisect bad <hash>"
        - "git bisect good <hash>"
        - note that bad hash must be "newer" and "smae branch" version of good hash
    3. Make a test script
        - sh py exe ps1 cmd, anything that can send return code
    4. Run bisect testing
        - "git bisect run <script>"
        - Start from good commit to bad commit in order
        - It'll return the 1st result that failed the test, which means the commit that breaks the code
    5. Display result
        - "git bisect log"
        - "git bisect visualize"
    '''
    print(lesson_msg)
    pass

def lesson_13():
    lesson_msg = '''
    [ Moving Or Rename Files ]

    Use "git mv <orignal file> <new path or name>" to change file location or name

    Why not just move the file?
        - git will track as adding a file and deleting a file
        - git mv can label file as "renamed:"
        - but mv from system will not be consider moved by git
    
    What if I combine with git add?
        - using "git add ." will not overwrite record from "git mv"
        - save to use together
    '''
    print(lesson_msg)
    pass

def lesson_14():
    lesson_msg = '''
    [ Checkout Part of the Project Files ]

    Sparse Checkout is similar to Clone, but ont copy and track part of the project

    Use "git sparse-checkout set <part of project folder>" to clone one part of project
    Development is the same as using git clone, add, commit, push

    If we need FULL project files when we are in sparse checkout, we can still get full project
    Using "git sparse-checkout disable"

    A switch tool between Full mode and Sparse mode
    '''
    print(lesson_msg)
    pass