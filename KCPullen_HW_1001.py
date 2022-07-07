# Keiland Pullen
# DSC 430: Python Programming
# Due Date: 11/26/2019
# Link to video: https://youtu.be/8tKA-NuqJJw
# Link to Second Chance video: https://youtu.be/FAcugzuUA6o
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 1001: Second Chance


from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
from collections import Counter
from urllib.parse import urlparse
from urllib.parse import  urljoin



def analyze(url):
    '''Function to return Visited URL and word frequency on that page along with list of http links at that url.'''

    print('\n \nVisiting', url)

    getTheURL = requests.get(url)                       #get the URL
    data = getTheURL.text                               #capture the text from that URL
    soup = BeautifulSoup(data, 'html.parser')           #user BeautifulSoup module to parse the text
    urls = []                                           #initiate list of URLs
    wordList = []                                       #initiate list of words 

    for link in soup.find_all('a'):                     #BeautifulSoup module to find all anchor links on page

        urls.append(urljoin(url,link.get('href')))      #for each link, create absolute URL
               
        for allText in soup.find_all('body'):           #get all text within the BODY tag
            content = allText.text
            words = content.lower().split()             #filter each word   
            for eachWord in words:                      
                wordList.append(eachWord)               #add each filtered word into list

    print('\n{:45} {:10} {:5}'.format('URL', 'Word', 'Count'))      # print header

    washWords(wordList, url)                            #send words to be "cleaned". 

    print('\n{:45} {:10}'.format('URL', 'Link'))        
    
    for link in urls:                                   
        print('{:45} {:10}'.format(url, link))          #print each parent url and the link on its page

    return urls



def washWords(myWords, url):
    '''Function to remove non-alpha numeric characters from the word list. '''

    url = url
    cleanWordsList = []
    
    for word in myWords: 
        chars = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
          
        for x in range (0, len(chars)): 
            word = word.replace(chars[x], '') 
              
        if len(word) > 0: 
            cleanWordsList.append(word)
            
    wordDict(cleanWordsList, url)



def wordDict(cleanWordsList, url):
    '''Function to display the 5 most frequent words on a page  '''

    wordCount = {} 
      
    for word in cleanWordsList: 
        if word in wordCount: 
            wordCount[word] += 1
        else: 
            wordCount[word] = 1

    counts = Counter(wordCount) 
      
    freq = counts.most_common(5)                       #the frequency of the top 5 words on a page
    #print(freq)

    for key, value in freq:
        #print (url, key, value)                        # print url, key, value for testing
        print('\n{:45} {:10} {:5}'.format(url, key, value))
        

    
visited = set()                                         #set to contain visited URLs

def crawl(url):
    '''Recursive web crawler'''

    global visited
    visited.add(url)
    #print("Vistited links and urls: ",visited)          # print for testing
    
    links = analyze(url)

    for link in links:
        #print(link)                                    # print links -- for testing
        if link not in visited:
            #try:                                       # try except in testing
            parsedURL = urlparse(link)
            #print(parsedURL.netloc)                    # print URL -- for testing
           
            cdmPath = parsedURL.netloc
           
            if cdmPath == "cdm.depaul.edu":
                crawl(link)
            #except:                                    # try except in testing
            #    pass
    
 
  



    
