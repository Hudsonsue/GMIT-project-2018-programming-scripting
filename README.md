

# GMIT-project-2018-programming-scripting #
Project 2018 for crn 52167 Programming &amp; Scripting. Student **G00219132 SHUDSON**

## Purpose of repository ##
This repository contains the Project of Student **G00219132, Susan Hudson** for module Programming and Scripting. The module is delivered as part of the [Higher Diploma in Data Analytics](https://www.gmit.ie/computing/higher-diploma-science-computing-data-analytics-ict-skills) in GMIT.
It contain the dataset, scripts and notes relating to the project

The project centres on Fisher's [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) 

Prior to this my only experience of Iris was as my requested seasonal flower in my wedding bouquet!

Bouquet *Flowers by Kay Galway*, Photograph  *Yann Studios, Galway*

![iris](iris.jpg)

## Project Brief & scope ##
Project brief and notes: [project brief](https://github.com/Hudsonsue/GMIT-project-2018-programming-scripting/blob/master/project%20brief.pdf)

Whilst the project brief outlined clearly the project minimum requirements the Project Scope was not dictated. Following an initial period of exploration of the dataset I decided to scope in line with personal goals as outlined below. I therefore decided to use similar analysis to work tasks that I would normally perform in Excel/SQL such as group by statistics, plots and outputting of results to files.

* General statistics on entire dataset. 
* Statistics at species level. 
* Produce some graphs and learn how to save these.
* Learn how to save output of statistics to file.

* As this is a new course and, in my worklife I have an interest in student retention, I decided to also document within the 'readme' personal goals, challenges and lessons learned. These sections can be found towards the end of this readme.
 
## Exercise files within this repository ##
*	project brief.pdf – Project Instructions document by Dr Ian McLouglin
*	iris.csv - the Iris dataset used in irisdatset.py [data](https://archive.ics.uci.edu/ml/datasets/iris)[14]
*	check_iriscsv.py – used as a check to ensure Iris dataset opened OK within repository
*	irisdataset.py – this contains the majority of the python code for this project. Some of the code involves outputs which are saved as:
    * Sepal.png -most recent saved output of sepal scatter plot within irisdataset.py
    * Petal.png -most recent saved output of petal scatter plot within irisdataset.py
    * summary.csv – output from describe function within irisdataset.py
    * generalstats.txt – output of data from irisdataset.py. 
*	seabornplots.py – this contains scripts used to create plots using the seaborn library and the Iris dataset from seaborn. 
* predict.py - this is a simple prediction toolbased on user inputs
*	iris.jpg – a picture used for the readme file

Irisdataset.py and seabornplots.py contain may additional comments and references not contained herein.

**Run Irisdataset.py**
The programme imports various libraries and reads the iris dataset using Pandas (without headers and also with headers added), it creates an array of the dataset and queries outlined below are performed the Iris dataset.
Upon selecting to run the user is prompted to select whether to dislay any text ouput on the terminal or save to file.
If you select to save output you will find it in *generalstats.txt*, otherwise it will display on your terminal. the programme runs through the following tasks:
* using numpy it calculates minimum, maximum and mean of all features, looking at the dataset as a whole. 
* it calculates the same simple satistics at species level.
* it outputs sample counts per species
* it uses pandas describe to summarise the datset (with added headers) and this output is saved as a csv file, summary.csv.This can be viewed with excel.  
* it then uses describe to produce species level summaries and a for loop is used to minimise repetition of code.
* it outputs and saves as a png file a scatter (using mathplotlib.pyplot) plot of Sepal length & width.
* it outputs and saves as a png file a scatter (using mathplotlib.pyplot) plot of Petal length & width
* it outputs some counts based on conditions, this approach could potentially be used as a basic prediction tool

*Please note* 
* when running irisdataset.py plots remain open and the programme pauses until closed by users. Despite research I was unable to find a way to allow the program to carry on with open plots. 
* I was unable to distinguish species by colour in these plots, I have left as comments some of my attempt to distinguish by colour in the petal characteristics plot code. One approach I was trying was to use if statements to assign colour by species name. I had to stop trying as it was holding up my project!

**Run seabornplots.py**

This programme imports the seaborn library and contains plots based on using seaborn with the Iris dataset. The dataset is also imported from seaborn library.
You will be asked whether or not you wish to display the Iris Dataset, select Y to display, any other selection will result in no display of dataset.

The following plots are contained and will display when the programme is executed. 
* Scatter plot of sepal width & length. This can be run with regression lines if the user wishes (by selecting Y when prompted)
* Scatter plot of petal width & length.
* Histogram based on petal length
* Histogram based on sepal length
* Histogram showing all four characteristics, petal and sepal length and width.
It should be noted that unlike the scatter plots within the irisdataset.py programme the seaborn scatter plots show species  distinguished by colour.

**Run predict.py**
This programme will attempt to predict species type based on user input values for Iris Characteristics. Upon running you will be asked to enter sepal length, sepal width, petal length and petal width. The programme will then suggest which species the input values may belong to. 
it should be noted that this is very basic and would need further refining. It has only been tested on iris dataset values!

## Code language ##
All coding is [Python 3.6.5](https://www.python.org/)

# Fishers Dataset – who & why? #
Sir Ronald Fisher (1890-1962) was a British geneticist and statistician. He was schooled in [Harrow Public School](https://www.harrowschool.org.uk/) and gained a first in Astronomy from [Cambridge University](https://www.cam.ac.uk/).

It was in his 1936 paper *The use of multiple measurements in taxonomic problems*[1] that the Iris Dataset was introduced. The dataset is a set of measurements (cm) of both Petal and Sepal length and width across three species of Iris. There are 50 measurements for each of species, *Iris setosa*, *Iris virginica* and *Iris versicolor*.
The data was used by Fisher to develop a linear discriminant model to distinguish species from each other. 
The Dataset is used as a dataset for testing purposes in computer science; it is used also to explore data mining. 
Whilst researching the dataset and use thereof I came across a [techopedia definition](https://www.techopedia.com/definition/32880/iris-flower-data-set) which I felt summed it up nicely.

One might question why such an innocuous group of measurements is so widely used and during my research I found the following which I felt was a great explanation for a novice to the area of data analytics such as myself, [stack exchange Q/A](https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching)

# Investigation Methodology #
Initial investigation of the dataset revolved around using python skills learnt to produce general stats: Maximum, minimum, mean and counts. This was done at overall level and at species level. 
Python tutorial[2] and pyplot tutorial[3] were useful sources of reference throughout.

My next step was to plot he data and to do this I attempted to plot scatter graphs of the main characteristic pairs (petal width and length and sepal length and width). I was somewhat hampered by my failure to change the colour of the individual species. I did succeed in saving the plots and was assisted in doing this by queries others had raised on stackoverflow [6] and chartio [7]

I then used some library features following research on pandas.org[4] and stackoverflow [5], using describe from pandas. I also researched seaborn plots, using the seaborn tutorial [9]. These demonstrated the power of python as what was taking me hours could be done in minutes with the correct library. 

My next challenge was to try and add in some real-life functionality. This took the form of:
*	User input to decide whether to display output on screen or save to file
*	Adding date and time stamp if saving to file, a solution for this was based on an article in www.pythonforbeginners.com [8]
*	Saving output to csv
*	Saving plots to file 

The approach I took was to get code working for one item (for example the sepal length), check output was correct and once happy it was correct I reproduced code for all items. Only when I was happy that all output was correct did I start adding in loops to avoid unnecessary repetition of code. Again I got the loops working for one of my sections of code and then applied the logic elsewhere. 
My final step was to spend some time trying to tidy up my code output. 

# Investigation Findings #
I kept my analysis fairly simple as I wanted to concentrate on my coding skills. 

The dataset contains a total of 150 sets of measurements with equal numbers of each of the three species, *Iris setosa*, *Iris virginica* and *Iris versicolor*.
Sepal Length ranges from 4.3cm to 7.9cm with the *Iris virginica* having the longest Sepals and *Iris setosa* the shortest.
Sepal Width ranges from 5cm to 5.7cm and it is *Iris setosa*  that has the widest sepals with *Iris versicolor* having the narrowest sepals.
Petal Length ranges from 3.6cm to 6.9cm and *Iris virginica* has the longest petals and *Iris setosa* the shortest.
Petal Width ranges from 0.1cm to 2.5cm with *Iris virginica* having the widest petals and *Iris setosa* the narrowest.

It can be seen from the scatter plots that *Iris setosa* has characteristics that separate it from the other species both in terms of petal and sepal. It would therefore be relatively easy to identify *Iris setosa* from these two measurements. *Iris visginica* and *Iris versicolor* overlap considerably within the scatter plots and would need to be considered by looking at both petal and sepal.

The final part of my programme was a series of conditions/counts, the logic of these I envisaged might be able to do a prediction of flower species for entered measurements. My aspiration being to load in a new dataset with measurements and predict based on the iris dataset. However to do this would require realistic measurements as otherwise I would be predicting nonsense! 
So instead I have confined myself to the scenatio where someone chances upon an Iris (in their wedding flowers perhaps!!) and wants to know which species it belongs to!
From looking at the analysis done by Patrick Hoey[13]it should be possible to create some conditions based on sepal length, petal length and petal width that would be a reasonable predictor. I attempted to do this and saved the code in the programme called predict.py. it is a very basic tool which would need further refining. 

Seaborn proved to be a very useful tool for plotting graphs and it easy to save output for use elsewhere - tools were embedded in the plots to do this. 

Whilst researching the dataset and the analysis and data visualization of it I came accross other's work on the iris dataset. 
Some sources I found particularly usefule were in websites: pybloggers.com[10], kaggle.com[11] and medium.com[12].

# References #
[1] Fisher, R.A. (1936) The Use of Multiple Measurements in Taxonomic Problems. Annals of Eugenics, 7, 179-188. 
http://dx.doi.org/10.1111/j.1469-1809.1936.tb02137.x 

### The following websites were used for general reference alongside course videos ###

[2] Python Tutorial https://docs.python.org/3/tutorial/
[3] pyplot tutorial https://matplotlib.org/users/pyplot_tutorial.html

### specific tasks /troubleshooting ###

[4] https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html 
[5] https://stackoverflow.com/questions/32835498/pandas-python-describe-formatting-output
[6] https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib
[7] https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/
[8] http://www.pythonforbeginners.com/basics/python-datetime-time-examples
[9] http://seaborn.pydata.org/tutorial.html

### The following were interesting sources to see how other's analysed the Iris Dataset ###

[10] http://www.pybloggers.com/2015/09/my-first-time-using-matplotlib/

[11] https://www.kaggle.com/benhamner/python-data-visualizations

[12] https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342  

[13] http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf

### dataset source ###
[14] https://archive.ics.uci.edu/ml/datasets/Iris/

# Personal Goals, challenges and lessons learned #
### personal goals ###
* Much of my day to day work involves data, whilst reasonably proficient in database interrogation and in the use of excel I am not always sure how to analyse and display different data in a *meaningful* way. I am hoping that what I learn during this module/project can be used and expanded upon in my daily work. 
* Embarking on further education was one of a series of personal goals/challenges I set myself to mark my half century milestone. 
When researching courses [this course](https://www.gmit.ie/computing/higher-diploma-science-computing-data-analytics-ict-skills) ticked a good many of my requirement boxes, interesting, relevant, cheap and potentially useful from a career progression perspective. 

### Challenges & Lessons Learned ###
* Broadband speed was an initial challenge as I was unable to download content to watch offline and had poor home BB. Luck intervened with the timely rollout of High Speed Broadband to my rural location in January.  
* Freeing up enough time to devote to the programming and scripting module proved difficult as it is not a subject that I could dip in and out of for 20 or 30 minutes and I found I needed at least two hours at a time to immerse myself in the module. I eventually found my best working method which was to watch the videos on my PC whilst attempting the examples on a laptop and then making relevant notes. Then and only then did I attempt weekly tasks! 
* Changed way of learning – in past study life all contact was in a classroom/lab environment and the online environment has its challenges as it was easy to get bogged down on small problems which in a classroom environment would have been solved quickly by consulting with peers/academics. I found the concept of discussion boards and google slightly alien and potentially overwhelming. 
* Day to day life and work responsibilities interrupted a few times and I found myself unable to engage in both modules simultaneously, after some initial panic I decided to divert my time fully to whichever of the modules needed it most until these external factors calmed down. I realised that for future modules I would be better placed to block off an evening and stay at work rather than try and work at home, there is a lot to be said for being uncontactable!
* The most important thing I have taken from this project is that for most tasks a tool probably already exists (seaborn for example) and that it is a valuable and powerful skill that I am attaining. Midway through the course (Euler5!) I was wondering if I could ever use this in real life, now I find myself looking at tasks and evaluating whether python would do it better!! 


