# LESSON 3: Collaborative Software Development
Lecture notes for the lesson on an introduction to collaborative software development. 
This lesson is taught using presentations (to illustrate concepts), demostrations and exercises (to practice the concepts). 
The code examples in the lessons often indicate tasks that participant should do along with the instructor.

:::{card} Learning Objectives:

- To understand the key aspects of managing research software projects. 
- To make use of issues, code changes, and pull/merge requests to make contributions to a software project hosted in a collaborative platform.
- To compose a software development team by assigning roles and responsibilities to a group of developers. 
- To contribute to the development of research software using a collaborative approach. 
- To choose between a centralised and shared collaborative workflow for a new software project. 
- To create contributions to software projects using one of the Git repository platforms such as GitHub. 

**Topics:**

{bdg-dark}`collaborative platforms`
{bdg-dark}`GitHub GUI`
{bdg-dark}`research software projects`
{bdg-dark}`managing projects`
{bdg-dark}`organising teams`
{bdg-dark}`collaborative workflows`
{bdg-dark}`documenting issues`
{bdg-dark}`centralised workflow`
{bdg-dark}`shared workflow`
{bdg-dark}`pull requests`

+++
**Materials:**

* [Collaborative software development](https://docs.google.com/presentation/d/1yBy_4r9aHhsUH9AH1s7zLWIQ_h20xNKVYM1somPnz1Q/edit?usp=sharing): a presentation with general information about the lesson and illustrations for supporing the explanations of some of the concepts, and exercises.
* [Username form](https://forms.gle/asj6dAhTh6vcyUhV9): a Google form to collect users-names of the collaborative platform that participants will use during the lesson. This serves as an example. 

:::


## {octicon}`tasklist` Preparation  

:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
* The instructor must collect particiapant's user names for GitHub/Gitlab beforehand, so that they can be invited to collaborative repositories. The **username form** serves as an example of how this could be done.
* The instructor must create a repository for [](check-in) using this [respository tempalte](https://github.com/WorkshopGitcodev/check-in-template).
:::


## {octicon}`history` Recapitulation: Operations with Remotes 
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`5 min`


Common operations with remotes

:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
* Recapitulation on how local repostories and remotes are connected and how to work with remotes (Slides).
* Recapitulation on what `clone, fetch, merge, pull` and `push` commands do.
:::

## {octicon}`repo` Episode 1: Collaborative Platforms

### 3.1.1. Connecting to Code Repositories  
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`10 min`


* Ask participants using Windows not to start Git Bash clicking on the desktop icon, as they did in Lesson 1. Instead,
    * use the app menu (the Windows logo)
    * pick up Git Bash from the list
    * launch Git Bash with the option **Run as administrator** available from the drop-down submenu.
    The participants may need to type in their credentials as local administrators.
This gain authority to have SSH installing its own features in their laptop next.

:::{admonition} {octicon}`mortar-board` Instructor's Note  
:class: tip
At their very first `git push`, Git might complain about a mismatch between the credentials of local and global administrator.
The warning itself suggests another Git command as the remedy to this impasse.
:::

#### Setting up SSH connection for GitHub

:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
GitHub requires authentication via SSH to do pulls and pushes, but not for cloning public repositories. Explain what a SSH connection entitles (slides).

Some participants might have already set up SSH keys for GitHub. In this case, they can skip the next steps. They can check if they have SSH keys by running the following command in the terminal:

```shell
    ssh -T git@github.com # for GitHub
```
:::

* If a SSH connection must be set, do the following in a BASH terminal:

    1. Create a Key-pair inside the `.ssh`  in the Home directory
        ```shell
            # move to Home directory
            cd ~
            # create key
            ssh-keygen -t ed25519 -C "your_email@example.com"
            # save to the default location and file name: ~/.ssh/id_ed25519
        ```

    2. Check the keys have been created
        ```shell
            ls ~/.ssh/
        ```

    3. Start the `ssh-agent` and add the **private** key to agent. This might be necessary for Windows users only.
        ```shell
            # start ssh-agent in the background
            eval "$(ssh-agent -s)":
        ```shell
            # start agent
            eval "$(ssh-agent -s)"

            # add private key
            ssh-add ~/.ssh/id_ed25519
        ```
    4. If a the private key was not save on the default directory, instruct SSH to use key files in different locations:
        ```shell
            ssh -i <path/private/keyfile>
        ```

        :::{admonition} {octicon}`mortar-board` Instructor's Note 
        :class: tip
        Window's user would need to set up the *ssh-agent** to [start the automatically](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases#auto-launching-ssh-agent-on-git-for-windows)
        Mac and Linux user don't have to worry about this.
        :::
    5. Copy public key to GitHub:
        ```shell
            clip < .ssh/id_ed25519.pub
        ```

        :::{admonition} {octicon}`mortar-board` Instructor's Note 
        :class: tip
        Go to GitHub, explain the basics of the interface and
        :::

    6. add the SSH key.
        ```shell
            Profile > Settings > SSH and GPG keys > New SSH key > Add SSH key
        ```

    7. Test SSH connection
        ```shell
            ssh -T git@github.com
        ```

        :::{admonition} {octicon}`mortar-board` Instructor's Note 
        :class: tip
        The message for a successful outcome is friendly and plain. Ask participants whether git@github.com has welcomed them.
        :::

#### Publishing Local Repository to GitHub 
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`5 min`


1. Create GitHub Repo: Go to GitHub and create an public empty repository called `workshop`. Repo description: *workshop on collaborative development*

2. Add Remote to Local Repo: before this remove any existing remotes in the locare repository with: `git remote remove <remote-alias>`

Move back to the repo directory: `~/Desktop/`
In your local repository (on the terminal), add the remote repository and push the content.

* Connect to remote
    ```shell
        git remote add origin git@github.com:<user-name>/<repo-name>.git
    ```

* Check that remote was added
    ```shell
        git remote -v
        git branch -M main # [Optional if config was changed. This will change the name of the main branch of the repo to make it more friendly]
        git push -u origin main
    ```

#### Check the Content is in GitHub
Go back to your repo page and refresh the browser.

:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
Questions?
:::

### 3.1.2. Exploring the GitHub GUI 
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`5 min`

Collaborative platforms host and manage remote repositories to facilitate descentrilized collaborative development workflows.

:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
Ask participants if they are familiar with GitHub. If not, give a short explanation of what it is for how to explore the GUI.

Mention GitLab as one of the alternative for a collaborative platform. For example: https://gitlab.tudelft.nl/
:::

(check-in)=
### 3.1.3. Collaborating 
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`5 min`


Participants are invited as collaborators to the **check-in** repository. A template to create a new repository is available in the [check-in template](https://github.com/WorkshopGitcodev/check-in-template).
 Participants must have permission to merge pull requets.

1. Demo on how to invite collaborators using the **check-in** repository.

2. Paticipant accept inviation via email or GitHub notifications.

````{card} 
{bdg-dark}`Exercise 3.1` --- Startig with Collaboration
^^^    

```{include} exercises/L3-ex01.md
```

````

## {octicon}`repo` Episode 2: Collaborative Development for Research Software

### 3.2.1.   Introduction to collaboration in software projects 
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`5 min`


:::{admonition} {octicon}`mortar-board` Instructor's Note
:class: tip
* A Quick introduction to collaborative development. Provide a short explanation on what it is and why it is important for research software development:

> Developing high quality software requires more than programming and technical skill. Exceptionally good programmers can produce high quality software by themselves. 
> But good programmers need to collaborate in order to develop complex, high quality software. &mdash;M. Garcia Alvarez

Topic to cover:
* The software development life cycle.
* Collaborative software development.
* Differences between open and close collaboration.
* Important considerations on open collaboration for research software.
* When a collaborative approach in software development makes sense.
:::

### 3.2.2 Managing Research Software Projects 
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`2 min`


:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
Explain the following topics:

* The importance of project management in developing software.
* Key factors to consider.
    - Purpose
    - People
    - Time
    - Maintenance
* Recommended management strategies for research software projects.

:::

### 3.2.3 Organising Research Team for Collaborative Development 
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`14 min`


:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
**Rores and Responsibilities**
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`3 min`

Describe the responsibilities for each role and why they are important for a research-software development project.

**Roles:**
- Project owner
- Administrator
- Reviewer
- Collaborator

> Questions? 
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`5 min`
:::

````{card} 
{bdg-dark}`Exercise 3.2` --- Roles and Responsibilities
^^^    

```{include} exercises/L3-ex02.md
```

````

## {octicon}`repo` Episode 3: Collaborative Workflows 

### 3.3.1. Documenting Issues
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`8 min`


Issues help to document ideas and tasks in a development project. They facilitate planning, discussing  and tracking the progress of a software project.

:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
Do-along. Instruct participants on how to crate issues in the repository used in [](check-in). Participants create at least one issue in such repository.
:::

Collaborative workflows are estrategies to organise the work of a development team, so that developers can independently can undertake development task while keeping their work aligned with overal project goals. 
Two common estrategies that use version control and collaborative platforms as leverage are:

- The **branching workflow** and
- The **forking workflow**

(branching)=
### 3.3.2. Centralised Workflow: Branching

:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
A short explanation on the branching workflow.
:::

````{card} 
{bdg-dark}`Excercise 3.3` --- Branching workflow 2
^^^    

```{include} exercises/L3-ex03.md
```

````

### 3.3.3. Pull Requests 
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`5 min`


Explaination of what pull request are, and a live demonstation on a code repository ( e.g., GitHub or GitLab).
Then teams follow the steps in the exercise below to create and merge pull requests.

:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
Ask participant if they already have experience with making pull request. Adapt your explanation accordingly.
:::

````{card} 
{bdg-dark}`Exercise 3.4` --- Pull requests
^^^    

```{include} exercises/L3-ex04.md
```

````

### 3.3.4. Shared Workflow: Forking 
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`5 min`


A short explanation on the forking and branching workflow for managing contribution to code reposiotries.


````{card} 
{bdg-dark}`Exercise 3.5` --- Forking Workflow
^^^    

```{include} exercises/L3-ex05.md
```

````

:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
Ask participants if they have Questions.
:::

## {octicon}`log` Lesson Summary
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`5 min`


- SHH is a secure way to connect to Code repositories.
- Collaborative workflows provide a way to organize a team around a software project.
- Workflows: branching (centralized) and forking (shared)
- High quality software requires good planning and management.
- Adopting roles and responsibilities can help teams to organize their work.
