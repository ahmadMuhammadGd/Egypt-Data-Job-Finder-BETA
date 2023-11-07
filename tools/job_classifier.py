import pandas as pd
import json

# Function to load the JSON keyword data
def load_keyword_data():
    with open('../data/data_keywords.json', 'r') as file:
        keyword_data = json.load(file)
    return keyword_data


# Function to create an empty keyword score dictionary
def create_empty_keyword_score_dict():
    template = load_keyword_data()
    score_dict = {}
    for keyword in template:
        score_dict[keyword] = 0
    return score_dict


# Function to perform raw classification
def raw_classification(input_string):
    keywords = load_keyword_data()
    keyword_scores = create_empty_keyword_score_dict()
    
    # Preprocess the input string
    input_string = input_string.strip().lower()
    words = input_string.split(' ')
    
    for keyword in keywords:
        for word in words:
            for key in keywords[keyword]:
                if word == key:
                    keyword_scores[keyword] += 1
    
    sorted_keyword_scores = dict(sorted(keyword_scores.items(), key=lambda item: item[1], reverse=True))
    return sorted_keyword_scores


# Function to classify DataFrame rows
def classify_rows(data_frame, column_name):
    data_frame[['Class', 'score']] = None
    
    for index, row in data_frame.iterrows():
        text = row[column_name].lower()
        if 'business' in text or 'data' in text:
            classification_result = raw_classification(text)
            final_result = next(iter(classification_result.keys()))
            score = classification_result[final_result]
            
            if not (score == 0):
                data_frame.at[index, 'Class'] = final_result
                data_frame.at[index, 'score'] = score
            else:
                data_frame.drop(index, inplace = True)
        else:
            data_frame.drop(index, inplace = True)