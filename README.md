<!-- Photo below by Hugo Main from Pexels -->

<img src=https://github.com/tn64/surfs_up/blob/main/Resources/pexels-hugo-marin-4716255.png>

# Surf's Up

## Overview

### In the scenario for this module, we are considering opening a surf and ice cream shop on the island of Oahu, HI. In order to accomplish this we will need financial backing and have contacted W Avy, a noted surfer and entrepeneur. He is intrigued by the proposal, but has asked for data to justify the location of the surf/ice cream shop (he had been involved in a similar venture previously, but it had failed due to weather conditions). Throught the module we have been asked for-- and provided-- a variety of data. Avy's last request is that we research historical termperature data for the months of June and December. That information is prvided below, along with the result of queries for precicpitation for those months.

## Results of the Requested Queries

### Choosing June and December provides data showing what the variaton in temperatures for the beginning of summer and the beginning of winter. This should provide data necessary for Avy to determine whether the temperature variation for the two months is acceptable for starting a business that will need to have temperatures conducive both to surfing and eating ice cream in both the summer and the winter.

Below are the results of the temperature data for the two months:

<img src=https://github.com/tn64/surfs_up/blob/main/Resources/June_Temps.png>


<img src=https://github.com/tn64/surfs_up/blob/main/Resources/Dec_Temps.png></br>

### Differences Between Data Sets
The temperature data sets for June and December show pleasant temperatures for both months

- First Difference

The first important difference between the two data sets is the number of temperature reports for the two months. While having nearly 200 fewer temperatures recorded in December than in June may at first seem significant, there are only about 10% fewer records in December than in June, so this difference is most likely not significant. <br/>

- Second Difference

Another difference (important because it shows the lowest temperatures recorded for the two months across the years of the data set) between the two data sets is the difference beteen high and low temperatures for the two months. There is an 8° F difference between minimum temperatures. The December minimum temperature is 8° F cooler (56° F) than the June minimum temperature (64° F).

- Third Difference

A third importabnt difference (important because it again shows how consistent the monthly temperatures are) between the data sets is the difference between the high temperatures for the two months. The maximum high for the month of June was 85° F, and the maximum high for the month of December was 83° F.

## Summary

### As with the previous queries run on the data set for this business proposal, the results of these queries have established generally warm temperatures for the winter and summer query months. While the lowest temperature recorded in the winter as only 56° F, it appears that the termperatures throughtout the year are conducive both to surfing and to eating ice cream. Temperatures themselve seem to support the probability of success for a surf/ice cream shop. 

### However, two additional queries can be run that also bear on how weather might affect such a business. Those queries are for precipitation in the months of June and December. A significant amount of rain might have a negative impact on both sides of the business. 

### Having run these queries (see the code and results below), it appears that the very low precipitation for both months might mean that both sides of the business might flourish throughout the year. Though there are many other aspects to running a successful business, the weather itself should not have a negative impact on either the surf or the ice cream side of the business.

1. June Precipitation

- Code
```
#Convert June precipitation to list
june_prcp = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==6).all()
print(june_prcp)

#Read as pandas DataFrame
june_prcp_df = pd.DataFrame(june_prcp, columns=['date', 'precipitation'])
print(june_prcp_df.to_string(index=False))

#Rename column and describe results
june_new_prcp_df = june_prcp_df.rename(columns={'precipitation': 'June Precipitation'})
june_new_prcp_df.describe()
```

<img src=https://github.com/tn64/surfs_up/blob/main/Resources/June_prcp.png>


2. December Precipitation

- Code
```
#Convert December precipitation to list
dec_prcp = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==12).all()
print(dec_prcp)

#Read as pandas DataFrame
dec_prcp_df = pd.DataFrame(dec_prcp, columns=['date', 'precipitation'])
print(dec_prcp_df.to_string(index=False))

#Rename column and describe results
dec_new_prcp_df = dec_prcp_df.rename(columns={'precipitation': 'December Precipitation'})
dec_new_prcp_df.describe()
```

<img src=https://github.com/tn64/surfs_up/blob/main/Resources/Dec_prcp.png>

Oddly, I now both want to start surfing and eating ice cream on Oahu!
<!-- Photo below by Raryn Elliott from Pexels -->
<img src=https://github.com/tn64/surfs_up/blob/main/Resources/ice_cream_and_palm_trees_pexels-taryn-elliott-4540493.png>
