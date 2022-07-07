# Keiland Pullen
# DSC 430: Python Programming
# Due Date 10/29/2019
# Link to video: https://youtu.be/nUO-OPE-CNo
# Honor Statement: I have not given or received any unauthorized assistance on this assignment
# Assignment 0602: Surf CDM


from urllib.parse import urljoin
from html.parser import HTMLParser
from urllib.request import urlopen
import urllib.request
import collections

class Collector(HTMLParser):
    'collects hyperlink URLs into a list'

    def __init__(self, url):
        'initializes parser, the url, and a list'
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.indent = 0
        self.data = []

    def handle_starttag(self, tag, attrs):
        'collects hyperlink URLs in their absolute format'
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])
                    # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == 'http': # collect HTTP URLs
                        self.links.append(absolute)

    def handle_endtag(self, tag):
        '''prints end tag with an indentation proportional
           to the depth of the tag's element in the document'''
        if tag not in {'br','p'}:
            self.indent -= 4
            #print('{}{} end'.format(self.indent*' ', tag))
         
    def getLinks(self):
        'returns hyperlinks URLs in their absolute format'
        return self.links

    def getData(self):
        ''' getData'''
        return self.data

        
def analyze(url):
    'returns list of http links in url, in absolute format'
    
    print('\n\nVisiting', url)           # for testing

    # obtain links in the web page
    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()          # get list of links

    # compute word frequencies
    content = collector.getData()
    #freq = frequency(content)
    freq = collections.Counter(content)
    
    # print the frequency of every text data word in web page
    print('\n{:45} {:10} {:5}'.format('URL', 'word', 'count'))

    counts = dict()
    for word in freq:
        words = word.decode().split()
        for wordsss in words:
            counts[wordsss] = counts.get(wordsss, 0) + 1
            
        #print('{:45} {:10} {:5}'.format(url, word, freq[word]))
        print('{:45} {:10} {:5}'.format(url, wordsss, counts[wordsss]))
    
    # print the http links found in web page
    print('\n{:45} {:10}'.format('URL', 'link'))
    for link in urls:
        print('{:45} {:10}'.format(url, link))

    return urls

def frequency(content):
    'function to check frequency of word'
    #print(type(content))
    counts = dict()
    for line in content:
        words = line.decode().split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    print(counts)


    
def crawl1(url):
    'recursive web crawler that calls analyze() on every web page'

    # analyze() returns a list of hyperlink URLs in web page url 
    links = analyze(url)

    # recursively continue crawl from every link in links
    for link in links:
        try:  # try block because link may not be valid HTML file
            crawl1(link)   
        except:           # if an exception is thrown,
            pass          # ignore and move on.


visited = set() # initialize visited to an empty set

def crawl2(url):
    '''a recursive web crawler that calls analyze()
       on every visited web page'''

    # add url to set of visited pages
    global visited     # warns the programmer 
    visited.add(url)

    # analyze() returns a list of hyperlink URLs in web page url 
    links = analyze(url)

    # recursively continue crawl from every link in links
    for link in links:
        # follow link only if not visited
        if link not in visited:
            try:
                crawl2(link)
            except:
                pass
