from django.shortcuts import render, redirect
from .forms import KeywordForm
from .models import Keyword, Trend
import matplotlib.pyplot as plt 
from io import BytesIO
import base64
import numpy as np
import pandas as pd


import requests
from bs4 import BeautifulSoup
from selenium import webdriver



# Create your views here.
def keyword(request):
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('keyword')
    else:
        form = KeywordForm()
        keywords = Keyword.objects.all()

    keywords_dict = {}
    
    for i in range(len(keywords)):
        keywords_dict[i+1] = keywords[i]
         
    context = {
        'form': form,
        'keywords_dict': keywords_dict
    }
    return render(request, 'trends/keyword.html', context)


def keyword_delete(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    trends = Trend.objects.filter(name=keyword.name)
    trends.delete()
    return redirect('keyword')


def get_data(keyword, tool):
    if tool == 'all':
        url = f'https://www.google.com/search?q={keyword}'
    elif tool == 'year':
        url = f'https://www.google.com/search?q={keyword}&tbs=qdr:y'
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    result_stats = soup.select_one('#result-stats')
    return result_stats.text


def crawling_data(tool):
    keywords = Keyword.objects.all()
    trends = Trend.objects.filter(search_period=tool)
    keywords_list = []
    for trend in trends:
        if trend.name not in keywords_list:
            keywords_list.append(trend.name)
    
    for keyword in keywords:
        crawling = get_data(keyword, 'year')
        end_idx = crawling.find('개')
        
        if keyword.name in keywords_list:
            trend = Trend.objects.get(name=keyword.name, search_period=tool)
            trend.result = int(crawling[7:end_idx].replace(',',''))
            trend.save()
            
        else:
            Trend.objects.create(name=keyword.name, result=int(crawling[7:end_idx].replace(',','')), search_period=tool)
    
def make_crawling_histogram(tool):
    trends = Trend.objects.filter(search_period=tool)
    trends_dict = {}

    for trend in trends:
        trends_dict[trend.name] = trend.result
    plt.figure()
    plt.bar(trends_dict.keys(), trends_dict.values())
    # print(trends_dict)
    plt.ylabel('Result')
    plt.title('Technology Trend Analysis')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart_img': f'data:image.png;base64, {image_base64}',
    }
    
    return context




def crawling(request):
    crawling_data('all')
    
    trends = Trend.objects.filter(search_period='all')
    context = {
        'trends': trends
    }
    return render(request, 'trends/crawling.html', context)

def crawling_histogram(request):
    context = make_crawling_histogram('all')
    return render(request, 'trends/crawling_histogram.html', context)



def crawling_advanced(request):
    crawling_data('year')

    context = make_crawling_histogram('year')
    
    return render(request, 'trends/crawling_advanced.html', context)