from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from app.data_source import Stations
from urllib.parse import urlencode, urlparse, urlunparse

stations = Stations()
stations.read_file()

paginator = Paginator(stations.data, 10)


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    # скорее всего есть более правильный способ объединить path и query в URL
    url_parsed_base = urlparse(reverse('bus_stations'))

    current_page_number = request.GET.get('page', 1)
    current_page = paginator.get_page(current_page_number)
    current_page_number = current_page.number
    next_page_url = None
    prev_page_url = None

    if current_page.has_next():
        url_parsed_next = url_parsed_base._replace(query=urlencode({'page': current_page.next_page_number()}))
        next_page_url = urlunparse(url_parsed_next)

    if current_page.has_previous():
        url_parsed_next = url_parsed_base._replace(query=urlencode({'page': current_page.previous_page_number()}))
        prev_page_url = urlunparse(url_parsed_next)

    return render_to_response('index.html', context={
        'bus_stations': paginator.page(current_page_number).object_list,
        'current_page': current_page_number,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
