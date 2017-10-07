# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def mainPage (request):
    return render(request, 'mainPage.html')

def posts (request):
    return render(request, 'posts.html')

def getPost(request, id=None):
    return render(request, 'getPost.html',{'id':id})