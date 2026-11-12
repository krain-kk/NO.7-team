1.What is the purpose of git clone?
To copy a remote repository to the local machine, including all files and version history, so developers can work on it locally.
2. What is the difference between a Git repository and a Git branch?
A repository is the entire project database containing all files and history. A branch is an independent line of development within the repository, allowing changes without affecting the main codebase.
3. What does git switch -c add-discount do?
It creates a new branch named "add-discount" and immediately switches to it.
4. What is the purpose of git add?
To stage modified files to the staging area, preparing them to be included in the next commit
5. Why do we use git commit?
To save the staged changes permanently into the local version history with a descriptive message, creating a restore point.
6. What is the difference between git push and git pull?
'git push'uploads local commits to the remote repository. 'git pull' downloads the latest changes from the remote repository and merges them into the local branch.
7. What is a Pull Request?
A request to merge your branch into another branch (like main). It provides a platform for team members to review code, discuss changes, and approve the merge.
8. Why should developers review each other's code before merging?
To catch bugs early, ensure code meets project standards, share knowledge among team members, and prevent broken code from entering the main branch.
9. What could happen if two developers modify the same file simultaneously?
A merge conflict will occur. The developer who pushes later will be rejected and must pull the latest changes, manually resolve the conflict, and then commit again.
10. How does using Git branches improve collaboration in software development?
Branches allow developers to work on new features or fixes independently without affecting others' work. The main branch stays stable, and code is merged only after review and testing, improving safety and efficiency.
