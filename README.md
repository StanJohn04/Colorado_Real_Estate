# EDA of Factors Affecting Home Price in Colorado


# Proposal
The aim of our project is to explore the patterns in the real estate market, mainly house price, with relation to the area that the houses are located. We’ll examine relationships between house price and different variables such as proximity to parks, access to healthcare, schools in the area, ect. We aim to do our analysis on the state of Colorado by using large data sets and access to API's such as Zillow Group Home - Data and APIs.

# Questions to be answered
  * How does healthcare affect home price
  * How does proximity to parks affect home price
  * How do local schools affect home price
  * What other factors have a large impact

# Data Collection and Cleanup
  * We got the Colorado Typlical Home Value data from Zillow Research & Data. Zillow uses the Zillow Home Value Index (ZHVI) to calculate typical home values at  different geographical levels. More information about ZHVI can be found [here](https://www.zillow.com/research/data/)

# Typical Home Value of Colorado Cities - Time Series


# Calculating R-Values


# Park Data


# Mountain Data


# Healthcare Data


# University Data


# Coffee Shop Data
-   Radius = 10 km
-   Using plot_linear_regression, it was found that the r-value is -0.25763.  This would indicate that coffee shops are not very strongly correlated to typical single-family home price.
-	We found that there were fewer coffee shops where the housing prices were higher, and more coffee shops where the typical single-family home price was lower.
-	The results from the API are not entirely what we thought they would be.
-	For example, the data states that there is only 1 coffee shop in Breckenridge.  We know that there are more.  This brings up questions like, “what is classified as a coffee shop?”
-	Given more time, we would like to dig deeper into what data the API is pulling and what specifically defines each supported key in the categories from geoapify.



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

