from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from csv import DictReader


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    current_page = int(request.GET.get('page', 1))

    with open('data-398-2018-08-30.csv', encoding='utf-8') as file:
        reader = DictReader(file)
        address = []
        for i in reader:
            address.append({
                'Name': i['Name'],
                'Street': i['Street'],
                'District': i['District']
            })
    paginator = Paginator(address, 10)
    current_page = int(request.GET.get('page', 1))
    page = paginator.get_page(current_page)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
