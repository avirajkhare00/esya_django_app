# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from service1.models import NewsArticle
from service1.core.submit_blockchain import SubmitBlockchain
from service1.core.get_data import get_data
from service1.core.do_vote import DoVote

import uuid

# Create your views here.

def index_page(request):

    if request.method == 'GET':

        return render(request, 'html/index.html')

    if request.method == 'POST':

        print request.POST

        unique_id = str(uuid.uuid4())

        NewsArticle.objects.create(
            unique_id = unique_id,
            news_title = request.POST['newsTitle'],
            news_url = request.POST['newsUrl'],
            news_category = request.POST['newsCategory'],
            upvotes = '0',
            downvotes = '0'
        )


        SubmitBlockchain(request.POST, unique_id)

        return HttpResponse(200)


def feeds(request):

    return render(request, 'html/feeds.html')

@csrf_exempt
def get_data_endpoint(request):

    return JsonResponse(get_data(), safe=False)

@csrf_exempt
def do_vote(request):

    if request.method == 'POST':

        DoVote(request, request.POST['unique_id'], request.POST['status'])

    return HttpResponse(200)