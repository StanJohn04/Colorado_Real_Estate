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
  * We used pandas to read the categories table from Geoapify Places API into our notebook and we used that together with a for loop to make a requests for every category. We then calculated the r-value using linregress to determine which categories has the strongest correlation

![image](https://user-images.githubusercontent.com/121142680/230936813-de48d539-d0dd-43e7-bdfd-e9d256be4a40.png)
![image](https://user-images.githubusercontent.com/121142680/230937101-9bdbc6f3-a3e5-4a31-97df-10d10335d944.png)


# Park Data
  * Radius 5 km
    * We chose a smalled radius for parks because of the overwhelming number of parks in the larger cities.
    
   ![image](https://user-images.githubusercontent.com/121142680/230937856-309ae78d-8a65-4903-a9b1-166a6a9b27da.png)
  * Using a linear regression the r-value was calculated ar -0.15. This suggests that the number of parks in a city is very loosley correlated with home value
  
  ![image](https://user-images.githubusercontent.com/121142680/230938408-d55d4b9a-3954-4450-830d-639479c1169a.png)


# Mountain Data
- Wanted to see if having more mountains in a city meant more expensive homes in the city.


Figured out how many mountains are in each city and typical home prices in each city. (Bar Graph)
![image](https://user-images.githubusercontent.com/122308689/230981682-38e802c8-2bd5-490c-936f-3c264e64e8cd.png)


Compared typical home prices to number of mountains in the city . (Scatter Plot)
![image](https://user-images.githubusercontent.com/122308689/230981723-eeee079f-0d77-46dc-81bf-1c5c1aca37fb.png)


Had a radius of 10 km because mountains wouldn’t be right in a city, they would be surrounding the city.


Found that there is a very strong correlation between the number of mountains and the home price. The R value was .76 which means there is a 76% chance that the value of homes increases based on the number of mountains. 


# Healthcare Data
•	we defined healthcare base on geoapify definition. Which is define as places that provide healthcare services such as hospitals, clinics, dentist, and pharmacies

![image](https://user-images.githubusercontent.com/121142680/230945125-c0d31beb-537d-4dd2-8ecf-493269d3042d.png)

•	Radius 10 miles 
•	Using plot_linear_regression, it was found that the r-value is -0.24 or a 25% chance that the value of homes decreases as the number of healthcare facilities increases.

![image](https://user-images.githubusercontent.com/121142680/230945188-911c4a1b-b2c5-430d-b4de-2fbb747ff98d.png)


•	Giving more time we would look at access to healthcare in relation to communities instead of cities. 


# University Data

- Radius = 10 km

![University vs  home price](https://user-images.githubusercontent.com/120751287/230527006-0de369f2-981e-46dc-ab8f-2e7ab29a5cd5.png)

- Using plot_linear_regression, it was found that the r-value is: -0.2977860076652728.

![Number of University per City in Colorado](https://user-images.githubusercontent.com/120751287/230526978-d6998971-90f9-4075-9f55-f1aee471a1ff.png)

- Per the bar chart, Colorado Spring has 31 University vs Breckenridge and Frisco with zero. Base on my finding, a strong demand for a good University nearby can drive property values higher. Also, I believe there are limitation to this dataset. In future project, I would expand my supported categories to “education.school” instead of limiting it to “education.university”

# Coffee Shop Data
-   Radius = 10 km

![image](https://user-images.githubusercontent.com/124820451/230524282-31ecf5e4-302f-4c03-a293-bec28fae13aa.png)

-   Using plot_linear_regression, it was found that the r-value is -0.25763.  This would indicate that coffee shops are not very strongly correlated to typical single-family home price.

![image](https://user-images.githubusercontent.com/124820451/230524315-ba2e32b8-48ce-45d3-9485-81e2de22ccf3.png)

-	We found that there were fewer coffee shops where the housing prices were higher, and more coffee shops where the typical single-family home price was lower.

![Screen Shot 2023-04-06 at 7 55 48 PM](https://user-images.githubusercontent.com/124820451/230524935-9579e870-240d-4ee0-9a72-e36d38e611c2.png)

-	The results from the API are not entirely what we thought they would be.
-	For example, the data states that there is only 1 coffee shop in Breckenridge.  We know that there are more.  This brings up questions like, “what is classified as a coffee shop?”
-	Given more time, we would like to dig deeper into what data the API is pulling and what specifically defines each supported key in the categories from geoapify.



# Next Steps
  * Dive deeper into each category and further examine individual results from the API
  * Use population data to better understand how different categories and home value are affected by the population of a city
  * Explore comparisons at different geographical levels
    * Neighborhood level
    * State Level

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

