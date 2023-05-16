# World-cup-data-analysis-project
An insightful analysis of all world cup match data with Python, PostgreSQL and PowerBI.
Welcome to the world cup data analysis project. Despite being my first project, it has shown me the importance of using data analysis to gain insights.

##Tools used
-Python and pandas
-SQL and PostgreSQL
-PowerBI

##Phases
###Defining the questions
Before I started the analysis, I had some questions that needed answers. They are:
-Which side has an advantage in win the world cup finals. Home or away?
-What percentage of host countries won a world cup they hosted?
-What percentage of host countries qualified for the finals in the world cup they hosted?
-Which countries has the most finals appearance and championship.
-Which world cup had the most total goals.
-Which world cup had the highest goals per game.
-Which teams scored the most goals in world cup history.
-Which teams conceded the most goals in world cup history.

##Data collection
The dataset was gotten from the kaggle website.  I downloaded it as a csv file.

##Data cleaning
I used pandas to:
-Open the csv file.
-Split the ‘match date’ column to Year, Month and Day.
-Remove unnecessary columns: Month, Day, ...

I also used pandas with sqlalchemy and psycorb2 to export the cleaned dataset to my PostgreSQL database.

##Data analysis
I used PostgreSQL and SQL to write some complex statements that answered all of my questions. Here are some of the codes:

Data visualization
After the analysis, I connected my database to PowerBI, imported the tables, transformed it and used the final result to create a dashboard that visualized the answers to my questions.
 
