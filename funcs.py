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

def multi_search(df,catlist):
    from config import geoapify_key
    import pandas as pd
    import requests    
    import time

    base_url = 'https://api.geoapify.com/v2/places?'
    radius = int(input("Radius: "))
    params = {
        'apiKey': geoapify_key,
        'limit':500
    }

    total_requests = len(df)*len(catlist)
    counter = 0
    listname = []

    print(f"Starting Data Requests for {len(catlist)} categories!")
    print(f"Total requests: {total_requests}")
    print("-------------------------")

    for cat in catlist:
            
        params['categories'] = cat

        for index, row in df.iterrows():
            counter += 1
            if counter % 50 == 0 and counter > 0:
                print(f"{counter} record(s) processed of {total_requests}.")
            
            lat = row['Latitude']
            lon = row['Longitude']
    
            params['bias'] = f'proximity:{lon},{lat}'
            params['filter'] = f'circle:{lon},{lat},{radius}'
            
            response = requests.get(base_url, params)
            data = response.json()
            if response.status_code == 200:
                df.loc[index, f'{cat}'] = len(data['features'])
            
                print(f"{row['City']}:{len(data['features'])} {cat}")
                time.sleep(1)
            else:
                print(f"Reponse Status:{response.status_code}")
                print(f"skipping {cat} for {row['City']}...")
                continue
    print("-------------------------")
    print("Data Retrieval Complete")
    print("-------------------------")
    return df