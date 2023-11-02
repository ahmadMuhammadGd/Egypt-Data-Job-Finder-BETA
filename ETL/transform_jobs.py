from transformers import pipeline
from tqdm import tqdm



def init_classefier():
    classifier = pipeline("zero-shot-classification",
                        model="facebook/bart-large-mnli",
                        device=0)
    candidate_labels = ['Data Analyst', 'Data Scientist', 'Data Engineer', 'Data Entry', 'Data Architect', 'Business Analyst']

    return classifier, candidate_labels



def rearrange_df(df):
    df = df[['Title', 'Category_Title', 'Company', 'Job_Type', 'Job_Link', 'Country', 'Governorate', 'City']]


def transform_jobs(df):
    """
    Transforms a DataFrame by classifying job titles and adding a 'Category_Title' column.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing job titles in the 'Title' column.

    Returns:
    - pandas.DataFrame: The transformed DataFrame with a new 'Category_Title' column.

    This function classifies job titles in the 'Title' column using a classifier and adds the predicted
    category label to a new 'Category_Title' column. It also removes rows with empty job titles and
    rows with low classification scores (below 0.5).
    """
    
    #re arrange df for better readability
    rearrange_df(df)
    logs = df.copy()
    logs['score'] = None
    initial = len(df)

    classifier, candidate_labels = init_classefier()

    for index, row in tqdm(df.iterrows(), total=len(df), desc="Transformation Progress"):
        if row['Title'] == '':
            df.drop(index, inplace=True)
        else:
            sequence_to_classify = row['Title']
            hypothesis = classifier(sequence_to_classify, candidate_labels)
            if hypothesis['scores'][0] < 0.5:
                # Drop the row if the condition is met
                df.drop(index, inplace=True)
            else:
                df.at[index, 'Class'] = hypothesis['labels'][0]

        logs.at[index, 'score'] = hypothesis['scores'][0]
        logs.at[index, 'Class'] = hypothesis['labels'][0]

    
    logs.to_csv('logs.csv')

    if initial == len(logs):
        print('everything is well recorder')
    else:
        print('something went wrong during the process')



    return df
