### cat_search() takes a df with City, Latitude, Longitude as arguement
### requests input for geoapify categories param
### returns the number of results found for each city in df
###second arguement is title of returned df col
def cat_search(df,ColTitle):
    try:
        from config import geoapify_key
    except:
        print("Error importing API Key from config...")
        print("Please ensure proper setup.")
        return
    import pandas as pd
    import requests    
    base_url = 'https://api.geoapify.com/v2/places?'
    categories = input('Which Category: ')
    radius = int(input("Radius: "))
    params = {
        'categories':categories,
        'apiKey': geoapify_key,
        'limit':500}

    listname = []

    for index, row in df.iterrows():
        lat = row['Latitude']
        lon = row['Longitude']
    
        params['bias'] = f'proximity:{lon},{lat}'
        params['filter'] = f'circle:{lon},{lat},{radius}'
    
        data = requests.get(base_url, params).json()
    
        listname.append({'City':row['City'], ColTitle:len(data['features'])})

        print(f"{row['City']}:{len(data['features'])}")
        
    list_df = pd.DataFrame(listname)
    return list_df


### retrieves lat and lon for a list containing Cities
###list of city names and state abrreviation as arguements
### currently only supports sesrching for cities in a single state
def coord_search(city_list,state_abv): 
    from config import geoapify_key
    import pandas as pd
    import requests

    listname = [] #empty list to store data
    base_url = "https://api.geoapify.com/v1/geocode/search?"

    for city in city_list:

        city_url = f"{base_url}city={city}&state={state_abv}&apiKey={geoapify_key}"
    
        city_data = requests.get(city_url).json()
        try:
            #store lat and lon from city
            lat = city_data['features'][0]['properties']['lat']
            lon = city_data['features'][0]['properties']['lon']

            #add subset to list
            listname.append({
                "City":city,
                "Latitude":lat,
                "Longitude":lon})
            #log
            print(f"Coords for {city} stored in df")
            
        except:
            print(f'Error Occured with {city}')
            continue

    #convert list to df and return
    list_df = pd.DataFrame(listname)
    return list_df







### multi_serach() is a work in progress... ###

# search_cats = ['healthcare.dentist','healthcare.dentist.orthodontics','healthcare.hospital','healthcare.pharmacy']
# def multi_serach(df,catlist):    
#     base_url = 'https://api.geoapify.com/v2/places?'
#     radius = int(input("Radius: "))
#     params = {
#         'apiKey': geoapify_key,
#         'limit':500
#     }

#     listname = []

#     for cat in catlist:
            
#         params['categories'] = cat
        
#         for index, row in df.iterrows():
#             lat = row['Latitude']
#             lon = row['Longitude']
    
#             params['bias'] = f'proximity:{lon},{lat}'
#             params['filter'] = f'circle:{lon},{lat},{radius}'
            
#             data = requests.get(base_url, params).json()
            
#             listname.append({'City':row['City'], f"Number of {cat}":len(data['features'])})
            
#             print(f"{row['City']}:{len(data['features'])} {cat}")
            
#     list_df = pd.DataFrame(listname)
#     return list_df