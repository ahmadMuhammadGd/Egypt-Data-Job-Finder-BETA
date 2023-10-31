import streamlit as st
import pandas as pd


df = pd.read_csv('data\\transformed.csv')


print(len(df))


try:
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
except:
    pass

try:
    df.drop(['Unnamed: 0.1'], axis=1, inplace=True)
except:
    pass

data_science_jobs = (df['Category_Title'] == 'Data Scientist').sum()
data_analysis_jobs = (df['Category_Title'] == 'Data Analyst').sum()
data_engineering_jobs = (df['Category_Title'] == 'Data Engineer').sum()
total_jobs = len(df)  # Total number of jobs in the DataFrame


                                                                            

st.set_page_config(layout='wide',
                   initial_sidebar_state='expanded',
                   page_title='index',
                   page_icon='📊')


st.markdown(f'# Egypt Data Career Job Finder')
st.markdown(f'## We\'ve got {total_jobs} Jobs')


st.sidebar.header('Filters')

job_title = st.sidebar.multiselect(
    'Select the job title',
    options=df['Category_Title'].unique(),
    default=df['Category_Title'].unique()
)

country = st.sidebar.multiselect(
    'Select the country',
    options=df['Country'].unique(),
    default=df['Country'].unique()
)

governorate = st.sidebar.multiselect(
    'Select the governorate',
    options=df['Governorate'].unique(),
    default=df['Governorate'].unique()
    )

city = st.sidebar.multiselect(
    'Select the city',
    options = df[df['Governorate'].isin(governorate)]['City'].unique(),
    default=df[df['Governorate'].isin(governorate)]['City'].unique()
)

# Filter the DataFrame based on selected options
filtered_df = df.query(
    "Category_Title==@job_title & Country==@country & Governorate==@governorate & City==@city"
)



a1, a2, a3 = st.columns(3)
a1.metric("Data science Jobs", data_science_jobs)
a2.metric("Data analysis Jobs", data_analysis_jobs)
a3.metric("Data engineering Jobs", data_engineering_jobs)

st.divider()

st.markdown(f"## Total Filterd Jobs: {len(filtered_df)}")



@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


exported = convert_df(filtered_df)

st.download_button(
   "Press to Download",
   exported,
   "file.csv",
   "text/csv",
   key='download-csv'
)
# Display the filtered DataFrame
st.table(filtered_df)