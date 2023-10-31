import pandas as pd

def get_cities(cities_url):
    """
    Retrieve a DataFrame containing information about cities in Egypt.

    Parameters:
    cities_url (str): The URL of the CSV file containing city data.

    Returns:
    pd.DataFrame: A DataFrame with city information.
    """
    cities = pd.read_csv(cities_url)

    # Attempt to drop unnecessary columns
    try:
        cities.drop(["id"], axis=1, inplace=True)
    except KeyError:
        print('KeyError, it seems id column isn\'t exist')

    try:
        cities.drop(["city_name_ar"], axis=1, inplace=True)
    except KeyError:
        print('KeyError, it seems city_name_ar column isn\'t exist')

    
    #changing governorate_id to id
    try:
        cities.rename(columns={'governorate_id': 'id'}, inplace=True)
    except KeyError:
        print('KeyError, it seems governorate_id column isn\'t exist')

    return cities

def get_governorates(governorates_url):
    """
    Retrieve a DataFrame containing information about governorates in Egypt.

    Parameters:
    governorates_url (str): The URL of the CSV file containing governorate data.

    Returns:
    pd.DataFrame: A DataFrame with governorate information.
    """
    governorates = pd.read_csv(governorates_url)

    # Attempt to drop unnecessary columns 
    try:
        governorates.drop(["governorate_name_ar"], axis=1, inplace=True)
    except KeyError:
        print('KeyError, it seems governorate_name_ar column isn\'t exist')

    return governorates

