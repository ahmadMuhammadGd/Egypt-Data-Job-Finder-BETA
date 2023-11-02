from transformers import pipeline
from tqdm import tqdm



def init_classefier():
    classifier = pipeline("zero-shot-classification",
                        model="facebook/bart-large-mnli",
                        device=0)
    candidate_labels = ['Data Analyst', 'Data Scientist', 'Data Engineer', 'Data Entry', 'Data Architect']

    return classifier, candidate_labels



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
                df.at[index, 'Category_Title'] = hypothesis['labels'][0]

        logs.at[index, 'score'] = hypothesis['scores'][0]
        logs.at[index, 'Category_Title'] = hypothesis['labels'][0]

    
    logs.to_csv('logs.csv')

    if initial == len(logs):
        print('everything is well documented')
    else:
        print('something went wrong during the process')


    return df
