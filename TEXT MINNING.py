# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 06:30:34 2022

@author: Rakesh
"""
########################Task 1 - Snapdeal#####################################
import requests   
from bs4 import BeautifulSoup as bs # Beautifulsoup is for web scrapping...used to scrap specific content 
import re 

import matplotlib.pyplot as plt
from wordcloud import WordCloud

# creating empty reviews list 
snap_reviews=[]


for i in range(1,21):
  ip=[]  
  url1="https://www.snapdeal.com/product/sangitap-bikers-half-face-mask/1804446082/reviews?page="+str(i)
  response = requests.get(url1)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  reviews = soup.find_all("div",attrs={"class","user-review"})# Extracting the content under specific tags  
  for i in range(len(reviews)):
    ip.append(reviews[i].text)  
 
  snap_reviews=snap_reviews+ip  # adding the reviews of one page to empty list which in future contains all the reviews

# writng reviews in a text file 
with open("snap.txt","w",encoding='utf8') as output:
    output.write(str(snap_reviews))
    
    
# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(snap_reviews)

import nltk

# Removing unwanted symbols incase if exists
ip_rev_string = re.sub("[^A-Za-z" "]+"," ", ip_rev_string).lower()
ip_rev_string = re.sub("[0-9" "]+"," ", ip_rev_string)

# words that contained in iphone XR reviews
ip_reviews_words = ip_rev_string.split(" ")
from nltk.corpus import stopwords
stoplist = stopwords.words('english')

with open('C:/Users/Rakesh/Downloads/Text-mining--Natural-language-Processing-main/Text-mining--Natural-language-Processing-main/stop.txt') as sw:
    stopwords = sw.read()

stopwords = stopwords.split("\n")

#removing stop words
ip_reviews_words = [w for w in ip_reviews_words if not w in stoplist]

# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(ip_reviews_words)

# importing word_tokenize from nltk
from nltk.tokenize import word_tokenize
# Passing the string text into word tokenize for breaking the sentences
token = word_tokenize(ip_rev_string)
token

# finding the frequency distinct in the tokens
# Importing FreqDist library from nltk and passing token into FreqDist
from nltk.probability import FreqDist
fdist = FreqDist(token)
fdist

# To find the frequency of top 10 words
fdist1 = fdist.most_common(10)
fdist1

# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()

# Importing Lemmatizer library from nltk and lemmatizing the data
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() 
ip_rev_string = lemmatizer.lemmatize(ip_rev_string)

#Parts of speech tagging and printing POST
for toke in token:
  print(nltk.pos_tag([toke]))


#Named entity recognition
#importing chunk library from nltk
from nltk import ne_chunk
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
tags = nltk.pos_tag(token)
chunk = ne_chunk(tags)
chunk

#Sentimental ANALYSIS 

wordcloud_ip = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_rev_string)

plt.imshow(wordcloud_ip)

#IMPORT POSITIVE WORD FILE
with open("C:/Users/Rakesh/Downloads/Text-mining--Natural-language-Processing-main/Text-mining--Natural-language-Processing-main/positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")
  
#IMPORT NEGATIVE WORD FILE
with open("C:/Users/Rakesh/Downloads/Text-mining--Natural-language-Processing-main/Text-mining--Natural-language-Processing-main/negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

# Positive word cloud
# Choosing the only words which are present in positive words
ip_pos_in_pos = " ".join ([w for w in ip_reviews_words if w in poswords])
wordcloud_pos_in_pos = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_pos_in_pos)

plt.imshow(wordcloud_pos_in_pos)

# negative word cloud
# Choosing the only words which are present in negwords
ip_neg_in_neg = " ".join ([w for w in ip_reviews_words if w in negwords])
wordcloud_neg_in_neg = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_neg_in_neg)

plt.imshow(wordcloud_neg_in_neg)

############################TASK 1 Amazon##########################
import requests #for URL extraxction#
from bs4 import BeautifulSoup as bs ## for webscraping for scraping specific content #
import re #regular expression# 
from wordcloud import WordCloud
import matplotlib.pyplot as plt

##creating empty list#
oneplus = []

for i in range(1,21):
    ip = []
    url = 'https://www.amazon.in/OnePlus-Nord-Bahamas-128GB-Storage/product-reviews/B09RG5R5FG/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'+str(i)
    response = requests.get(url)
    soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
    reviews = soup.find_all("span",attrs={"class","a-size-base review-text review-text-content"})# Extracting the content under specific tags  
    for i in range(len(reviews)):
        ip.append(reviews[i].text)
        
oneplus=oneplus+ip        
        

##writing review in text file#
with open('onplusnord.txt', 'w', encoding='utf8') as output:
    output.write(str(oneplus))
    
##joining all reviews into single paragraph#
ip_rev_string = ' '.join(oneplus)  

import nltk  
from nltk.corpus import stopwords

# Removing unwanted symbols incase if exists
ip_rev_string = re.sub("[^A-Za-z" "]+"," ", ip_rev_string).lower()
ip_rev_string = re.sub("[0-9" "]+"," ", ip_rev_string)        

##words that contain in Iphone Xr review#
ip_review_words = ip_rev_string.split(' ')

stoplist = stopwords.words('english')

with open('C:/Users/Rakesh/Downloads/Text-mining--Natural-language-Processing-main/Text-mining--Natural-language-Processing-main/stopwords_en.txt', 'r') as sw:
    stopwords =sw.read()

stopwords = stopwords.split('\n')  

##removing stop words#
ip_review_words =[w for w in ip_review_words if not w in stoplist]  

##joining all the reviews into single paragraph#
ip_rev_string = ' '.join(ip_review_words)

from nltk.tokenize import word_tokenize
##passing string text into word tokenize for braking sentence#
token =  word_tokenize(ip_rev_string)

##finding frequncecy distinct in th tokens#
##importing Freqdist library from nltk and passing token into Freqdist#
from nltk.probability import FreqDist
fdist = FreqDist(token)
fdist

## for finding  the frequency of top 10 words#
fdist1 = fdist.most_common(10)
fdist1

##Frequncy dist plot#
fdist.plot(30, cumulative=False)
plt.show()

##Lematization#
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
ip_rev_string = lemmatizer.lemmatize(ip_rev_string)

##POS tagging and printing POS tagging#
for toke in token:
    print(nltk.pos_tag([toke]))
    
##Name entity recognition#
from nltk import ne_chunk    
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
tags = nltk.pos_tag(token)
chunk = ne_chunk(tags)
chunk

##sntiment analysis#
wordcloud_ip= WordCloud(background_color='black',
                        width=1800,
                        height = 1400
                        ).generate(ip_rev_string)
plt.imshow(wordcloud_ip)

##importing positive word file#
with open('C:/Users/Rakesh/Downloads/Text-mining--Natural-language-Processing-main/Text-mining--Natural-language-Processing-main/positive-words.txt','r') as pos:
    poswords=pos.read().split('\n')
    
##importing negative word file#
    
with open('C:/Users/Rakesh/Downloads/Text-mining--Natural-language-Processing-main/Text-mining--Natural-language-Processing-main/negative-words.txt','r') as pos:
    negwords=pos.read().split('\n')
    
##positive cloud words#
#choosing only words which are present in positive word#
ip_pos_in_pos = ' '.join([w for w in ip_review_words if w in poswords])    
wordcloud_pos_in_pos= WordCloud(background_color='black',
                        width=1800,
                        height = 1400
                        ).generate(ip_pos_in_pos)
plt.imshow(wordcloud_pos_in_pos)
##negative cloud words#
#choosing only words which are present in negative word#
ip_neg_in_neg = ' '.join([w for w in ip_review_words if w in negwords])    
wordcloud_neg_in_neg= WordCloud(background_color='black',
                        width=1800,
                        height = 1400
                        ).generate(ip_neg_in_neg)
plt.imshow(wordcloud_neg_in_neg)

###################################Task 2 IMDB ####################################################
import requests   
from bs4 import BeautifulSoup as bs # Beautifulsoup is for web scrapping...used to scrap specific content 
import re 

import matplotlib.pyplot as plt
from wordcloud import WordCloud

##create a emmpty list 
imdb_review= []

for i in range(1,21):
  ip=[]  
  url="https://www.imdb.com/title/tt8178634/reviews?ref_=tt_urv"+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  reviews = soup.find_all("div",attrs={"class","content"})# Extracting the content under specific tags  
  for i in range(len(reviews)):
    ip.append(reviews[i].text)

imdb_review=imdb_review+ip   

##writing review in text file #
with open('imdbRRR.txt', 'w', encoding='utf8') as output:
    output.write(str(imdb_review))

##joining all review into single paragraph#
ip_rev_string = ' '.join(imdb_review)

import nltk
# Removing unwanted symbols incase if exists
ip_rev_string = re.sub("[^A-Za-z" "]+"," ", ip_rev_string).lower()
ip_rev_string = re.sub("[0-9" "]+"," ", ip_rev_string)

##words that contain in Iphone Xr review#
ip_reviews_words = ip_rev_string.split(' ')

from nltk.corpus import stopwords
stoplist = stopwords.words('english')

with open("D:/DATA SCIENCE ASSIGNMENT/12 Text_Mining_Problem Statement/stopwords_en.txt","r") as sw:
    stopwords = sw.read()

ip_reviews_words = [w for w in ip_reviews_words if not w in stopwords]

##joining all review into single paragraph#
ip_rev_string = ' '.join(ip_reviews_words)

##simple word cloud #
##plotting wordcloud#
from wordcloud import WordCloud

wordcloud_ip = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_rev_string)

plt.imshow(wordcloud_ip)

# positive words # Choose the path for +ve words stored in system
with open("D:/DATA SCIENCE ASSIGNMENT/12 Text_Mining_Problem Statement/positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")
  
# negative words  Choose path for -ve words stored in system
with open("D:/DATA SCIENCE ASSIGNMENT/12 Text_Mining_Problem Statement/negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")  
  
# Positive word cloud
# Choosing the only words which are present in positive words
ip_pos_in_pos = " ".join ([w for w in ip_reviews_words if w in poswords])
wordcloud_pos_in_pos = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_pos_in_pos)

plt.imshow(wordcloud_pos_in_pos)  


# negative word cloud
# Choosing the only words which are present in negwords
ip_neg_in_neg = " ".join ([w for w in ip_reviews_words if w in negwords])

wordcloud_neg_in_neg = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_neg_in_neg)

plt.imshow(wordcloud_neg_in_neg)




















































