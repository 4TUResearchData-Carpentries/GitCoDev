# Curriculum

Version control is an essential tool in software development. It enables the tracking of changes in the code source and the management of multiple versions. Git is a version control system that allows asynchronous development and is currently the most popular version control system. 

Collaborative development is a software development approach that can help researchers organise their software projects, foster collaboration among their peers and create a community around open-source research software.
Researchers involved or expecting to be involved in developing research software can benefit greatly from mastering the basics of collaborative development.


## Prerequisites

Knowledge and experience in using the command-line interface (CLI) with Unix Shell to perform the following tasks:

* to navigate and visualise the content of directories (folders);
* to create, copy, move and delete files and directories;
* to edit files with terminal-based text editors (such as Nano, vim, emacs, etc);
* to visualise hidden files and directories;
* to redirect and append a command output to a file.

## Tools and Materials

* Unix Shell.
* Git.
* GitHub account or account on a similar platform.
* A laptop with administrative privileges running MacOS, Linux or Windows.

(course-units)=
## Course Units

This course is organised in lessons, episodes and topics. The course consists of **Lessons**. 
Each Lesson is divided into **Episodes** and then into **Topics**. The order in which lessons, 
episodes and topics are organised is the result of extensive discussions on the best way to deliver 
the course. The following aspects played a key role in the organisation:

*  The audience of the course are researchers with previous experience and knowledge at a level between beginner and intermediate user. 
*  Feedback and experiences gathered from delivering the content in three different occasions where most of the audience were PhD candidates. 

The learning objectives and topics of each lesson are presented below. The taxon according to [Bloom's revised taxonomy](https://upload.wikimedia.org/wikipedia/commons/6/6a/Bloom%27s_revised_taxonomy.svg) is indicated in parenthesis. 


````{card} Lesson 1: Fundamental Operations with Git 

**Learning Objectives:**

- To understand the basic operations of version control using Git. (*understand*)
- To use Git to create repositories and commit changes. (*apply*)
- To apply Git operations to track, reverse and delete changes in working documents. (*apply*)
- To organise tracked changes in the Git history. (*understand*)

```{dropdown} Topics
| Episode | Topic                                                       |
| :------ | :---------------------------------------------------------- |
| **1.1** | **Git repositories for version control**                    |
|         | Introduction to Git                                         |
|         | Git command syntax and getting help                         |
|         | Creating an empty repository                                |
| **1.2** | **Tracking changes in working documents**                   |
|         | Tracking changes with the index                             |
|         | Not tracking and stop tracking                              |
|         | Undoing changes with the index                              |
|         | Deleting and renaming tracked files and directories         |
| **1.3** | **Organising tracked changes in a history**                 |
|         | Committing changes with a configured identity and a message |
|         | Inspecting changes using the history                        |
|         | Undoing changes with the history                            |
|         | Marking the history using tags                              |

```
````

````{card} Lesson 2: Branching and Remote Operations

**Learning Objectives:**
- To understand the concept of branches in Git repositories. (*understand*)
- To apply Git operations to create and merge branches in a local Git repository. (*apply*)
- To understand the concepts of bare and remote Git repositories. (*understand*)
- To clone and push changes to remote Git repositories. (*apply*)
- To synchronise changes between local and remote Git repositories. (*apply*)

```{dropdown} Topics
| Episode | Topic                                              |
| :------ | :------------------------------------------------- |
| **2.1** | **Branching**                                      |
| ---     | Create, rename, change, and delete branches        |
| ---     | Develop and compare branches                       |
| ---     | Visualise and merge branches and resolve conflicts |
| **2.2** | **Operations with remotes**                        |
| ---     | Create a bare repositories                         |
| ---     | Cloning and pushing to upstreams                   |
| ---     | Syncing changes between repositories               |

```
````

````{card} Lesson 3: Collaborative Software Development

**Learning Objectives:**

- To understand the key aspects of managing research software projects. (*understand*)
- To make use of issues, code changes, and pull/merge requests to make contributions to a software project hosted in a collaborative platform (*apply*)
- To compose a software development team by assigning roles and responsibilities to a group of developers. (*create*)
- To contribute to the development of research software using a collaborative approach. (*analyse*)
- To choose between a centralised and shared collaborative workflow for a new software project. (*analyse*)
- To create contributions to software projects using one of the Git repository platforms such as GitHub. (*create*) 

```{dropdown} Topics
| Episode | Topic                                                   |
| :------ | :------------------------------------------------------ |
| **3.1** | **Collaborative Platforms**                             |
| ---     | Connecting to code repositories                         |
| ---     | Exploring the GitHub GUI                                |
| ---     | Collaborating                                           |
| **3.2** | **Collaborative Development for Research Software**     |
| ---     | Introduction to collaboration in software projects      |
| ---     | Managing research software projects                     |
| ---     | Organising research teams for collaborative development |
| **3.3** | **Collaborative Workflows**                             |
| ---     | Documenting issues                                      |
| ---     | Centralise workflow: branching                          |
| ---     | Pull requests                                           |
| ---     | Shared workflow: forking                                |

```
````


````{card} Lesson 4: Managing Collaboration and Best Practices

**Learning Objectives:**

- To understand the importance of contribution guidelines and best practices to manage collaboration in research software projects. (*understand*)
- To organise the activities of a software team that participates in a collaborative development workflow. (*create*)
- To understand the impact of code reviews and best practices on software quality. (*understand*)
- To perform code reviews as part of a research software team. (*apply*)
- To discuss best practices related to code reviews, licensing, citation, semantic versioning, and software releases. (*evaluate*)

```{dropdown} Topics
| Episode | Topic                      |
| :------ | :------------------------- |
| **4.1** | **Managing collaboration** |
| ---     | Code Reviews               |
| ---     | Contributing Guidelines    |
| **4.2** | **Licensing and Citation** |
| ---     | Open Source Licenses       |
| ---     | Software Citation          |
| **4.3** | **Releasing Software**     |
| ---     | Semantic Versioning        |
| ---     | Software Releases          |

```
````