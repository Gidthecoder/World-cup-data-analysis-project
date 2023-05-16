# World-cup-data-analysis-project
An insightful analysis of all world cup match data with Python, PostgreSQL and PowerBI.
Welcome to the world cup data analysis project. Despite being my first project, it has shown me the importance of using data analysis to gain insights.

## Tools used
- Python and pandas
- SQL and PostgreSQL
- PowerBI

## Phases
### Defining the questions
Before I started the analysis, I had some questions that needed answers. They are:
1. Which side has an advantage in win the world cup finals. Home or away?
2. What percentage of host countries won a world cup they hosted?
3. What percentage of host countries qualified for the finals in the world cup they hosted?
4. Which countries has the most finals appearance and championship.
5. Which world cup had the most total goals.
6. Which world cup had the highest goals per game.
7. Which teams scored the most goals in world cup history.
8. Which teams conceded the most goals in world cup history.

### Data collection
The dataset was gotten from the [kaggle](https://www.kaggle.com/datasets/jahaidulislam/fifa-world-cup-1930-2022-all-match-dataset) website.  I downloaded it as a csv file.

### Data cleaning
I used pandas to:
- Open the csv file.
- Split the ‘match date’ column to Year, Month and Day.
- Remove unnecessary columns: Month, Day, ...

I also used pandas with sqlalchemy and psycorb2 to export the cleaned dataset to my PostgreSQL database.

### Data analysis
I used PostgreSQL and SQL to write some complex statements that answered all of my questions. Here are some of the statements:

QUESTION 1: which side is more likely to win the finals? home or away?

```sql
create table home_away_finals as
select outcome, count(outcome) from world_cup
where stage = 'final'
group by outcome;
```



QUESTION 2: does the host have a chance of winning the world cup

```sql
create table host_finals_win as
select year, host, home_team, away_team, outcome,
case
	when outcome = 'home team win' and host = home_team then 'won'
	when outcome = 'away team win' and host = away_team then 'won'
	else 'lost'
end as won_world_cup
from world_cup
where stage = 'final';
```



QUESTION 3: does the host have a chance of making it to the finals

```sql
create table host_in_finals as
select year, host, home_team, away_team, outcome,
case
	when host = home_team or host = away_team then 'true'
	else 'false'
end as in_final
from world_cup
where stage = 'final';
```


QUESTION 4: which countries has the most finals appearance and championship

```sql
create table team_finals_appearance as
select home_team, count(home_team)  from world_cup
where stage = 'final'
group by home_team
order by home_team asc;

insert into team_finals_appearance
select away_team, count(away_team)  from world_cup
where stage = 'final'
group by away_team
order by away_team asc;

create table finals_appearance as
select home_team as team, sum(count) as appearance 
from team_finals_appearance
group by home_team
order by home_team;

create table winners as
select outcome,
case
	when outcome = 'home team win' then home_team
	when outcome = 'away team win' then away_team
end as winner
from world_cup
where stage = 'final';

create table winners_freq as
select winner, count(winner) 
from winners
group by winner
order by winner;

create table team_appearance_won as
select finals_appearance.team, finals_appearance.appearance, winners_freq.count as won
from finals_appearance
full outer join winners_freq
on finals_appearance.team = winners_freq.winner;


update team_appearance_won
set won = 0
where won is NULL ;
```

check the remaining code [here](https://github.com/Gidthecoder/World-cup-data-analysis-project/blob/main/sql.txt)
### Data visualization
After the analysis, I connected my database to PowerBI, imported the tables, transformed it and used the final result to create a dashboard that visualized the answers to my questions.
![visualization](https://github.com/Gidthecoder/World-cup-data-analysis-project/blob/main/visualization.png)
 
