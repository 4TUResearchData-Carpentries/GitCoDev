# LESSON 1: Fundamental Operations with Git

Lecture notes on the fundamental operations with Git. A hands-on lesson for introducing version control, tracking changes, and the tracking history. 


:::{card} Learning Objectives:

* To understand the basic operations of version control using Git. 
* To use Git to create repositories and commit changes. 
* To apply Git operations to track, reverse and delete changes in working documents. 
* To organise tracked changes in the Git history. 

**Topics:**

{bdg-dark}`git syntax`
{bdg-dark}`version control`
{bdg-dark}`repositories`
{bdg-dark}`tracking changes`
{bdg-dark}`untracking files`
{bdg-dark}`gitignore`
{bdg-dark}`undoing changes`
{bdg-dark}`deleting and renaming files`
{bdg-dark}`committing changes`
{bdg-dark}`inspecting changes`
{bdg-dark}`tags`

+++
**Materials:**

* [Collaborative software development](https://docs.google.com/presentation/d/1BucILQ9Osz_2tKYF3kF-c3uZFND8xfJ4/edit?usp=sharing): a presentation that introduces the workshop and contains slides with this lesson exercises.
:::


## {octicon}`repo` Episode 1: Git repositories for version control
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`ca 50 min total`


### 1.1.0 Welcome slides
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


Introduce:
* Trainers
* Code of conduct
* Course outline
* Today's schedule
* The need for and goals of version control
* The role of git as a software solution supporting these goals

### 1.1.1 Introduction to Git
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`

* Create a directory for the course

:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
Students are assumed to have at least basic awareness of working from the command line and navigating the directory tree,
but help them if necessary.
:::

In the first section, we create the directory that will house the project. Note that depending on the environment setup,
the Desktop may or may not actually be under the participants' home directory so instructor and  helpers should be ready to help learners locate it.

```shell
    cd ~/Desktop/
    ls
    mkdir -p 2410-gitcodev/git
    ls
    ls 2410-gitcodev/
```
```shell
    cd 2410-gitcodev/git/
    ls
    pwd
```
* Check which shell is available 

```shell
    echo $SHELL
    echo
```

* Check installed version of Git
* (This will be the participants' first interaction with git, so any installation or PATH problems should show up here)

``` shell
    git
    git --version
    git version
```

### 1.1.2 Git Command Syntax and Getting Help
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


* We indtoduce the git help system both as a resource that they can use in future, and a way to start getting used to the CLI interface and command format.

```shell
    git help
    git help help
    git config
    git config --list
```

Introduce the key config parameterts, including pre-setting some that only apply on day 2. Participants may need a reminder to substitute their own details, and a quick explanation of the Windiws vs Unix end-of-line conventions (Carriage Return / Linefeed on Windows, only Linefeed on Mac / Linux / other unixoids)

```shell
    git config --global user.name "John Doe"
    git config --global user.email johndoe@example.com
    git config --global core.editor nano
    git config --global core.autocrlf input # false for Win
    git config --global init.defaultBranch main
    git config --list
    git help config
```
```shell
    git help glossary
    git help -g
```

### 1.1.3. Creating an Empty Reposiory
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
Here and throughout, it is possible to edit the file with an editor rather than appending
lines with *echo*, however this will make the nature of the changes invisible in any
gitautopush record, so is not recommended in class.
:::

* We add some content to a file and observe that, where no repo has been initialised, operations like 'git status' don't do very much.
* We follow this with a git init.  It is important to be sure that all participants are actuall in the correct directory when they do this.

``` shell
    pwd
    ls
    echo 'first line'
    echo 'first line' >lines.txt
    ls
```
```shell
    cat lines.txt
    echo 'second line' >>lines.txt
    cat lines.txt 
    git status
    git init
```
The *git status* command above should return a fatal error because we are not in a repository.

```shell
    ls
    ls -a
    ls -aF
    ls -aF .git
    ls
```

### 1.1.4. Q&A
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


At this point, we have an empty repository, plus a single file in a working directory that has not been added to the repository.
Students have had a brief view (via *ls -af .git*) of the inner contents of the repository proper, but should not be encouraged to dig
too deeply at this point.

### {octicon}`stopwatch` Break
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


## {octicon}`repo` Episode 2: Tracking Changes in Working Documents
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`ca 75 min`

### 1.2.1 Tracking Changes with the Index
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


* In this section, we observe that a file in the working directory that has not been explicitly added to the repo is observed by git status, but not yet tracked.  So we introduce the git add command and, alongside it, git diff.

```shell
    git status 
    git add lines.txt
    git status 
    ls -a .git
    git diff lines.txt
```
:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
The only visible difference between the output of this and the previous *ls -a .git* is the appearance of the *index*
:::

```shell
    echo 'third line' >>lines.txt
    cat lines.txt
    git diff lines.txt
```

**Output:**
The output of the *git diff* command should resemble the following. Use this opportunity to explore the format of a diff file.

```shell {Output}
    diff --git a/lines.txt b/lines.txt
    index 06fcdd7..20aeba2 100644
    --- a/lines.txt
    +++ b/lines.txt
    @@ -1,2 +1,3 @@
     first line
     second line
    +third line
```

* We see that new additions to tracked file still need to be added to the index.  The instructor may want to explain cases where this is relevant and useful.

```shell
    git status 
    git add lines.txt
    git status 
    git diff lines.txt
```


````{card} 
{bdg-dark}`Exercise 1.1` --- Tracking changes with the Index
^^^    

```{include} exercises/L1-ex01.md
```

```{dropdown} Answers

    [No answers yet]

```
````

#### Tracking Directories
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`

:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
In this section, we see that while empty directories are not tracked or `seen' by git,
adding a directory to the index automatically adds its contents.
:::

```shell
    mkdir directory
    ls
    ls -F
    git status 
    touch directory/emptyfile.txt
```

* git status should not 'notice' the empty directory

```shell
    ls -R
    ls -RF
    git status 
    git status -u
    git help status
```

* git status should report the untracked filename
  
```shell
    git add directory
    git status
```

* git status here should report emptyfile.txt as staged but not committed

### 1.2.2 Not Tracking and Stop Tracking
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
In this section, we introduce the .gitignore mechanism. It is worth taking a few minutes to talk about the kinds
of files associated with a project that you might not want to track, such as IDE configurations, Apple .DS_Store
files, log files, test run outputs etc. We don't want these cluttering up our git status output, or accidentally
messing up our coleagues' work environments.
:::

* First, we generate a random log file of the kind we don't want to track.

```shell
    history
    history 20
    history 20 >history.log
    cat history.log 
    git status
```

* git status reports the new, untracked file
* Next, we will add a glob that matches the file to .gitignore.

```shell
    echo '*.log'
    echo '*.log' >.gitignore
    git status
    ls -a
    ls -aF
```

* git status should no longer report the file at all, although it is still present in the working directory

```shell
    git add .gitignore
    git status 
    echo 'lines.txt' >>.gitignore
    cat .gitignore
```
:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
Adding lines.txt, as we can see in the git status output, does not remove lines.txt from the index,
and git continues to track it, but would not start tracking it or offer it for staging if it were new.
:::

```shell 
    git status 
    git add .gitignore 
    git status 
```
* .gitignore is a regular file and will be tracked unless listed in .gitignore. Whether or not this is a good idea for a particular project is up to the collaborators.

#### Ignore Untracked Directories
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
This section illustrates three points:
* That git ignores the contents of directories that match a line in .gitignore,
* That ! is a not operatory for matching purposes
* That git will implement the 'last rule standing' after parsing .gitignore
:::

```shell
    touch directory/trackme.txt
    touch directory/donttrackme.txt
    ls directory/
    git status 
    echo 'directory' >> .gitignore
```
```shell
    cat .gitignore 
    git status
    echo '!directory' >> .gitignore
    cat .gitignore 
    git status
```
```shell 
    cat .gitignore 
    echo 'directory' >>.gitignore
    cat .gitignore 
    git status 
    git help gitignore
```
```shell
    git status 
    git add .gitignore 
    git status 
```
```shell
    git rm --cached directory/emptyfile.txt 
    git status 
    ls -FR
```


````{card} 
{bdg-dark}`Exercise 1.2` --- Stop tracking Changes in a File
^^^    

```{include} exercises/L1-ex02.md
```

```{dropdown} Answers

    [No answers yet]

```
````

### {octicon}`stopwatch` Break
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`20 min`


### 1.2.3 Undoing Changes with the Index
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
The central idea here is the use of git restore to 'undo' changes to tracked files in the working directory from
the index, not from the commit history, as we haven't introduced that yet.
:::

```shell
    cat lines.txt 
    echo 'fifth line' >>lines.txt 
    cat lines.txt 
    git status 
    git diff lines.txt
```
```shell
    git restore lines.txt
    cat lines.txt 
    git status 
    git diff lines.txt
    git restore lines.txt
```
```shell
    cat lines.txt 
    git status 
    echo '!directory' >>.gitignore
    ls
    git status 
```
```shell
    git status -u
    git add directory/trackme.txt 
    git status -u
    git add directory/donttrackme.txt 
    git add directory/emptyfile.txt
```
```shell 
    git status 
    git add .gitignore 
    git status 
```

### 1.2.4  Deleting and renaming tracked files and directories
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
Here we illustrate the need to use git's utilities to delete or rename files
that are tracked in the repo, if their history is to be properly maintained.
:::

```shell
    git rm --cached directory/donttrackme.txt 
    git status 
    rm -r directory/
    ls -FR
```
```shell
    git status 
    git restore directory
    git status 
    ls -FR directory/
    touch directory/donttrackme.txt
```
```shell
    git status 
    git rm directory
    git rm -r directory
    git status 
    git rm -rf directory
```
```shell
    git status 
    ls -FR directory/
    git restore directory
    git status 
    git status -u
```
```shell
    mv directory/donttrackme.txt directory/trackne.txt
    git status -u
    # use the command `git mv <oldname> <newname>`
    # lines.txt Lines.txt
    git status -u
    git mv lines.txt Lines.txt
    git status -u
```

````{card} 
{bdg-dark}`Exercise 1.3` --- Renaming Tracked Files
^^^    

```{include} exercises/L1-ex03.md
```

```{dropdown} Answers

    [No answers yet]

```
````

## {octicon}`repo` Episode 3: Organizing Tracked Changes in a History
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`ca 75 min`

:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
This is a critical moment in the lesson. We have introduced the index, as a representation
of the project at a point in time. Now we begin to develop the idea of the repository as a
sequence of such staged changes over time that culminate in the current state of the project
(or branch, but we haven't introduced that concept yet), HEAD.
:::

### 1.3.1 Commiting Changes with a Configured Identify and a Message
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`

* We introduce the 'git commit' command as an commitment of the state of the index at some point in time.
* We note that a commit MUST be accompanied by a descriptive message

```shell
    cat Lines.txt 
    git diff
    git status 
    git commit -m 'Add first four lines' Lines.txt
```
* We see next that a succesful commit gives us a 'clean' index with no stages changes, but we can look at a log and see the history.
* When we look at the log, we see the 'long form' commit ID for the commit we just made, which is effectively guaranteed to be globally unique.

```shell
    git status 
    git log
```


`````{card} 
{bdg-dark}`Exercise 1.4` --- Commit Changes in a Tracked File

^^^    

````{include} exercises/L1-ex04.md
````

````{dropdown} Answers    
```shell
    git status 
    git commit -m 'Add .gitignore' .gitignore 
    git status 
```
```shell
    rm -r directory  # to keep things clean
    git status 
    ls
    git log
```
````
`````


`````{card} 
{bdg-dark}`Exercise 1.5` --- Follow the state of the repository in the commit routine
^^^    

````{include} exercises/L1-ex05.md
````

````{dropdown} Answers    
```shell
    # Procedure for exercise 5
    echo 'fifth line' >>Lines.txt 
    cat Lines.txt 
    git status 
    git add Lines.txt 
    git status
```
```shell 
    git commit -m 'Add fifth lines' Lines.txt 
    git status 
    history
    git log
```
````
`````

### 1.3.2 Inspecting Changes Using the History


`````{card} 
{bdg-dark}`Exercise 1.6` --- Follow the state of the index in the commit routines
^^^    

````{include} exercises/L1-ex06.md
````

````{dropdown} Answers    

```shell
    # procedure for exercise 6
    git status 
    git diff
    echo 'sixth line' >>Lines.txt 
    git diff
    git add Lines.txt
```
```shell 
    git diff
    git diff Lines.txt
    git commit -m 'Add sixth line' Lines.txt 
    git diff
    git log
```
```shell
    git log --oneline
    git status 
    echo 'seventh line' >>Lines.txt 
    git diff Lines.txt
    git add Lines.txt
```
```shell 
    git diff Lines.txt
    git status 
    git log --oneline
    git diff HEAD Lines.txt
    git diff e278702 Lines.txt
```
```shell
    git diff HEAD~1 Lines.txt
    git log --oneline
    git diff 7f2ca Lines.txt
    git diff HEAD~2 Lines.txt
    git diff HEAD~3 Lines.txt
```
```shell
    git diff HEAD~7 Lines.txt
    git diff Lines.txt
    git diff HEAD~3 Lines.txt
    git diff HEAD HEAD~1 Lines.txt
    git diff HEAD~1 HEAD Lines.txt
```
```shell
    git diff HEAD~4 HEAD~2 Lines.txt
    git diff HEAD~3 HEAD~2 Lines.txt
    git log
    # 
    pwd
```
```shell
    git status 
    git log --oneline
    git diff Lines.txt
    git diff HEAD Lines.txt
    git diff HEAD~1 Lines.txt
```
```shell
    git diff HEAD HEAD~1 Lines.txt
    git diff HEAD~1 HEAD Lines.txt
    diff HEAD HEAD Lines.txt 
    git diff HEAD HEAD Lines.txt 
    git diff HEAD~2 HEAD~2 Lines.txt
```
````
`````

### {octicon}`stopwatch` Break 
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


`````{card} 
{bdg-dark}`Exercise 1.7` --- Explore the changes recorded in the history
^^^    

````{include} exercises/L1-ex07.md
````

````{dropdown} Answers    
```shell
    # No answers yet
```
````
`````

> Exercise 8 is an optional exercise about [comparing differences in the history.](./exercises/L1-ex08.md)


### 1.3.3 Undoing Changes with the History
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
This topic involves using `git restore`.
We have introduced the HEAD~x notation in the exercises above, and we will introduce both the short form commit ID and the tag mechanism shortly.  Here we see that using the -s flag we can specify a source (commit) from which to restore a specified file. 
:::

```shell
    git restore -s HEAD~2 Lines.txt
    cat Lines.txt
    git status
    git restore -s HEAD Lines.txt
    git status
```


### 1.3.4 Marking the History Using Tags
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`

* Lightweight tags
* Using the git tag mechanism, we can 'name'specified commits for ease of reference.  These may represent special points in a project, like releases, or particular points in the development lifecycle, or just be useful 'bookmarks'.
* We also see here, using git log --oneline, the short form commit ID, which is effectively guaranteed to be project-unique, if not globally unique.

```shell
    git log --oneline
    git tag 'hey'
    git log --oneline
    git log
```
```shell
    git tag 'hey' HEAD~1
    git tag 'hey2' HEAD~1
    git log --oneline
    git tag 'hey3' HEAD~5
    git tag 'hey4' 87ab7b6
```
```shell 
    git log --oneline
    git diff HEAD HEAD~1 Line.txt
    git diff HEAD HEAD~1 Lines.txt
    git diff hey hey2 Lines.txt
    git log --oneline
```
```shell
    git diff hey hey2 Lines.txt
    echo 'eighth line' >>Lines.txt
    cat Lines.txt 
    git status 
    git add Lines.txt
```
```shell 
    git status 
    git commit -m 'Add eighth line' Lines.txt
    git log --oneline
    git tag -d hey1
    git tag -d hey4
```
```shell
    git log --oneline
    git diff hey hey4 Lines.txt
    git log --oneline
    git tag -d hey2
    git tag -d hey
```
```shell
    git tag HEAD~4 v1
    git tag v1 HEAD~4
    git log --oneline
    git tag v2 HEAD~3
    git tag v3 HEAD~2
```
```shell
    git log --onelein
    git log --oneline
    git tag v4 HEAD~1
    git tag v5 HEAD
    git log --oneline
```


`````{card} 
{bdg-dark}`Exercise 1.9` --- Add lightweight tags to the history
^^^    

````{include} exercises/L1-ex09.md
````

````{dropdown} Answers    
```shell
    # no answers yet
```

````
`````

* Annotated Tags

* THis section is fundamentally similar except that the tags get an additional annotation via the -m option.

```shell
    git tag -a
    git tag -a -m 'First annotated tag' 
    git tag -a -m 'First annotated tag' TAG1
    git log --oneline
```
```shell
    git tag
    git show
    git show HEAD~1
    true
```

## {octicon}`log` Lesson Summary
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


Give a short wrap up about what has been learned. Encourage questions and perhaps give a 'teaser trailer' for lesson 2.


:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
Remember to coordinate with the trainer for day 2 to ensure that they have a repository that begins day 2 with the same state as the learners, either by their rerunning the command log, or by physically copying your repo in a ZIP or tarfile.
:::
