from django.shortcuts import render

from newsapi import NewsApiClient
  
# Create your views here. 
def index(request):
      
    newsapi = NewsApiClient(api_key ='d413baca255341cf95e18dc6a7b4de1b')
    top = newsapi.get_top_headlines(sources ='techcrunch')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'index.html', context ={"mylist":mylist})