# Teaching Resources

This section contains a list of resources that can be used by the intructor. The resources are divided into two categories:
* **Teaching resources**: These are resources that can be used by the instructor to deliver the course. They include slides, tools, and other materials that can be used to support the teaching of the course.
* **Prepartion resources**: These are resources that can be used by the instructor to adquired the knowledge and sills required to teach the topics in the course.


## Teaching Resources

### Terminal History Set-Up

The following helps the instructor to set up a terminal that will show the history of command from one terminal in another. This helps participant to keep track of what commands have been typed by the instructor.  

1. On main terminal:
```bash
 export PROMPT_COMMAND="history -a; $PROMPT_COMMAND"
```
2. On second (history) terminal:
```bash
 tail -f ~/.bash_history | nl -w 3
```

### Windows Terminal (Preview) 
Shortcuts for the Windows Terminal (Preview) App on Windows 11.

| Action             | Shortcut                |
|--------------------|--------------------------|
|Split pane horizontally | Alt + Shift + `-`   | 
|Split pane vertically   | Alt + Shift + `+`   |
|Close a pane            | Ctrl+Shift + `w`     |
|Move pane focus         | Alt + `Arrow keys`   |
|Resize the focused pane | Alt+Shift + `Arrow keys` |


### MacOS Terminal
Shortcuts for the terminal in MacOS

| Action             | Shortcut                |
|--------------------|--------------------------|
|Split pane horizontally | Cmd + `d`   | 
|Close a pane            | Shift + Cmd + `d`   |
------

## Presentations

* [Lesson 1: Fundamental operations with Git]()
* [Lesson 2: Branching and remote operations]()
* [Lesson 3: Collaborative workflows](https://docs.google.com/presentation/d/1yBy_4r9aHhsUH9AH1s7zLWIQ_h20xNKVYM1somPnz1Q/edit?usp=sharing)
* [Lesson 4: Managing collaboration and best practices](https://docs.google.com/presentation/d/1TvWIrBsVNwmEyvZodd4V7gueATeECKMubUqSSYKMyuU/edit?usp=sharing)


## Preparation Resources

* [Git Documentation](https://git-scm.com/doc)
* [GitHub Documentation](https://docs.github.com/en)
* [GitLab Documentation](https://docs.gitlab.com/)

