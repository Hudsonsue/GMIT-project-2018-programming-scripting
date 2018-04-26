# GMIT-project-2018-programming-scripting #
Project 2018 for crn 52167 Programming &amp; Scripting. Student **G00219132 SHUDSON**

## Purpose ##
This repository contains the Project of Student **G00219132, Susan Hudson** for module Programming and Scripting. The module is delivered as part of the [Higher Diploma in Data Analytics](https://www.gmit.ie/computing/higher-diploma-science-computing-data-analytics-ict-skills) in GMIT.
It contain the dataset, scripts and notes relating to the project

The project centres around Fisher's [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) 

Prior to this my only experience of Iris was as my requested seasonal flower in my wedding bouquet!

Bouquet *Flowers by Kay Galway*, Photograph  *Yann Studios, Galway*

![iris](iris.jpg)

# Project Brief #
Project brief and notes: [project brief](https://github.com/Hudsonsue/GMIT-project-2018-programming-scripting/blob/master/project%20brief.pdf)

# Project Scope #
Wilst the project brief outlined clearly the project minimum requirements the Project Scope was not dictated. Following an initial period of exploration of the dataset I decided to scope in line with personal goals as outlined below. I therefore decided to use similar analysis to work tasks that I would normally perform in Excel/SQL such as group by statistics, plots and outputting of results to files. 
* General statistics on entire dataset.
* Statistics at species level. 
* Produce some graphs and learn how to save these.
* Learn how to save output of statistics to file.
* As this is a new course and I have an interest in student retention I decided to also document within the 'readme' personal goals, challenges and lessons learned.These sections can be found towards the end of this readme.

### Exercise files within this repository ###
*	Project brief.pdf – Project Instructions document by Dr Ian McLouglin
*	Iris.csv - the Iris dataset used in irisdatset.py., ??
*	Check_iriscsv.py – used as a check to ensure Irisdata set opened OK within repository
*	Irisdataset.py – this contains the majority of the python code for this project. Some of the code involves outputs which are saved as:
    * Sepal.png -most recent saved output of sepal scatter plot within irisdataset.py
    * Petal.png -most recent saved output of petal scatter plot within irisdataset.py
    * Summary.csv – output from describe function within irisdataset.py
    * Generalstats.txt – output of data from irisdataset.py. 
*	Seabornplots.py – this contains scripts used to create plots using the seaborn library and the Iris dataset from seaborn. 
*	Iris.jpg – a picture used for the readme file

Irisdataset.py and seabornplots.py contain additional comments and references not contained herein. 

Please note when running irisdataset.py and seaborn.py that plots remain open and the programme pauses until closed by users. Despite research I was unable to find a way to allow the program to carry on with open plots. 

A more detailed description of irisdataset.py and seabornplots.py is contained within the section ‘investigation methodology’ below.

## Code language ##
All coding is [Python 3.6.5](https://www.python.org/)

# Fishers Dataset – who & why? #
Sir Ronald Fisher (1890-1962) was a British geneticist and statistician. He was schooled in [Harrow Public School](https://www.harrowschool.org.uk/) and studied Astronomy at [Cambridge University](https://www.cam.ac.uk/).
It was in his 1936 paper *The use of multiple measurements in taxonomic problems* that theIris Dataset was introduced. The dataset is a set of measurements (cm) of both Petal and Sepal length and width across three species of Iris. There are 50 measurements for each of species, *Iris setosa*, *Iris virginica* and *Iris versicolor*.
The data was used by Fisher to develop a linear discriminant model to distinguish species from each other. 
The Dataset is used as a dataset for testing purposes in computer science, it is used also to explore data mining. 
Whilst researching the dataset and use thereof I came across a [techopedia definition](https://www.techopedia.com/definition/32880/iris-flower-data-set) which I felt summed it up nicely.

One might question why such an innocuous group of measurements is so widely used and during my research I found the following which I felt was a great explanation for a novice to the area of data analytics such as myself, [stack exchange Q/A](https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching)

## Investigation Methodology ##
Initial investigation of the dataset revolved around using python skills learnt to produce general stats: Maximum, minimum, mean and counts. This was done at overall level and at species level. 
My next step was to plot he data and to do this I attempted to plot scatter graphs of the main characteristic pairs (petal width and length and sepal length and width). I was somewhat hampered by my failure to change the colour of the individual species. 
I then used some library features (describe from pandas and seaborn for plots). This demonstrates the power of python as what was taking me hours could be done in minutes with the correct library. 
My final step was to try and add in some real-life functionality. This took the form of:
*	User input to decide whether to display output on screen or save to file
*	Adding date and time stamp if saving to file, thus allowing users 
*	Saving output to csv
*	Saving plots to file 


## Investigation Findings ##






























## Personal Goals ##
* Much of my day to day work involves data, whilst reasonably proficient in database interrogation and in the use of excel I am not always sure how to analyse and display different data in a MEANINGFUL way. I am hoping that what I learn during this module/project can be used and expanded upon in my daily work. 
* Embarking on further education was one of a series of personal goals/challenges I set myself to mark my half century milestone. 
When researching courses [this course](https://www.gmit.ie/computing/higher-diploma-science-computing-data-analytics-ict-skills) ticked a good many of my requirement boxes, interesting, relevant, cheap and potentially useful from a career progression perspective. 

## Challenges & Lessons Learned ##
* Broadband speed was an initial challenge as I was unable to download content to watch offline and had poor home BB. Luck intervened with the timely rollout of High Speed Broadband to my rural location in January.  
* Freeing up enough time to devote to the programming and scripting module proved difficult as it is not a subject that I could dip in and out of for 20 or 30 minutes and I found I needed at least two hours at a time to immerse myself in the module. I eventually found my best working method which was to watch the videos on my PC whilst attempting the examples on a laptop and then making relevant notes. Then and only then did I attempt weekly tasks! 
* Changed way of learning – in past study life all contact was in a classroom/lab environment and the online environment has its challenges as it was easy to get bogged down on small problems which in a classroom environment would have been solved quickly by consulting with peers/academics. I found the concept of discussion boards and google slightly alien and potentially overwhelming. 
* Day to day life and work responsibilities interrupted a few times and I found myself unable to engage in both modules simultaneously, after some initial panic I decided to divert my time fully to whichever of the modules needed it most until these external factors calmed down. I realised that for future modules I would be better placed to block off an evening and stay at work rather than try and work at home!
* The most important thing I have taken from this project is that for most tasks a tool probably already exists (seaborn for example) and that it is a valuable and powerfuls skill that I am attaining. Midway through the course (Euler5!) I was wondering if I could ever use this in real life, now I find myself looking at tasks and evaluating whether python would do it better!! 


