# LESSON 2: Branching and remote operations

<!-- This is a summary of the lecture notes for this lesson.
The original list of commands has been edited and decorated with headings corresponding to the [lessons in the curriculum](course-units) more clearly. 
Some commands have been either removed or relocated or added for clarity and help self-study after the lesson.
Accidental errors have been removed, but intended errors have been kept.

The comments after each line are annotations on whether a command/option appears for the first time (**new**) or is a **known action**. 
Else, the annotation recalls why we typed that certain command, for example to **observe** the state of the play (typically before a certain change) or to **verify** the results of a change.
**routine** commands are the typical commit sequence learned in Lesson 1.

The original list of commands is available at this commit [as displayed by GitHub](https://github.com/4TUResearchData-Carpentries/workshop_notes/blob/056617efa8abb7d79ffb3e85b3ac8dbbcaed50e6/Lesson2.md). -->

<!-- ````{note}
The list of commands below has been grouped arbitrarily for readability's sake.
```` -->
---


## Learning objectives:

:::{card} Learning Objectives:

* Understand the concept of **branches** in Git repositories.
* Apply Git operations to **create** and **merge** branches in a local Git repository.
* Understand the concepts of **bare** and **remote** Git repositories.
* **Clone** and **push** changes to remote Git repositories.
* **Synchronise** changes between local and remote Git repositories.

+++
Materials:

<!-- * No additional materials related to the lesson for the instructor is expected.  -->
* Slides for the introduction of concepts is *desired but not mandatory*.
:::



---


:::{admonition} Instructor's Note 
:class: tip
<!-- 1. The instructor should start with a recap from lesson lesson 1 and introduce lesson 2.  -->
- The following *tasks* are expected from the instructor:

1. *Confirm the participants have Git correctly setup from lesson 1*
2. *Ensure everyone has configured a repository for lesson 1*
3. *Ask participants for question related to lesson 1*

If times allow, explain:
4. *The schedule of the lesson 2*
5. *The [**topics**](https://manugil.github.io/GitCoDev/curriculum.html) fot the lesson 2*
:::





<!-- ### Schedule
| 13:00  | 13:50 | 14:00 | 14:50 | 15:10 | 16:00 | 16:10 | 17:00 | 17:10 |
|:-------|:------|:------|:------|:------|:------|:------|:------|:------|
| Teaching 50' | **Break 10'** | Teaching 50' | **Break 20'** | Teaching 50' | **Break 10'** | Teaching  50'| **Wrap-up 10'** | Closure | -->


<!-- 
| Episode | Topic | Time |
|:----|:----|:----|
| **2.1** | **Branching** | **13:00**| 
| --- | Create, rename, change, and delete branches | -|
| --- | Develop and compare branches | -|
| --- | Visualise and merge branches and resolve conflicts |-| 
| **2.2** | **Operations with remotes** | **15:00**|
| --- | Create a bare repositories |-|
| --- | Cloning and pushing to upstreams |-|
| --- | Syncing changes between repositories |-| -->

:::{admonition} Instructor's Note 
:class: tip
For *steps 1 and 2* from previous Instructor's Note, the following actions may help you with the setup of the lesson:

- First let’s make sure we’re still in the right directory. You should be in the `root` directory with `Lines.txt` and `history.log` files. Remember that the branch we are located in `main*`. Note that you might need to change the default branch to be called `main`. This might be the default branch depending on your settings and version of git.

- Second, you should be able to illustrate hoe the working directory looks like in your terminal with the following steps:

```shell
git status
```

Output:
```csharp
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   directory/donttrackme.txt
	new file:   directory/emptyfile
```

```shell
ls
```

Output:
```csharp
Lines.txt   directory   history.log new.txt
```

We can remove folder `directory` and `new.txt`

```shell
rm -rf 2024-gitcodev
```

```shell
rm -r directory/
```
or

```shell
git rm --cached directory/donttrackme.txt
git rm --cached directory/emptyfile
```
or update `.gitignore` file.

Other possible Output:

```csharp
Lines.txt   history.log
```

The `Lines.txt` should contains the following lines:

```csharp
❯ cat Lines.txt 
first line
second line
third line
fourth line
twas brillig and the slithy toves
did gyre and gimble
seventh
eigth line
```

<!-- **Note:** For this lesson, we will use **main** as the primary branch name instead of **master**. All commands, outputs, and instructions referring to the primary branch are intended to use **main**. Please ensure your repository is configured accordingly. -->
:::

## Episode 1: Understanding Branches

<!-- **Objetive**: Introduce basic branch operations and concepts -->

:::{admonition} Instructor's Note 
:class: tip
1. Ask what they understand about Branches in Git
2. Explain in a nushell what are Branches in Git
3. Memorise the new commands and the Branch where the instructor is `main*`
:::



### 2.1.1 Create, rename, change and delete branches


```shell
git branch                     # new command for checking the branches (output: *main)
git branch B1                  # new argument (create new branch)
git branch                     # verify (output: B1, *main)
```
Your newly created branch (here, `B1`) will show up, but your active branch should still be `main`. Note that `B1` is just a name. You could also call your branch ``delft``, if you want.


:::{admonition} Instructor's Note 
:class: tip
A question from students may arise: *Lowercase matters?* 

- While it's essential to provide enough information for clarity, overly long branch names can become cumbersome and difficult to manage. Lowercase and dashes: Stick to lowercase letters and use dashes instead of spaces in branch names to ensure compatibility across different operating systems and Git hosting platforms. [Show the best practices for naming Git branches](https://graphite.dev/guides/git-branch-naming-conventions). 

- You can explain the key reason for using `branches` in the whiteboard or with the following image:


```{figure} ../img/git-branches.png
---
height: 400px
name: approach-fig
---
[A successful Git branching model, article from 2010](https://nvie.com/posts/a-successful-git-branching-model/)
```
:::

```shell
git status                     # verify (output: On branch main - nothing to commit, working tree clean)
cat Lines.txt                  # verify (ouptut: Lines.txt with eighth line)
```

<!-- ![](https://cdn.vectorstock.com/i/1000v/32/97/colorful-tree-with-leafy-branches-vector-13883297.jpg) -->

<!-- * **Lets first explain the following:**
- **What are branches?**
<!-- <div style="text-align: center;"> <img src="https://book.the-turing-way.org/_images/sub-branch.png" alt="Branches"> <p><strong>Figure 1:</strong> Branches in version control</p> </div> -->



<!-- - **what are the most common `git branch` flags?** -->

Lets explore in our terminal with `git branch --help`:

---
* `-r` or `--remote`: Lists only remote branches.
* `-d` or `--delete`: Deletes a specified branch. For example, `git branch -d B1`.
* `-D` or `--force`: Force deletes a branch, even if it has unmerged changes.
* `-m` or `--move`: Renames a branch. For example, `git branch -m old-branch new-branch`.
* `-c` or `--copy`: Creates a new branch by copying an existing branch. For example, `git branch -c existing-branch new-branch`.
* `-v` or `--verbose`: Shows more information when listing branches, including the last commit message.
---

```shell
git branch -m B1 B2            # new short option (rename B1 to B2)
git log --oneline              # verify (notice that B1 is renamed to B2)
```
Now its time to explain the output of `git log --online`

```csharp
c0ebedd (HEAD -> main, b2) Eighth line
c1eb703 (tag: tag1) seventh line
3005e3d Jabberwocky line 2
965e44f Modified Lines.txt
c165327 Adding .gitignore
0e77df2 Add first four lines
```

:::{admonition} Instructor's Note 
:class: tip
The following *points* maybe useful to discuss with students from the previous output:
1. *Commit Hashed:* each commit has a unique identifier. The abbreviated form (first 7 characters) is usually sufficient for referencing commits in commands.
2. *Branches (`main`, `b2`):* Branches are pointers to specific commits. In our case, `main` and `b2` are pointing to the latest commit `c0ebedd`
3. *Tags (`tag1`):* Tags are used to mark specific commits, often for releases or significant milestons.
4. *`HEAD`:* `HEAD` is a special pointer that indicates your current position in the repository. It points to the latest commit in the currently branch (`main` in this case)
5. *Commit Messages:* These are descriptions provided when making commits to explain what changes were made. Good commit messages are essential for understanding the history and purpose of changes.
:::
<!-- 
1. `c0ebedd (HEAD -> master, b2) Eighth line`

`c0ebedd`:
- Description: This is the abbreviated commit hash. Every commit in Git has a unique SHA-1 hash, and Git typically displays the first 7 characters for brevity.
`(HEAD -> master, b2)`:
- `HEAD`: Points to your current checked-out commit. It's a reference to the latest commit in your working directory.
- `master`: Indicates that this commit is the tip of the master branch.
- `b2`: Shows that another branch named b2 is also pointing to this commit.
- `Eighth line`:Commit Message: A brief description of the changes introduced in this commit.

> This is the latest commit in your repository. The `HEAD` is pointing to the `master` branch, and both `master` and `b2` branches are referencing this commit. The commit message is "`Eighth line`".

2. `c1eb703 (tag: tag1) seventh line`

- `c1eb703`: abbreviated commit Hash
- `(tag:tag1)`:
  * indicates that this commit is tagged with `tag1`. Tags are typically used to mark specific points in history as important, such as releases.
- `seventh line`: commit message

> Interpretation: This commit is the second most recent and has been marked with the tag tag1. The commit message is "seventh line".

3. `3005e3d Jabberwocky line 2`
- 3005e3d: Abbreviated Commit Hash.
- No References: This commit isn't currently pointed to by any branch or tag.
- Jabberwocky line 2: Commit Message.

> Interpretation: This is an older commit with the message "Jabberwocky line 2". It isn't associated with any specific branch or tag. -->

Once a branch has created and its not longer needed, it can be deleted. Removing branches that are no longer active helps maintain a clean and manageable branch structure. To delete a branch, you can use the `git branch` command, followed by a `-d` flag:


```shell
git branch -d B2               # new short option (output: Deleted branch B2 (was 8f14e06).)
git log --oneline              # verify (notice that main is the only branch available)
git branch -m main foo       # known action (rename "main" to "foo" branch)
```

:::{admonition} Instructor's Note 
:class: tip

A question from students may arise: *is kind of best practices modifying `main` branch name?*

- If there is a specific organizational reason, renaming the `main` branch is a good practice as long as it is done thoughtfully with clear communication and updates to all reserch infrastructure and systems, following internal convetions and widely adopted practices within the community. However, if the repository is already well-established and widely used with the `main` branch name, the impact of renaming might outweigh the benefits. [Show the best practices for naming Git branches](https://graphite.dev/guides/git-branch-naming-conventions).*
:::


```shell
git log --oneline              # verify
git branch -d foo              # known action (fails)
```
This should output similar to:

```shell
error: Cannot delete branch 'foo' checked out at '/Users/courses/gitcodev/2310-gitcodev/git/lesson2'
```
In Git, every repository has a current branch that your working directory is using. This is known as the checked-out branch. The **error** you're encountering means that Git is preventing you from deleting the branch you're currently on. This happens because:

1. Git needs an active branch to track changes. If you delete the current branch, there would be no branch left for Git to refer to in the working directory.
2. To prevent you from accidentally removing the branch where your work is happening, Git won’t allow you to delete the branch you are currently on.


```shell
git branch -m foo main         # known action (replace "foo" to "main")
git branch                     # verify
```


:::{admonition} Instructor's Note 
:class: tip
Few recommendations to discuss and recap with students:
- Checked-out branch: The branch you're currently working on.
- You can’t delete the branch you’re on because Git needs to keep a reference to your working directory.
- You must always specify the target branch when using `git switch`. Without a branch name or commit hash, Git doesn’t know what to switch to, hence the error.
- `git switch` is a modern alternative to the older git `checkout` for branch operations, and it's more intuitive for switching branches.
:::


```shell
git status                     # verify
git log --oneline              # verify
git branch B1                  # known action (create again new branch B1)
git branch                     # verify
git log --oneline              # verify
```
Lets now change branches with `git switch` git command.

```shell
git switch                     # new commmand (fails - fatal: missing branch or commit argument)
```

```shell
git switch B1                  # new argument: on branch B1
```
Possible Output:

```csharp
A	directory/donttrackme.txt
A	directory/emptyfile
Switched to branch 'b1'
```

:::{admonition} Instructor's Note 
:class: tip
Understanding the `A`:

- The letter `A` stands for *"Added"*. This indicates that these files have been added to the staging area (also known as the **index**) in Git. The staging area is where you prepare changes before committing them to the repository.
:::

Removing Tracking from `B1`:

```shell
git rm --cached directory/dontrackme.txt
git rm --cached directory/emptyfile
```

```shell
git log --oneline              # verify
git branch B2                  # known action
git log --oneline              # verify
```
```shell
git switch B2                  # known action: on branch B2
git log --oneline              # verify
git switch main                # known action: on branch main
git log --oneline              # verify
```

<!-- ![alt text](image-1.png) -->

:::{card} 
Exercise 1 --- Get familiar with branches
^^^    

```{include} exercises/L2-ex01.md
```

```{dropdown} Answers

```shell
git branch
# verify
git branch -d B1 B2
# known action
git branch
# verify
git log --oneline
# verify
cat Lines.txt
# verify
```
:::


### 2.1.2 Develop and compare branches


After the exercise, lets create the following actions in git:

```shell
git status                                                      # observe (nothing to commit, working tree clean)
git branch B1                                                   # known action
git branch B2                                                   # known action
git branch                                                      # on branch main
git status                                                      # routine with git status
```
```shell
echo 'ninth line' >>Lines.txt                                   # routine with git status
git status                                                      # routine with git status
git add Lines.txt                                               # routine with git status
git status                                                      # routine with git status
```
The output you should get is as following:
```shell
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   Lines.txt

no changes added to commit (use "git add" and/or "git commit -a")
```


:::{admonition} Instructor's Note 
:class: tip
- `On branch main`: This indicates that you are currently on the `main` branch.
- `Changes not staged for commit`: This section lists the changes that have been made to the files in your working directory but have not yet been staged for commit.
- `(use "git add <file>..." to update what will be committed)`: This message suggests that you can use the git add <file> command to stage the changes in the specified file(s) for the next commit.
- `(use "git restore <file>..." to discard changes in working directory)`: This message suggests that you can use the git restore <file> command to discard the changes in the specified file(s) and revert them to the last committed state.
- `modified: Lines.txt`: This indicates that the file Lines.txt has been modified but the changes have not been staged for commit.
- `no changes added to commit (use "git add" and/or "git commit -a")`: This message indicates that there are no changes currently staged for commit. It suggests using git add to stage changes or git commit -a to automatically stage and commit all changes to tracked files.
:::


<!-- **Possible question: what means "stage" the changes in a file?**
In Git, "staging the changes" refers to the process of preparing specific changes to be included in the next commit. It’s a way to organize your work before making a permanent snapshot (a commit) of your changes in the repository. Once staged, the changes are ready to be included in the next commit, which is then recorded in the Git repository. -->



```shell
git commit -m 'Add ninth line on main' Lines.txt                # output: [main 0e85a39] added ninth line  1 file changed, 1 insertion(+)
```
```shell
git status                                                      # output: On branch main nothing to commit, working tree clean
git log --oneline                                               # verify
git status                                                      # verify
```

Lets go back to branch B1:

```shell
git switch B1                                                   # on branch B1
git status                                                      # verify (nothing to commit, working tree clean)
```
```shell
git log --oneline                                               # verify
git log --oneline --all                                         # new long option
cat Lines.txt                                                   # verify
```
The output of `Lines.txt` should display:
```shell
first line
second line
third line
fourth line
sixth line
seventh line
eighth line
```
Lets add the *ninth line* on the `Lines.txt`:
```shell
git status                                                      # routine with git status
echo 'ninth line' >>Lines.txt                                   # routine with git status
```

```shell
git status                                                      # routine with git status
git add Lines.txt                                               # routine with git status
git status                                                      # routine with git status
git commit -m 'Add ninth line on B1' Lines.txt                  # routine with git status
git status                                                      # routine with git status
```
```shell
git log --oneline                                               # verify
git log --oneline --all                                         # verify
git log --oneline --all --parents                               # new long option
```


Now, we switch to the `main` branch:

```shell
git switch main                                                 # on branch main
git log --oneline --all                                         # verify
```

The output of the `git log --oneline --all` command provides a concise view of the commit history across all branches in your Git repository. Let’s break down what each part of the following output means:

```csharp
b90bce0 (b1) add ninth line on B1
f6ef1b3 (HEAD -> main) add ninth line on main
```
<!-- 
**1. Commit Hash (b90bce0 and f6ef1b3)**
Each commit in Git has a unique identifier called commit hash (also known as a SHA-1 hash). In this case:
- `b90bce0` is the hash of one commit.
- `f6ef1b3` is the hash of another commit.

**2. Branch Name ((b1) and (HEAD -> main)**
The text in parentheses indicates which branch or branches point to a particular commit:
- `(b1)`: means that the branch `b1` is pointing to the commit with hash `b90ce0`. In other words, the most recent commit on branch `b1` is `b90bce0`.
- `(HEAD -> main)` indicates that `HEAD` (which refers to the current active branch) is pointing to the `main` branch, and the latest commit on the `main` branch is `f6ef1b3`.

**3.Commit Message (`add ninth line on B1` and `add ninth line on main`**
- After the commit hash and branch information, you see the **commit message**, which describes what changes were made in that commit:
  * The commit `b90bce0` on branch `b1` has the message **"add ninth line on B1"**
  * The commit `f6ef1b3` on branch `main` has the message **"add nitnth line on main"**

**4. HEAD (`HEAD -> main`)**
- `HEAD` refers to the currently branch you are working on "checked-out"
- `HEAD -> main` means that the `main` branch is currently checked out, and you are working on this branch -->

This output suggests that the branches `b1` and `main` both have separate commits, and the HEAD is currently pointing to the main branch.

```csharp
  b1                main (HEAD)
  |                  |
b90bce0           f6ef1b3
(add ninth       (add ninth
 line on B1)      line on main)
```
In this case, the commit on `b1` differs from the commit on `main`, even though both commits have similar descriptions.

Lets suppose we added a new line by mistake:
```shell
echo 'ninth line (duplicate)' >> Lines.txt                      # routine (an intended mistake)
git add Lines.txt                                               # routine
git commit -m 'Add tenth line on main (with mistake)' Lines.txt # routine
cat Lines.txt                                                   # verify
```
The following output should be displayed:
```shell
❯ cat Lines.txt 
first line
second line
third line
fourth line
sixth line
seventh line
eighth line
ninth line
ninth line(duplicate)
```

### 2.1.3 Visualise and merge branches, and conflict resolution


:::{admonition} Instructor's Note 
:class: tip
The objectives of this section is to:
- Show participants how to identify what has been changed in a file between commits.
- Explain the meaning of each part of the diff output, including how to interpret the context of changes.
- Teach participants how to merge branches and handle conflicts.
:::


Git also offers an option for  visualization of branches inside the command line. For that you can use `git log` (introduced in the previous chapter on Git Essentials) with four flags:

```shell
git log --oneline --all                                # explore
git log --oneline --all --parents                      # explore
git log --oneline --all --parents --graph              # explore
```
<!-- 
1. `git log --oneline --all:`

- `--oneline`: Displays each commit in a condensed format (one line per commit) with the commit hash and message.
- `--all`: Shows the commit history of all branches in the repository, not just the currently checked-out branch.

2. `git log --oneline --all --parents --graph`:

- `--oneline`: Same as before, showing each commit in one line.
- `--all`: Shows commits from all branches.
- `--parents`: Displays the parent commit hashes for each commit. This is especially useful for merge commits, as it shows which commits were merged.
- `--graph`: Adds a visual representation of the commit history, including branches and merges. The history is displayed as a graph of lines and characters (like `|`, `/`, and `*`) to represent the structure of branches and merges. -->

Below is the output: 

```csharp
* c5d261c 9122e5b (HEAD -> main) add tenth line on main (with mistake)
* 9122e5b c0ebedd add ninth line on main
| * 3730df7 c0ebedd (b1) added ninth line on B1
|/  
* c0ebedd c1eb703 (b2) Eighth line
* c1eb703 3005e3d (tag: tag1) seventh line
* 3005e3d 965e44f Jabberwocky line 2
* 965e44f c165327 Modified Lines.txt
* c165327 0e77df2 Adding .gitignore
* 0e77df2 Add first four lines
```

The graph shows a branching history with a divergence between `main` and `b1` at commit `c0ebedd`. 
`HEAD -> main` indicates that you are currently on the main branch, and this is the latest commit in the repository.
 The tags and branch names are helpful for identifying important commits or points in the history (like tag1). 
 Merge points and relationships between branches are clearly shown using the `|` (vertical bar), `/`, and `*` symbols.

<!-- What each part means:
**Breaking Down the Output:**

**Commit Structure**:
- Each line represents a commit.
- The commit hash (e.g., c5d261c) is followed by its parent commit(s) (e.g., 9122e5b).
- The text following the hashes is the commit message (e.g., "add tenth line on main (with mistake)").

**Branches and HEAD**:
- The current branch is marked with HEAD -> main, indicating that the HEAD pointer is currently at the tip of the main branch.
- The branch b1 is also shown with the commit 3730df7.

**Tag**:
- The commit c1eb703 is tagged with tag1, indicating a saved point in the repository's history.

**Graph Representation**:
- The graph (*, |, /) represents the relationships between commits.
- The * represents a commit point.
- The | represents a vertical continuation of a branch.
- The / represents a merge point or a branch that is not currently part of the HEAD.

**Interpreting the Specific Output:**
1. Commit `c5d261c`:
- This is the most recent commit on the main branch (HEAD -> main).
- It has the message "add tenth line on main (with mistake)".
- Its parent commit is 9122e5b.

2. Commit `9122e5b`:
- This commit is on the main branch with the message "add ninth line on main".
- It shares the parent commit c0ebedd with another branch (b1), indicating that the branches main and b1 diverged after this commit.

3. Commit `3730df7 (branch b1)`:
- This commit is on the branch b1, which has the message "added ninth line on B1".
- It shares the same parent commit as main at c0ebedd, showing that both branches have a common history until this point.

4. Commit `c0ebedd`:
- This commit appears on both main and b1, marking the point where the branches diverged.

5. Older Commits:
- `c1eb703` is tagged as tag1, representing the seventh line commit.
- `3005e3d` contains a modification to Jabberwocky line 2.
- The rest of the commits (965e44f, c165327, etc.) represent earlier changes such as adding a .gitignore file and the initial commits.

The `|` shows that b1 continues from the common commit `c0ebedd` (on both main and b1).
The `|/` indicates that the b1 branch diverged from main at commit c0ebedd.
So, `|` just shows the linear flow of commits in a particular branch. -->



```shell
git log --oneline --all --graph --decorate             # any change?
```

:::{admonition} Instructor's Note 
:class: tip
Use `--decorate` when you want to quickly understand which commits belong to which branches or tags. It’s particularly helpful when working on repositories with multiple branches and tags, as you can immediately see where each branch or tag is positioned in the commit history.
:::

We should now focus on the output! Lets change the branch now to `B1`:
```shell
git switch B1                                          # on branch B1
cat Lines.txt                                          # verify (Lines.txt should be without duplicate ninth line)
```
Lets add the tenth line on the `Lines.txt` file to show a case of conflict:
```shell
echo 'tenth line on B1' >> Lines.txt                   # routine
git add Lines.txt                                      # routine
git commit -m 'Add tenth line on B1' Lines.txt         # routine
git log --oneline --all --graph                        # verify
```
Lets now switch to the `main` branch:

```shell
git switch main                                        # on branch main
```
Before committing the changes, we should review differences between versions of the files using `git diff`
```shell
git diff HEAD HEAD~1 Lines.txt                         # Show changes in Lines.txt between the latest commit and the previous commit
```
The output from the command git `diff HEAD HEAD~1 Lines.txt` shows the differences between the current commit `(HEAD)` and the previous commit `(HEAD~1)` for the file `Lines.txt`.

```csharp
diff --git a/Lines.txt b/Lines.txt
index 8622345..e24eb28 100644
--- a/Lines.txt
+++ b/Lines.txt
@@ -7,4 +7,3 @@ did gyre and gimble
 seventh
 eigth line
 ninth line
-ninth line (duplicate)
(END)
```
<!-- 
**1. diff --git a/Lines.txt b/Lines.txt:**
This line indicates that a diff is being generated for the file Lines.txt, comparing the version in the **current commit (b/Lines.txt)** to the version in the **previous commit (a/Lines.txt)**.
**2. index 8622345..e24eb28 100644:**
`8622345`: The blob hash of the version of the file in the previous commit (HEAD~1).
`e24eb28`: The blob hash of the version of the file in the current commit (HEAD).
`100644`: This indicates the file mode, showing that it is a regular file.

**3. --- a/Lines.txt and +++ b/Lines.txt:**
`--- a/Lines.txt`: Refers to the version of the file in the previous commit.
`+++ b/Lines.txt`: Refers to the version of the file in the current commit.

**4. @@ -7,4 +7,3 @@:** -->

:::{admonition} Instructor's Note 
:class: tip
This line indicates the line numbers where the differences occur:
  * `-7,4`: The previous version had `4` lines starting from line `7`.
  * `+7,3`: The current version has `3` lines starting from line `7`.

This means that at **line 7** of the previous version, there were `4` lines, while in the current version, there are `3` lines.
:::


```shell
git diff main B1 Lines.txt                             # Show changes in Lines.txt between the main branch and branch B1
git diff main B1~1 Lines.txt                           # Show changes in Lines.txt between the main branch and the parent of the latest commit on branch B1
git diff main~1 B1~1 Lines.txt                         # Show changes in Lines.txt between the parent of the latest commit on the main branch and the parent of the latest commit on branch B1
git log --oneline --all --graph                        # Display a graph of the commit history for all branches in a concise format
```
```shell
git status                                             # verify
nano Lines.txt                                         # edit file to fix mistake
cat Lines.txt                                          # verify
git status                                             # verify
git add Lines.txt                                      # routine
```
```shell
git commit -m  'Correct tenth line on main' Lines.txt  # routine
git log --oneline --all --graph                        # routine
cat Lines.txt                                          # verify
```


````{card} 
Exercise 2 --- Explore differences across branches
^^^    

```{include} exercises/L2-ex02.md
```

```{dropdown} Answers

   ```shell
   # sol. ex1
   git switch B2 sol ex.1
   # sol. ex2 
   git diff HEAD~1
   git diff HEAD~2
   git diff HEAD~3
   ```
   # sol. ex3
   git diff HEAD~4
   git diff HEAD~5
````


````{card} 
Exercise 3 --- Commit in a secondary branch
^^^    

```{include} exercises/L2-ex03.md
```

```{dropdown} Answers

    ```shell
    git switch B2                                             # on branch B2
    cat Lines.txt                                             # verify
    echo 'ninth line' >>Lines.txt                             # routine
    echo 'tenth line' >>Lines.txt                             # routine
    git add Lines.txt                                         # routine
    git commit -m 'Add ninth and tenth line on B2' Lines.txt  # routine
    git status                                                # verify
    git log --oneline --all --graph                           # verify
    ```

```
````

Lets keep going and come back to branch `B1`:
```shell
git switch B1                                             # on branch B1
echo 'eleventh line' >>Lines.txt                          # routine
echo 'twelfth line' >> Lines.txt                          # routine
git diff                                                  # routine
git add Lines.txt                                         # routine
```
```shell
git commit -m 'Add 11th and 12th lines on B1' Lines.txt   # routine
git log --oneline --all --graph                           # routine
```
We now move back to `main` branch:

```shell
git switch main                                           # on branch main
git diff main B1 Lines.txt                                # verify
git merge -m 'Merge development from branch B1' Lines.txt # wrong syntax
```
Here is the output:

```csharp
❯ git merge -m "merge development from branch b1" Lines.txt
merge: Lines.txt - not something we can merge
```
This `Lines.txt` in the previous `git merge` command is incorrectly specified as the target to merge. Git expects a branch name here, not a file. To merge changes from branch `B1` into the current branch (e.g., `main`), you should use the branch name, not a file name. But lets explore another error:

```shell
git merge -m 'Merge development from branch B1'           # wrong syntax
```


The **error message fatal** `No remote for the current branch` indicates that the current branch does not have a remote tracking branch set up. This means Git doesn't know which remote branch to merge from. To merge changes from a specific branch (e.g., `B1`) into the current branch, you need to specify the branch name:

```shell
git merge -m 'Merge development from branch B1' B1        # right syntax: fails because of conflict
```
When a merge conflict arises, you should not view it as a limitation of Git but rather as a helpful feature. If you try to merge branches with conflicting changes in a file the output looks similar to this:

```csharp
Auto-merging Lines.txt
CONFLICT (content): Merge conflict in Lines.txt
Automatic merge failed; fix conflicts and then commit the result.
```

During a merge conflict, you can run `git status` to see which files are in conflict:

```csharp
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   Lines.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

You can also check the different file versions with `diff`
```csharp
git diff Lines.txt                                        # verify
```
<!-- Git will highlight the conflicting parts in the affected file(s), and you must choose the desired changes or modify them to create a consistent version. To do this, open up the file(s) with conflicts in a text editor of your choice, and you’ll see the conflicting sections marked with the following indicators:

* `<<<<<<<`: indicates the beginning of lines that encountered a merge conflict.
* `=======`: shows the break point for comparison.
* `>>>>>>>`: shows the end of the lines with a merge conflict.

The lines between `<<<<<<< HEAD` and `=======` represent the changes that were made in your current branch. -->


To resolve the merge conflict, you need to manually edit the conflicting sections to the desired state, removing the conflict markers. You might want to keep some changes from your current branch, some from the merged branch, keep only the changes from one branch, or make entirely new changes.

```shell
cat Lines.txt                                             # explore
nano Lines.txt                                            # edit the file within the conflict decorations
```

In this example, the conflict has been resolved by mixing both sets of changes. Parts of the changes from both branches are now present in the file. If you are done you can use git add to stage the resolved changes:
```shell
cat Lines.txt                                             # verify
git diff                                                  # verify
git status                                                # verify
git add Lines.txt                                         # mark resolution
git status                                                # verify
```
```shell
git commit -m 'Merge changes from B1 into main' Lines.txt # conclude merge wrong syntax
git commit -m 'Merge changes from B1 into main'           # conclude merge right syntax
cat Lines.txt 
```
```shell                                            # verify
git status                                                # verify
git log --oneline --all --graph                           # verify
git log --oneline --all --graph --parents                 # verify
```

````{card} 
Exercise 4 --- A first type of merge
^^^    

```{include} exercises/L2-ex04.md
```


```{dropdown} Answers

    ```shell   
    # sol. ex.1 
    git switch B2
    wc -l Lines.txt
    git switch main
    wc -l Lines.txt
    # sol. ex.2
    git switch main
    git merge B2
    # sol. ex.3
    git log --oneline --graph --decorate --all
    ```

```
````

## Episode 2: Understanding operations with remotes

### 2.2.1 Create and explore a bare repository

:::{admonition} Instructor's Note 
:class: tip
Lets first explain what is a bare repository:

> A bare repository is a repository that doesn't have a working directory. It only contains the .git directory, the directory in which Git stores all its internal data. The main purpose of these repositories is to be a central repository that developers can push to and pull from, so there's no need in having a working directory. Bare repositories are also used in Git hosting services like GitHub and GitLab. In the next several lessons we will learn how to create a bare repository and how to push to it [Stackoverflow forum](https://stackoverflow.com/questions/37992400/what-is-a-bare-repository-and-why-would-i-need-one).

:::

<!-- **- A. Working Space (Working Directory)**
  1. What It Is: The working space (or working directory) is where you can see and modify files in a Git repository. It represents the current state of your project on your local machine. This is where you do your coding, editing, and file changes.
  2. Purpose: The working space is for active development. It contains your project files in their checked-out state (the version currently being worked on).
  3. What It Contains: The working directory contains all the project files, including the .git directory (the hidden folder that stores Git’s metadata and history). You can modify these files and later stage and commit the changes to the repository.

- Key Operations in the ** Working Space**:
  1. `git add`: Stage changes from the working directory for commit.
  2. `git commit`: Commit the staged changes to the Git history.
  3. `git status`: View the current state of the working directory (i.e., which files have been modified, staged, or are untracked).
  4. `git checkout` or `git switch`: Change branches or switch to different commits in the working directory.

- Relation to the Repository:  The working space is tied to a non-bare Git repository, which allows you to see and work with your project files.
![Key Differences:](image.png)


**B. Bare Repository**
  1. What It Is: A bare repository is a Git repository without a working directory. It consists only of the Git version history, metadata, and objects (commits, branches, tags, etc.), but no editable project files.
  2. Purpose: Bare repositories are commonly used as central repositories that developers push their changes to or fetch changes from. They are not meant for active development; instead, they are used as a collaboration hub for multiple contributors.
  3. What It Contains: A bare repository contains only the internal .git directory with the Git metadata, commit objects, and references (branches, tags, etc.), but none of the project files are checked out. There is no working space, so you cannot directly modify files in a bare repository.
  4. Instead of containing a .git directory inside a folder of files, the bare repository consists only of Git's contents, including:
      - `HEAD`
      - `refs/`
      - `objects/`
      - `config`

  **Key Operations in a Bare Repository:**
      - `git push`: Developers push changes from their local repositories to the bare repository.
      - `git fetch` or `git pull`: Developers pull or fetch changes from the bare repository to their local repositories.
      - Bare repositories are typically hosted on remote servers or shared locations (e.g., GitHub, GitLab).

  **Relation to the Repository:**
      - A bare repository is a remote repository used for collaboration and centralization. It is typically created with the --bare flag (e.g., git init --bare).
      - You cannot directly edit files in a bare repository because it does not have a working directory. -->


```shell
pwd                           # Print the current working directory
cd ..                         # Change to the parent directory (directory of the workshop)
pwd                           # Verify the current working directory
ls -F                         # List files and directories with a trailing '/' for directories
git init --bare git-zero.git  # Initialize a new bare Git repository named git-zero.git
```

```shell
ls -F git-zero.git            # Verify the creation of the bare repository by listing its contents
ls -Fa git                    # List all files and directories, including hidden ones, in the git directory
ls -Fa git/.git               # List all files and directories, including hidden ones, in the .git directory of the git repository
cd git-zero.git               # Change to the directory of the bare repository
ls                            # List all files and directories in the bare repository
```
The following output should be displayed in your terminal:

```csharp
./           HEAD         description  info/        refs/
../          config       hooks/       objects/
```


The files and directories inside `.git` are the **internal data and configuration files** that Git uses to manage the repository. When you run `ls -Fa git-one/.git`, you’re looking at the contents of the `.git directory` in your **cloned repository (git-one)**. This directory is what makes the folder a Git repository.
<!-- 
**Explanation of Each File/Directory:**

- `./`: This refers to the **current** directory (.git itself).
- `../`: This refers to the **parent** directory (git-one), the directory containing the .git folder.
- `HEAD`:
  1. The HEAD file is one of the most important files in Git. 
  2. It points to the current branch that you have checked out. 
  3. When you switch branches with `git switch`, this file changes to point to the new branch. 
  4. Inside the HEAD file, you’ll typically see a reference like this:
- `config`:
  1. This file stores the configuration settings specific to this Git repository.
  2. These settings can include things like the default branch name, user information, remote URLs, and other repository-specific Git configurations.
  3. You can view or modify these settings with commands like git config.
- `description`: A description of the repository (used by web interfaces).
- `hooks/`: Contains scripts to run on specific **Git actions**.
- `info/`: Additional repository information, like ignore rules.
- `objects/`: Stores the content and history (blobs, trees, and commits).
- `refs/`: Stores references to branches and tags. -->

The `.git directory` is the heart of your repository, containing everything Git needs to manage and track changes in your project.

Lets try to write:
```shell
git status                    # observe (fails)
```

The **error message** `fatal: this operation must be run in a work tree` indicates that the git status command was run inside a bare repository. The git status command requires a working directory to show the status of files, but bare repositories do not have a working directory. 


Another **error**:

```shell
git log                       # observe (fails)
```
The **error message** fatal means that your current branch `main` does not have any commits yet indicates that the git log command was run on a branch that does not have any commits. The git log command displays the commit history, but if there are no commits, it cannot show any history.

```shell
git branch                    # observe its empty
cd ..                         # observe
ls                            # verify
```

### 2.2.2 Cloning and pushing to "remote" bare repositories (upstreams)

This command clones the bare repository `git-zero.git` into a new directory named `git-one`.

```shell
git clone git-zero.git git-one                    # new command
```
<!-- 
:::{admonition} Instructor's Note 
:class:tip
- `git clone:` This command is used to create a copy of an existing Git repository. It creates a local copy from the remote repository.
- `git-zero.git:` This is the URL or path of the remote repository that you are cloning. In this case, git-zero.git is the source repository.
- `git-one:` This is the name of the directory where the cloned repository will be saved locally. Instead of cloning into a folder with the same name as the repository (git-zero), you specify a new folder called git-one where the cloned content will go.
::: -->

You should get the following output:

```shell
❯ git clone git-zero.git git-one 
Cloning into 'git-one'... 
warning: You appear to have cloned an empty repository. done.
```
<!-- **What Happened:**
- `Cloning into 'git-one'...`:
1. Git is starting the cloning process and creating a new directory called git-one in your current working directory.
2. This directory will contain the clone of the repository git-zero.git.
- `warning: You appear to have cloned an empty repository.`:
1. This warning means that the repository you're cloning (git-zero.git) does not contain any commits, files, or branches yet. It is an empty repository.
2. This can happen when the source repository was initialized but no changes (files or commits) have been added yet.
- `done.`:
1. Git has completed the cloning process, even though the repository is empty.
2. The local git-one directory has been created and initialized as a Git repository that mirrors the empty remote repository.

**What Does This Mean?**
- You successfully cloned git-zero.git into a new directory called git-one, but since git-zero.git is empty, there are no files, branches, or commits in the git-one directory.
- You can now start working in the git-one repository by adding files, making commits, and pushing them back to git-zero.git.

**Next Steps:**
Since the cloned repository is empty, you could:
- Add some files to the git-one directory.
- Stage and commit these files using git add and git commit.
- Push the changes back to the remote repository git-zero.git using git push. -->


```shell
ls -Fa git-one                                    # observe
ls -Fa git-one/.git                               # observe
ls -F                                             # observe
cd git-one                                        # directory of the first clone
```
```shell
git status                                        # nothing to commit
git branch                                        # observe that is empty
git log                                           # observe (fatal: your current branch 'main' does not have any commits yet)
```
The git remote command is used to manage the set of repositories ("remotes") whose branches you track. These remotes are typically other repositories that you can **fetch** from and **push** to.

:::{admonition} Instructor's Note 
:class: tip
The following key functions of `git remote` can be explained to students:
- `Fetching`:
  1. Fetching from a remote repository means **downloading** new data (commits, branches, or tags) from that remote repository into your local repository.
  2. This allows you to see changes made by other collaborators without affecting your working directory until you decide to merge or integrate the changes.
- `Pushing`:
  1. Pushing to a remote repository means **uploading** your local commits to the remote repository.
  2. This is how you share your changes with others who are working on the same project.
:::

<!-- **What is a Remote Repository?**
A remote repository is another Git repository, typically stored on a remote server (such as GitHub, GitLab, Bitbucket, or another machine), that your local Git repository can interact with.
- When you work locally, you usually have a copy of a repository, but you often need to sync changes with other developers or backups stored in other locations.
- This is where remotes come into play: they represent those **external locations**. -->

```shell
git remote                                        # new command
git remote -v                                     # new short option
```
The command `git remote` lists the short names of all configured remote repositories. When you run `git remote` and see `origin`, it means that there is a remote repository configured with the name `origin`. 

```csharp
origin	/Users/user/Desktop/2024-gitcodev/git-zero.git (fetch)
origin	/Users/user/Desktop/2024-gitcodev/git-zero.git (push)
```

:::{admonition} Instructor's Note 
:class: tip
You can explain the following to studets:
- `origin /Users/user/Desktop/2024-gitcodev/git-zero.git (fetch)`: This shows the URL used for fetching changes from the remote repository. When you run commands like git fetch or git pull, Git will fetch changes from the remote repository located at this path.
- `origin /Users/user/Desktop/2024-gitcodev/git-zero.git (push)`: This shows the URL used for pushing changes to the remote repository. When you run commands like git push, Git will push your local changes to this remote repository.
:::


<!-- What is `origin`?: origin is the default name given to the remote repository when you clone a repository or add a remote for the first time. It is a shorthand reference to the URL of the remote repository from which you cloned your local repository. You can fetch from and push to this remote repository using the name origin. -->

```shell
echo 1 >> numbers.txt                              # routine
cat numbers.txt                                   # verify
git status                                        # routine with git status (untracked file: numbers.txt)
git add numbers.txt                               # routine with git status 
git status                                        # routine with git status (changes to be commited: numbers.txt)
```

```shell
git commit -m 'git-one: add first 1' numbers.txt  # routine with git status
git log --oneline                                 # verify
git status                                        # verify (ignore the but-warning)
```
```shell
git push                                          # new command
```
This is the expected output after `git push`:

```csharp
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 234 bytes | 234.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To /Users/ccugutrillague/Documents/courses/gitcodev/2310-gitcodev/git/git-zero.git
 * [new branch]      main -> main
```


<!-- **Explanations:**

1. Enumerating objects: 3, done.
Git is identifying the objects (commits, trees, blobs) that need to be pushed to the remote repository.
In this case, there are 3 objects to be pushed.

2. Counting objects: 100% (3/3), done.
Git counts the total number of objects to be pushed.
It confirms that all 3 objects have been counted.
3. Writing objects: 100% (3/3), 234 bytes | 234.00 KiB/s, done.
Git writes the objects to the remote repository.
It shows the total size of the objects (234 bytes) and the speed at which they were written (234.00 KiB/s).
4. Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
    - Total 3: Indicates the total number of objects being pushed.
    - delta 0: Indicates that no objects were compressed using delta compression.
    - reused 0: Indicates that no objects were reused from the remote repository.
    - pack-reused 0: Indicates that no objects were reused from a previous pack.
5. To /Users/ccugutrillague/Documents/courses/gitcodev/2310-gitcodev/git/git-zero.git
Specifies the remote repository to which the objects are being pushed.
6. `* [new branch] master -> master`
Indicates that a new branch named master is being created on the remote repository.
The local master branch is being pushed to the remote master branch. -->

```shell
git status                                        # verify
```
```shell
cd ../git-zero.git                                # directory of the upstreamgit
git status                                        # observe (fails)
git log                                           # observe
ls -F                                             # observe
cd ..                                             # in the workshop directory
```
```shell
pwd                                               # verify
git clone git-zero.git/ git-two                   # known action
ls -F                                             # verify
cd git-two/                                       # in the second clone
ls -aF                                            # verify
cat numbers.txt                                   # observe
```
```shell
git log                                           # observe
git remote -v                                     # observe
```

<!-- :::{admonition} Instructor's Note 
:class: tip

*This is the summary of `git remote -v` output*
- `origin` is the remote repository.
- The URL for `origin` is `/Users/../Documents/courses/gitcodev/2310-gitcodev/git/git-zero.git`.
- The URL is used for both fetching and pushing changes.
::: -->

```shell
echo 2 >>numbers.txt                              # routine
cat numbers.txt                                   # verify
git add numbers.txt                               # routine
```
```shell
git commit -m 'git-two: add first 2' numbers.txt  # routine
git log --oneline                                 # verify
git push                                          # known action
git status                                        # verify
```


### 2.2.3 Fetching and merging (pulling) from upstreams

The git fetch command is used to download commits, files, and references from a remote repository into your local repository. It updates your local copy of the remote branches without modifying your working directory or local branches.

:::{admonition} Instructor's Note 
:class: tip
These are the *key points* to explain:
1. *Fetches Updates:* Downloads new data from the remote repository.
2. *No Changes to Working Directory:* Does not change your working directory or local branches.
3. *Updates Remote Tracking Branches:* Updates your local copy of the remote branches (e.g., origin/main).
:::

```shell
cd ../git-one                                      # Change to the directory of the first clone
pwd                                                # Verify the current working directory
git status                                         # Verify the status of the working directory
git log --oneline                                  # View the commit history in a concise format
git fetch                                          # Fetch updates from the remote repository
```
The below code is the expected output of the last command:

```csharp
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 238 bytes | 238.00 KiB/s, done.
From /Users/ccugutrillague/Desktop/2024-gitcodev/git-zero
   fa26574..88ee05e  main     -> origin/main
```

:::{admonition} Instructor's Note 
:class: tip

The `git fetch` operation successfully downloaded new commits from the **remote repository (git-zero)** and updated the `origin/main` reference. 
You now have the latest changes from the remote, but *they haven’t been merged into your local branch* yet. 
You can review them or choose to integrate them into your local working directory with a `git merge` or `git pull`.
:::


```shell
git status                                         # routine
git log --oneline                                  # routine
git log --oneline --all                            # routine
cat numbers.txt                                    # routine
```
```shell
# git pull = git fetch + git merge                 # git has compound commands
git fetch                                          # known action
git merge                                          # see episode 2.1 (no conflict here)
```

:::{admonition} Instructor's Note 
:class: tip
Summary of `git merge` output:
- The `git merge` command successfully merged the changes from the specified branch into your current branch.
- The merge was a `"fast-forward"` merge, meaning no new merge commit was created.
- The file `numbers.txt` was modified, with one line added.
:::

```shell
git log --all                                      # verify
cat numbers.txt                                    # verify
echo 1 >>numbers.txt                               # add another 1
```
```shell
cat numbers.txt                                    # routine
git add numbers.txt                                # routine
git commit -m 'git-one: add second 1' numbers.txt  # routine
git log --oneline --all                            # verify
```
```shell
git status                                         # verify
git push                                           # known action
git status                                         # verify
git log --oneline --all                            # verify
```


### 2.2.3 (continued) Resolving conflicts when pushing

```shell
cd ../git-two/                                     # in the directory of the second clone
ls                                                 # observe
cat numbers.txt                                    # observe
git status                                         # observe
git log --oneline                                  # observe
```
```shell
echo 2 >>numbers.txt                               # routine
cat numbers.txt                                    # verify
git add numbers.txt                                # routine
git commit -m 'git-two: add second 2' numbers.txt  # routine
git status                                         # verify
```
```shell
git log --oneline                                  # verify
git push                                           # known action with conflict
```
Expected `git push` output:

```csharp
To /Users/[..]/Documents/courses/gitcodev/2310-gitcodev/git/git-zero.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to '/Users/[..]/Documents/courses/gitcodev/2310-gitcodev/git/git-zero.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
The error message you received when running git push indicates that your push was rejected because the remote repository contains commits that are not present in your local repository. This situation typically arises when someone else has pushed changes to the remote repository that you do not have locally. 
<!-- 
**Explanation:**

**To /Users/ccugutrillague/Documents/courses/gitcodev/2310-gitcodev/git/git-zero.git**
- Specifies the remote repository to which you attempted to push.

**! [rejected] master -> master (fetch first)**
- Indicates that the push was rejected.
- The `master` branch on your local repository could not be pushed to the `master` branch on the remote repository.
- You need to fetch the latest changes from the remote repository first.

**error: failed to push some refs to '/Users/ccugutrillague/Documents/courses/gitcodev/2310-gitcodev/git/git-zero.git'**
- Confirms that the push operation failed.

**hint: Updates were rejected because the remote contains work that you do not have locally.**
- Explains that the remote repository has commits that are not present in your local repository.

**hint: This is usually caused by another repository pushing to the same ref.**
- Indicates that another user or repository has pushed changes to the same branch you are trying to push to.

**hint: You may want to first integrate the remote changes (e.g., 'git pull ...') before pushing again.**
- Suggests that you should fetch and merge the remote changes into your local branch before attempting to push again.

**hint: See the 'Note about fast-forwards' in 'git push --help' for details.**
- Refers you to the Git documentation for more information about fast-forward merges and push rejections. -->

The reason for rejection is that you need to `fetch` the latest changes from the remote repository first.

:::{admonition} Instructor's Note 
:class: tip
Summary of git push output:

1. *Push Rejected:* The push was rejected because the remote repository contains commits that are not present in your local repository.
2. *Fetch First:* You need to fetch the latest changes from the remote repository and integrate them into your local branch before pushing again.
3. *Steps to Resolve:* Fetch the latest changes, merge them into your local branch, resolve any conflicts, and then push again.
:::

```shell
git fetch                                          # Fetch updates from the remote repository
git status                                         # Check the status of the working directory
git merge                                          # Merge the fetched changes into your current branch
```
```shell
git diff                                           # Show the differences and conflicts
```
The output of the `git diff` command with `diff --cc` indicates a merge conflict in the numbers.txt file. This happens when Git tries to merge two branches (or commits) that have changes to the same part of the file, and Git cannot automatically resolve the differences.

```csharp
diff --cc numbers.txt
index 2ca3cd5,e13c5bf..0000000
--- a/numbers.txt
+++ b/numbers.txt
@@@ -1,3 -1,3 +1,7 @@@
  1
  2
++<<<<<<< HEAD
 +2
++=======
+ 1
++>>>>>>> refs/remotes/origin/main
```


This part shows the merge conflict markers and the conflicting lines between the two versions of the file:
- `@@@ -1,3 -1,3 +1,7 @@@`: This shows the conflicting area in both versions of the file. In both the local HEAD and the remote origin/main, there’s a conflict starting from line 1, and the conflict spans a few lines.
Conflict Markers:
- `<<<<<<< HEAD`: The lines below this marker are the changes from your current branch (HEAD), which refers to the branch you are currently on. (`+2`)
This means that, in your local branch, there is an additional 2 that was added to the file.
- `=======`: This marker separates the changes between your local branch (HEAD) and the remote branch (origin/main).
- `>>>>>>> refs/remotes/origin/main`: The lines below this marker are the changes from the remote branch (origin/main), which is the branch being merged into your local branch.

:::{admonition} Instructor's Note 
:class: tip

**You can ask students about the current situation**

- In your local branch (the current HEAD), you added a second 2 to **numbers.txt** (resulting in two lines with 2).
- In the remote origin/main branch, a 1 was added to the file (which conflicts with your changes).

**You can ask students how should we resolve this conflict**

To resolve this, you need to manually edit the `numbers.txt` file and decide which change to keep. You have three options:

1. *Keep your changes from the local branch (HEAD):* Remove the conflict markers and keep the changes from your branch (+2).
2. *Keep the remote changes from origin/main:* Remove the conflict markers and keep the changes from the remote (+1).
3. *Combine both changes:* Modify the file to include both changes in a way that makes sense.

:::
```shell
cat numbers.txt                                    # View the contents of numbers.txt
nano numbers.txt                                   # Edit the file to resolve the conflict
cat numbers.txt                                    # Verify the resolved contents of numbers.txt
git status                                         # Verify the status of the working directory
```
```shell
git add numbers.txt                                # mark resolution
git status                                         # verify
git commit -m 'git-two: conclude merge'            # conclude merge
git status                                         # verify
git log --oneline                                  # verify
```
```shell
git push                                           # known action
git log --oneline                                  # verify
git status                                         # verify
```

````{card} 
Exercise 5 --- Another type of merge
^^^    

```{include} exercises/L2-ex05.md
```

```{dropdown} Answers

    ```shell   
    # sol. ex.1 
    git switch B2
    git merge B2
    # sol. ex.2
    # make the changes in the file, then:
    git commit
    wc -l Lines.txt
    # sol. ex.3
    git log --oneline --graph --decorate --all
    ```

```
````


<!-- ```{dropdown} Differences Between git fetch and git merge?
Key Differences
* `git fetch:` Only downloads updates from the remote repository.
Does not change your working directory or local branches.
Allows you to review changes before merging.
* `git merge:` Merges changes from one branch into another branch.
Directly modifies your current branch by integrating changes from the specified branch.
Typically used to combine feature branches into the main branch. -->
