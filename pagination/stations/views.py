from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    with open('data-398-2018-08-30.csv') as file:
        reader = csv.DictReader(file)
        content = list(reader)
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
