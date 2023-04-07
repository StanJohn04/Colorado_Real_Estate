# EDA of Factors Affecting Home Price in Colorado


# Proposal
The aim of our project is to explore the patterns in the real estate market, mainly house price, with relation to the area that the houses are located. We’ll examine relationships between house price and different variables such as proximity to parks, access to healthcare, schools in the area, ect. We aim to do our analysis on the state of Colorado by using large data sets and access to API's such as Zillow Group Home - Data and APIs.

# Questions to be answered
  * How does healthcare affect home price
  * How does proximity to parks affect home price
  * How do local schools affect home price
  * What other factors have a large impact

# Data Collection and Cleanup
  * We got the Colorado Typical Home Value data from Zillow Research & Data. Zillow uses the Zillow Home Value Index (ZHVI) to calculate typical home values at  different geographical levels. More information about ZHVI can be found [here](https://www.zillow.com/research/data/)
  
  * After the CSV was read in, some cleanup needed to be done:
    * DataFrame was reduced to only CO entries
    * Data was grouped by City
    * At this point a new DataFrame was created containing the 19 Colorado Cities and their corresponding home value data for the most recent month available (02-2023)
    * This process was completed for Single Family, Top Tier, and Bottom Tier data.
    
  * Using this DataFrame, we made requests to the Geoapify API and stored the latitude and longitude of each city.
  
  ![image](https://user-images.githubusercontent.com/121142680/230521718-1d408748-e3f8-4ddf-9914-c34eadefbc9e.png)
  
  * Using the coordinates from each city we were able to utilize the Geoapify Places API to get data on different categories and then compare them to home values
  
# Typical Home Value of Colorado Cities - Time Series
  * This graph shows that home value in Colorado has been trending upward, with the rate of increase seeming to speed up starting in 2020.

![image](https://user-images.githubusercontent.com/121142680/230521971-6fdcd853-319e-400c-bbf3-9e95f195bef6.png)

# Calculating R-Values


# Park Data


# Mountain Data


# Healthcare Data


# University Data


# Coffe Shop Data


# Next Steps


# Team Members
  * [Stan Johnson](https://github.com/StanJohn04)
  * [Brian Haynes](https://github.com/brianphaynes)
  * [Jennasis Escobar](https://github.com/jenntruly)
  * [Kelsey Abbey](https://github.com/kelseyabbey)
  * [Toan Nguyen](https://github.com/Toan88Nguyen)

# Acknowledgment
The following data was downloaded from [Zillow®](https://www.zillow.com/research/data/):
 * ZHVI Single Family Homes (RawSingleFamily_Neighborhood.csv)
 * ZHVI All Homes - Top Tier (RawTopTierHomes_TimeSeries_City.csv)
 * ZHVI All Homes - Bottom Tier (RawBottomTierHomes_TimeSeries_City.csv)

Our location data is from [Geoapify](https://www.geoapify.com/) and [OpenStreetMap®](https://www.openstreetmap.org/copyright)

