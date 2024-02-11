import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

nlp.components

import pandas as pd

amazon_reviews=pd.read_csv(r"C:\Users\bhamr\Downloads\capstone amazon\Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv")

amazon_reviews.head()

reviews_data=amazon_reviews["reviews.text"]    #choosing reviews.text column from dataframe
print(reviews_data)

clean_data=amazon_reviews.dropna(subset=["reviews.text"])   #using dropna function to remove missing values
print(clean_data)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
cl1=clean_data['reviews_without_stopwords'] = clean_data['reviews.text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
print(cl1)

cl1.astype(str)


input=cl1



def ratings(input,index):
    
    result=[]
    result=input[index]
    print(result)
    
    doc=nlp(result)
    p=doc._.polarity   #finding the polarity
    s=doc._.subjectivity   #finding subjectivity
    return (p,s)



t=ratings(input,8)      #change index to select different review
print(f"polarity and subjectivity: {t}")


nlp = spacy.load('en_core_web_md')
my_choice1=nlp(amazon_reviews['reviews.text'][1])   #choosing a review to compare
my_choice2=nlp(amazon_reviews['reviews.text'][2])   #choosing a review to compare
p=my_choice1.similarity(my_choice2)   #finding similarity
print(my_choice1)

print(my_choice2)


print(f"similarity: {p}")