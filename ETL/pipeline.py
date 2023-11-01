import pandas as pd
import Egypt_Governorates_and_cities as EGS
import transform_jobs 

# Define URLs for the cities and governorates data
print("downloading CSVs: in progress")

jobs_sheeet_id = '1r6K1HW2RiahoEMTOBcNkqs-9pulLt3Ev'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{jobs_sheeet_id}/export?format=csv", encoding='utf-8')
df.to_csv('data\\df.csv')

cities_url = "https://raw.githubusercontent.com/Tech-Labs/egypt-governorates-and-cities-db/master/cities.csv"
governorates_url = "https://raw.githubusercontent.com/Tech-Labs/egypt-governorates-and-cities-db/master/governorates.csv"

cities = EGS.get_cities(cities_url)
governorates = EGS.get_governorates(governorates_url)
city_govern = cities.merge(governorates, on='id', how='inner')
city_govern.to_csv('data\\city_govern.csv')

print("downloading CSVs: Done")

'''
df = pd.read_csv('data\\df.csv')
city_govern = pd.read_csv('data\\city_govern.csv')

'''
try:
    city_govern.drop('id', axis=1, inplace=True)
except KeyError:
    print('id col at city_govern isn\'t found')


try:
    df.drop(['Unnamed: 0', 'details', 'day_posted'], axis=1, inplace=True)
except KeyError:
    print("a col or set of col from ['Unnamed: 0', 'details', 'day_posted'] aren\'t found")


for col in df.columns:
     df.rename(columns={col: col.title()}, inplace=True)


for index, row in df.iterrows():
  if row['Company'][-1] == '-':
    df.at[index, 'Company'] = row['Company'][:-2]


# Initialize 'Country', 'Governorate', and 'City' columns with None
df[['Country', 'Governorate', 'City']] = None



"""
This loop processes each row in the DataFrame to update the 'Country', 'Governorate', and 'City' columns
based on the information in the 'City_Country' column and the 'city_govern' DataFrame.

1. It splits the 'City_Country' cell into a list of place names.
2. Iterates through the place names to identify and populate 'Country', 'Governorate', and 'City' columns.
3. It attempts to estimate missing 'Governorate' and 'City' information based on the available data.
4. Removes rows where both 'City' and 'Governorate' are missing.
"""
# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    city_country = row['City_Country']
    # Split the 'City_Country' cell into a list of place names
    city_country = city_country.split(',')

    # Iterate through the place names in the list
    for place in city_country:
        transformed_place = place.title().strip()  # Transform the place name to title case
        
        # Check if the transformed place is a governorate name in the 'city_govern' DataFrame
        if transformed_place in city_govern['governorate_name_en'].unique():
            df.at[index, 'Governorate'] = place


        # Check if the transformed place is a city name in the 'city_govern' DataFrame
        elif transformed_place in city_govern['city_name_en'].unique():
            df.at[index, 'City'] = place

        # Check if the transformed place is 'Egypt' and set 'Country' to 'Egypt'
        elif transformed_place == 'Egypt':
            df.at[index, 'Country'] = 'Egypt'

    # If 'Governorate' is still None, attempt to estimate it based on 'City'
    if pd.isna(df.at[index, 'Governorate']) and pd.isna(df.at[index, 'City']):
            # If both 'Governorate' and 'City' are None, drop the row
            df.drop(index=index, inplace=True)

    elif pd.isna(df.at[index, 'Governorate']):
            # Estimate 'Governorate' based on 'City' using 'city_govern' DataFrame
            city = df.at[index, 'City']
            estimated_governorate_filtered_df = city_govern[city_govern['city_name_en'] == city]

            # If 'Governorate' is not None, estimate it based on 'City'
            # else drop the row 
            if not estimated_governorate_filtered_df.empty:
                df.at[index, 'Governorate'] = estimated_governorate_filtered_df['governorate_name_en'].values[0]
                del city, estimated_governorate_filtered_df
            else:
                df.drop(index=index, inplace=True)
            
print((len(df)))


df.drop(['City_Country'], axis=1, inplace=True)
print('\n\n\n\n\n', df.head())


print(df['City'].unique())
df['Governorate'] = df['Governorate'].astype(str)
print('\n\n\n\n', df['Governorate'].unique())


# transforming jobs
df = transform_jobs.trnsform_jobs(df)

df.to_csv('data\\transformed.csv')
