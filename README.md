# Ebenezer 2019 Data Analysis

Results for four (4) years (2016-2019) of the Ebenezer Mile Race was analysed to see if any trends could be found in the data. Given the limited number of fields and the small dataset no real trends could be found, with it being noted that male swimmers average time falls off less with age when compared to female swimmers. 
## Background
The Ebenezer Mile swim takes place every year in mid-March at the Mountain Yacht Club, Ebenezer Dam, Haenertsburg. It is a single day race with 4 events, 3x1.6km swims and a single open 3000m swim. The events are split into:
1.	Female Under 13 and Over 30 of age (1.6km)
2.	Male Under 13 and Over 30 of age (1.6km)
3.	Male and Female 13 to 30 of age (1.6km)
4.	Male and Female Open 3000km

With the dam being shallower than previous years the race was a zig-zag between 5 buoys for 2019, where previous years only had a circular 3 buoys route seen in the image below:

![alt text](https://github.com/rokaN8/ebenezer/blob/master/Photos/Ebenezer_Race.jpeg?raw=true)

Obligatory group photo of our group of friends who went swimming on the day:

![alt text](https://github.com/rokaN8/ebenezer/blob/master/Photos/Ebenezer_GroupPhoto.jpg?raw=true)

## Data
Data was manually extracted from https://www.timeme.co.za/results/ where only Gender, Age, Time, Event and Year was compiled into the input dataset. In total 1175 rows of valid/clean data was extracted from the results website. It would have been interesting to also have 'did not finish' (DNF) information for the races however this was not present in the original dataset.
## Results 
### Count
Grouped the ages into buckets of 5 years each due to the small dataset size. From this grouping and chart the 13-18 year bracket has the most competitors on average. This age group spike is due to a club in the area (Warriors) often competing with the rest of the outside swimmers as an event.

![alt text](https://raw.githubusercontent.com/rokaN8/ebenezer/master/Results/Count.png)

### Scatter Plot
Interesting to plot our group of friends in comparison with the general population.

![alt text](https://github.com/rokaN8/ebenezer/blob/master/Results/Scatter.png?raw=true)

### Average Time and Age Trend for Gender
Plot to see that on average male swimmer’s times don’t fall off as quickly as those of females as age increases. It is noted that less swimmers are in these higher age ranges and that it’s also more likely for someone who is fit to continue swimming as they become older skewing the results.

![alt text](https://github.com/rokaN8/ebenezer/blob/master/Results/Trend.png?raw=true)

### Average per Gender for the Years
One of the group members mentioned that 2018 was a tough year for swimming and they felt that the weather or some external factor affected the race. Given that the races (Event 1 – Female and Event 2 - Male) are swam about an hour from each other the average time for these 2 events was calculated. It does seem as if weather could have negatively affected the Male race however this is speculative and not confirmed except for the spike seen below.

![alt text](https://github.com/rokaN8/ebenezer/blob/master/Results/AverageLine.png?raw=true)
![alt text](https://github.com/rokaN8/ebenezer/blob/master/Results/AgeAverageCount.png?raw=true)
