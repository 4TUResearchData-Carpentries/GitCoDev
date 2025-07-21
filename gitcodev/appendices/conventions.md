# Formating Conventions

This website renders content with the [Jupyterbook Theme](https://jupyterbook.org/en/stable/basics/organize.html). The following conventions are used to organise and format content.


## Lessons
A lesson shall be organised as follows:

1. Title.
1. Learning objectives (at the top of the document).
2. Main body containing other elements, including exercises. 
2. Lesson summary with the take-home messages of the lesson.

### Learning Objective

Use a `card` at the beginning of each lesson to state the learning objectives:

````md
:::{card} Learning Objectives:

* Objective 1
* Objective 2

**Topics:**

{bdg-dark}`topic 1`
{bdg-dark}`topic 2`
{bdg-dark}`topic n`

+++
**Materials:**

* A list of additional materials related to the lesson for the instructor. 
* For example: slides.

:::
````

Rendered as:

:::{card} Learning Objectives:

* Objective 1
* Objective 2
  
**Topics:**

{bdg-dark}`topic 1`
{bdg-dark}`topic 2`
{bdg-dark}`topic n`
+++
Materials:
* *[Collaborative software development](https://docs.google.com/presentation/d/1yBy_4r9aHhsUH9AH1s7zLWIQ_h20xNKVYM1somPnz1Q/edit?usp=sharing)*
:::


### Instructor's Notes
Lessons may include explanations or instructions for the instructor. Use the following admonition for including *instructor's notes*:

```md
:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
<Content>
:::
```
Rendered as:

:::{admonition} {octicon}`mortar-board` Instructor's Note 
:class: tip
*The content in italics*
:::

### Time Estimates
Time estimates for each section, subsection or exercise should be included to indicate how much time the instructor has for a particular activity. Use the following format:

````md

### Section/Exercise Title
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`5 min`

````

Rendered as:

### Section Title
{octicon}`clock;1em;sd-text-warning` {bdg-warning-line}`5 min`


### Figures

Figures will be numbered and shall include a caption. Their size can be controlled by adjusting the value for `height`.

````md
```{figure} img/teaching-approach.png
---
height: 400px
name: approach-fig
---
Caption
```
````


Example:

```{figure} ../../img/teaching-approach.png
---
height: 400px
name: approach-fig-example
---
Example figure caption
```

### Lesson's Exercises

Exercises within a lesson are included using a `card`  and the `{include}` directive as follows.

````md
:::{card} 
Exercise 1 
^^^    

```
{include} exercises/L3-ex01.md
```
:::
````

Exercises are numbered for each lesson, starting at one. The header of the lesson includes the word *Exercise* and the number of the exercise. The body of the card contains a reference to the file that describes the exercise (see below).  


## Exercise Files

Exercises are organised in files; each file  contains the following parts:

* A title mentioning the lesson and the episode. 
* The time required to complete the exercise.
* A statement indicating if the exercise should be resolved individually or as a team/group.
* A list of tasks or instructions.
* Admonitions (`note, warning, important`), figures, etc. (optional)
* The answers to the exercise. If the exercise has no answers, that is stated by writing, `No answers are provided for this exercise`. 

Example:

````md
# Lesson 3 Episode 1 --- Clone a repository and make a contribution 

**Time: 10 min**

Please perform the following tasks individually.

1. Clone the Check-in repository via SSH: https://github.com/manuGil/check-in
1. Make a copy of the file `check-in/template.md` in the same directory; 
1. Open your copy of `template.md` and add something to the lists in the file.

:::{admonition} Instructor's Note 
:class: tip
Optional. Include other content
:::


:::{dropdown} Answers
 Use a dropdown to provide answers to the exercise. If none, use the text: "No answers are provided for this exercise."
:::
````
