# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class NewsArticle(models.Model):

    unique_id = models.CharField(max_length=100, null=True)
    news_title = models.CharField(max_length=200, null=True)
    news_url = models.CharField(max_length=500, null=True)
    news_category = models.CharField(max_length=20, null=True)
    upvotes = models.CharField(max_length=10, null=True)
    downvotes = models.CharField(max_length=10, null=True)

    def __unicode__(self):

        return self.unique_id
