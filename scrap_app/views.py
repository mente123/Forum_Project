import forum_automation
from forum_automation import *
from django.shortcuts import render


def scrape(email, pswrd, link):
    scrape_link(email, pswrd, link)


def index(request):
    context = {}
    return render(request, 'scrap_app/home.html', context)
