from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
import urllib.parse


CONTENT = []

with open("data-398-2018-08-30.csv") as f:
    bus_stations_dict = csv.DictReader(f, delimiter=",")
    for stations in bus_stations_dict:
        CONTENT.append({'Name': stations['Name'], 'Street': stations['Street'], 'District': stations['District']})


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):

    current_page = int(request.GET.get('page', 1))
    params_next_page = {'page': current_page+1}
    params_prev_page = {'page': current_page-1}
    next_page_params = urllib.parse.urlencode(params_next_page)
    prev_page_params = urllib.parse.urlencode(params_prev_page)
    next_page_url = reverse('bus_stations')+'?'+next_page_params
    prev_page_url = reverse('bus_stations')+'?'+prev_page_params
    paginator = Paginator(CONTENT, 10)
    page = paginator.page(current_page)
    return render(request, 'index.html', context={
        'bus_stations': page,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
