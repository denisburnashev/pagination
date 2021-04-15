from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

CONTENT = []

with open("data-398-2018-08-30.csv") as f:
    bus_stations_dict = csv.reader(f, delimiter=",")
    for stations in bus_stations_dict:
        CONTENT.append([stations[1], stations[4], stations[6]])


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):

    current_page = 1
    next_page_url = 'bus_stations?page='+str(int(request.GET['page']) + current_page)
    paginator = Paginator(CONTENT[0], 10)
    return render(request, 'index.html', context={
        'bus_stations': paginator.page(current_page),
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })

