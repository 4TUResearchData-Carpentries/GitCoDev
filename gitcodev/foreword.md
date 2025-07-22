<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400..700&display=swap" rel="stylesheet">
<style>
h3.dancing {
  font-family: "Dancing Script", cursive;
  font-optical-sizing: auto;
  font-weight: 500;
  font-style: normal;
}
</style>


# Foreword

This website describes a curriculum for a short course on **Version Control and Collaborative Development for Research Software** &mdash;GitCoDev[^logo]. 
The content has been designed specifically for the instructors and not for the learners. A derivative document suited to learners would require adapted design, format and distribution.

## Why do we need a new course on version control?
To any educator reading this, it will be evident that having new topics to teach is not the only reason for designing new teaching materials. 
Changes in learning objectives, the target audience, or the teaching approaches are also valid reasons to 
design and develop new teaching materials.  
Therefore, we could answer the question: *why do we need a new course  about version control with Git?* by simply stating: 
*This course has different learning objectives and teaching approaches*. 

However, more curious readers would like to know in which ways it is different. Which objectives and teaching approaches are different? 
How do these materials compare to the ones by author 'A' or organisation 'O'? 
Which topics are different? And how different are they? 
Are these materials better than those in course 'C'?
Proving scientific evidence of the differences in this course will require spending considerable time dissecting, analysing and comparing with courses covering similar topics.
We have chosen not to engage in that endeavour; instead, we have decided to put our efforts to better use and focus on improving how version control and collaborative development are taught to researchers in technical universities.

Therefore, we do not provide answers to the questions listed above. Though we do not mean to discourage anyone, 
who wishes to put the effort into finding answers from pursuing so. 
Instead, we explain our motivation for developing this course and hope it will satisfy readers who share our motivation. We encourage them to adopt, adapt and reuse the contents of this course.

## Motivation
After teaching introductory courses on version control using Git at the [Delft University of Technology](https://www.tudelft.nl/), 
recurring feedback provided by participants, mainly early-career researchers such as PhD candidates and post-docs, made evident that such courses were highly appreciated and interesting. However, participants also often mentioned that after the courses, they did not feel confident applying what was learned to their research.
They did not know how they could apply the recently acquired skills to their research projects, 
even when such projects involve writing code for themselves or their research groups.

On the other hand, during my role as a research software engineer, I often find myself explaining to early-career and well-established researchers how to adopt and adapt practices prevalent in collaborative software development into their work and the work of their research groups. That meant I could spend less time contributing directly to developing their research software. In more than one case, the benefits of changing how researchers approach research software development were evident. 
However, in those cases, there was also an initial reluctance to change the way developing research software was made. 

These experiences convinced me that researchers would benefit from understanding what software development entitles and adopting some of the best practices without needing to become software engineers themselves. 
If that could be achieved, research software would be of better quality, software as a research output would be easier to maintain, which would increase the likelihood of research results being reproducible for a longer time, the productivity among researchers that continuously engage in the development of research software could be improved; and,  the time spent on directly working on research software, as a software engineer, could be increased to the benefit of the researchers themselves. 

In summary, two situations motivated the development of this course. First, there is a need to increase confidence and independence in applying version control to research software among researchers attending similar courses. 
Second, we are enthusiastic about helping researchers adopt best practices in collaborative development to foster their productivity and improve the quality of research software. 

<h3 class="dancing">Manuel. G. García</h3>

*Research Software Engineer* <br>
*Delft University of Technology*


## Acknowledgements
The original materials for this course were developed by the authors. 
Since then, many people have contributed to improving of the course materials.
We would like to thank the following people for their contributions.

```{include} contributors.md
```

## Content

```{tableofcontents}
```

[^logo]: The GitCoDev logo was inspired by the [Git Logo](https://git-scm.com/downloads/logos) by Jason Long.  
