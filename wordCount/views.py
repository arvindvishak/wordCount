from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def author(request):
    return render(request, 'author.html', {'today': 'February 10, 2020'})

def nba(request):
    return render(request, 'nba.html', {'arvind' : 'sixers'})

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fullText']
    wordlist = fulltext.split()
    textLength = len(wordlist)

    wordDictionary = dict()

    for word in wordlist:

        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
    
    sortedDict = sorted(wordDictionary.items(), key = operator.itemgetter(1), reverse= True)

    return render(request, 'count.html', {'submittedText': fulltext, 'lengths': textLength, 'wordDictionary': sortedDict})