from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator
import csv

with open(BUS_STATION_CSV, encoding='utf-8') as file:
    data = csv.DictReader(file)
    keys = ['Name', 'Street', 'District']
    short_data = [dict(filter(lambda x: x[0] in keys, item.items())) for item in data]


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page = int(request.GET.get('page', 1))
    paginator = Paginator(short_data, 10)
    stations = paginator.get_page(page)
    context = {
        'bus_stations': stations,
        'page': stations,
    }
    return render(request, 'stations/index.html', context)
