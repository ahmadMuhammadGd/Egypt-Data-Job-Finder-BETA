import streamlit as st
import pandas as pd

#catching data
df = pd.read_csv('data\\transformed.csv')
df = df[['Title', 'Class', 'Company', 'Job_Type', 'Job_Link', 'Country', 'Governorate', 'City']]

print(len(df))


try:
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
except:
    pass

try:
    df.drop(['Unnamed: 0.1'], axis=1, inplace=True)
except:
    pass


data_science_jobs = (df['Class'] == 'Data Scientist').sum()
data_analysis_jobs = (df['Class'] == 'Data Analyst').sum()
data_engineering_jobs = (df['Class'] == 'Data Engineer').sum()
data_entry_jobs = (df['Class'] == 'Data Entry').sum()
business_analysis_jobs = (df['Class'] == 'Business Analyst').sum()
total_jobs = len(df)  # Total number of jobs in the DataFrame


                                                                            
#setting page configurations
st.set_page_config(layout='wide',
                   initial_sidebar_state='expanded',
                   page_title='index',
                   page_icon='📊')


st.markdown(f'# Egypt Data Career Job Finder')
st.markdown(f'## We\'ve got {total_jobs} Jobs')



#side bar
st.sidebar.header('Filters')

job_title = st.sidebar.multiselect(
    'with job title',
    options=df['Class'].unique(),
    default=df['Class'].unique()
)

country = st.sidebar.multiselect(
    'with country',
    options=df['Country'].unique(),
    default=df['Country'].unique()
)

governorate = st.sidebar.multiselect(
    'with governorate',
    options=df['Governorate'].unique(),
    default="Giza"
    )

city = st.sidebar.multiselect(
    'with city',
    options = df[df['Governorate'].isin(governorate)]['City'].unique(),
    default=df[df['Governorate'].isin(governorate)]['City'].unique()
)

# Filter the DataFrame based on selected options
filtered_df = df.query(
    "Class==@job_title & Country==@country & Governorate==@governorate & City==@city"
)



a1, a2, a3 = st.columns(3)
b1, b2, b3 = st.columns(3)

a1.metric("Data science Jobs", data_science_jobs)
a2.metric("Data analysis Jobs", data_analysis_jobs)
a3.metric("Data engineering Jobs", data_engineering_jobs)


a1.metric("Data entry Jobs", data_entry_jobs)
a2.metric("Business analysis Jobs", business_analysis_jobs)
#a3.metric("Data Architect Jobs", data_architect_jobs)

st.divider()

st.markdown(f"## Total Filterd Jobs: {len(filtered_df)}")



@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


exported = convert_df(filtered_df)

st.download_button(
   "Download",
   exported,
   "file.csv",
   "text/csv",
   key='download-csv'
)
# Display the filtered DataFrame
st.table(filtered_df)