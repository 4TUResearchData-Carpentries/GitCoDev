# LESSON 4: Managing Collaboration and Best Practices

Lecture notes for the lesson on managing collaboration and best practices. 
Most of the content in this lesson aims to present some best-practices for developing research software and lead an open discussion about when to apply them. 

:::{card} Learning Objectives:

* To understand the importance of contribution guidelines and best practices to manage collaboration in research software projects.
* To organise the activities of a software team that participates in a collaborative development workflow. 
* To understand the impact of code reviews and best practices on software quality.
* To perform code reviews as part of a research software team. 
* To discuss best practices related to code reviews, licensing, citation, semantic versioning, and software releases. 

**Topics:**

{bdg-dark}`managing collaboration`
{bdg-dark}`code reviews`
{bdg-dark}`guidelines for contributions`
{bdg-dark}`licensing`
{bdg-dark}`software citation`
{bdg-dark}`semantic versioning`
{bdg-dark}`software releases`

+++
Materials:

* [Managing collaboration and best practices](https://docs.google.com/presentation/d/1TvWIrBsVNwmEyvZodd4V7gueATeECKMubUqSSYKMyuU/edit?usp=sharing): a presentation with  general information about the lesson and illustrations for supporing the explanations of some of the concepts, and exercises. 
:::

## {octicon}`history` Recapitulation: Collaborative Workflows

Participants complete a group exercise to recapitulate the content of Lesson 3.

````{card} 
{bdg-dark}`Exercise 4.1` --- Implement a Collaborative Workflow 
^^^    

```{include} exercises/L4-ex01.md
```
````


## {octicon}`repo` Episode 1: Managing Collaboration

### 4.1.1. Code Reviews

Provide an introduction in the form of a short lecture on code reviews and their importance in collaborative software development. The following are some points to present and discuss with the participants:
* Reasons for code reviews:
    * Sharing knowledge
    * Spreding ownership
    * Unifiying development practices
    * Quality control

* Aspect to focus on during code reviews.
* Giving feedback as part of the code review process.
* Explicit communication.
* Documenting code revies as an author .
* Best practices in code reviews: do's and don'ts.

:::{admonition} Instructor's Note 
:class: tip
Slides 6 to 16 of the presentation above contain information on this topic.
:::

The instructor demonstrates how to conduct a code review on the collaborative platform used in the course (GitHub, GitLab, etc.). The instructor can use the pull request created in the previous exercise as an example. Depending on the platform, the instructor can show how to:

* Assign reviewers to a pull request/merge request.
* Add comments to the code.
* Suggest changes to the code.
* Approve the pull request/merge request.
* Merge the pull request/merge request into the main branch.
* Close the pull request/merge request.


````{card} 
{bdg-dark}`Exercise 4.2` --- Code Reviews
^^^    

```{include} exercises/L4-ex02.md
```
````


### 4.1.2. Contributing Guidelines

Contributing guidelines are a set of rules and best practices that help to ensure that contributions to a project are consistent, high-quality, and easy to review. They can include information on how to write code, how to format code, how to write commit messages, how to write documentation, and how to submit pull requests.
Provide an explanation on the purpose and importance of contributing guidelines in collaborative software development, and show some examples of the conent in a `CONTRIBUTING.md` file.

Examples:
- [Illuminator project](https://github.com/Illuminator-team/Illuminator/blob/main/CONTRIBUTING.md)
- [FairCode template](https://github.com/manuGil/fair-code/blob/main/CONTRIBUTING.md)

:::{admonition} Instructor's Note 
:class: tip
The instructor facilitess a discussion on the importance of contributing guidelines in collaborative software development before the exercise. Somoe of the topics that can be discussed are:
* Why are contributing guidelines important?
* How contributing guidelines can help to ensure that contributions to a project are consistent, high-quality, and easy to review?
* What are the main components of a contributing guideline and how to adapt them depending of the nature of the project?
* Why contributors should follow the contributing guidelines?
:::


````{card} 
{bdg-dark}`Exercise 4.3` --- Guidelines for Contributions 
^^^    

```{include} exercises/L4-ex03.md
```
````

## {octicon}`repo` Episode 2: Licensing and Citation

Explain and discuss the importance of software licenses and software citation for software. 

### 4.2.1. Open Source Licenses

Explain the importance of open source licenses and how they can help to protect the rights of the authors and users of the software. Discuss the different types of open source licenses, such as permissive licenses (e.g., MIT, Apache) and copyleft licenses (e.g., GPL), and their implications for software development (reuse of soruce code) and distribution. Limit the explantions to the most common licenses, such as MIT, Apache, and GPL without focusing too much on the legal details. 

It is important to mention what it is assumed (by law) when software provides no licensing information. In such cases, it is assumed that software cannot be use by anyone else than the author. 

Also explain why software licensing is diffrent than data and digital content licensing. For exaple, why [Creative Common licenses](https://creativecommons.org/share-your-work/) should not be used for software.

:::{admonition} Instructor's Note
:class: tip

If your institutions has a software policy for research software, it is important to mention it to the particpants, and provide relevant details about guidelines provided by the university to publish open source software.
:::

### 4.2.2. Software Citation

Explain how citations files are used to provide information about the software and its authors, and how they can be used to generate citations in different formats. In GitHub, for example, the citation file is called `CITATION.cff` citation file can be used to generate citations in different formats, such as BibTeX, APA, and MLA.

Provide a demo on how to create `.cff` files using this [CFFInit Tool](https://citation-file-format.github.io/cff-initializer-javascript/)


````{card} 
{bdg-dark}`Exercise 4.4 --- Choosing Licenses and Enabling Software Citation
^^^    

```{include} exercises/L4-ex04.md
```
````

## {octicon}`repo` Episode 3: Releasing Software

Releasing software is an important step in the software development process. It allows developers to share their work with others and to get feedback on their code. It also allows users to use the software and to report bugs or issues.


### 4.3.1. Semantic Versioning

Explain the concept of [semantic versioning](https://semver.org/) and how it helps to have a common language for communicating about software releases. Discuss the different components of a semantic version number, such as major, minor, patch versions, and their implications for software development and distribution.

### 4.3.1. Software Releases
Explain the importance of releasing software and how it can help to ensure that the software is stable, reliable, and easy to use. Discuss the different types of software releases, such as alpha, beta, release candidates and stable releases, and their implications for software development and distribution.

Demonstrate how to create a software release in the collaborative platform used in the course (GitHub, GitLab, etc.). 

Explain and discuss the role and importance of [keeping a changelog](https://keepachangelog.com/en/1.0.0/) file in the software repository. A changelog file is a file that contains a list of changes made to the software, such as bug fixes, new features, and improvements. It is important to keep a changelog file up to date so that users can see what has changes between releases, and how those changes may affect them.

## {octicon}`log` Lesson Summary
**[5 mins]**

- Code reviews a essential to produce high quality software.
- Be mindful when giving feedback to someone else code.
- Collaborative guidelines let potential collaborators to know how they can contribute to a software.
- It is important to think about citing an licensing your software.
- Use semantic versioning when releasing software.


:::{admonition} Follow-up Material
:class: info

- [A complete guide to code reviews](https://www.swarmia.com/blog/a-complete-guide-to-code-reviews/?utm_term=github%20review%20process&utm_campaign=SRH-REVIEW-EU-EN&utm_source=adwords&utm_medium=ppc&hsa_acc=6644081770&hsa_cam=16463390785&hsa_grp=134848023315&hsa_ad=585675515695&hsa_src=g&hsa_tgt=kwd-1139323406817&hsa_kw=github%20review%20process&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gclid=EAIaIQobChMIzsGZhPiO-gIVgbrVCh1dwABgEAAYASAAEgKVufD_BwE)
- [Code review guidelines for humans](https://phauer.com/2018/code-review-guidelines/)
- [Google's code review  developer guide](https://google.github.io/eng-practices/review/)
- [GitHub pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews)
- [Best practices for reviewing pull requests in GitHub](https://rewind.com/blog/best-practices-for-reviewing-pull-requests-in-github/)
:::