#!/usr/bin/env python
# encoding: utf-8

from django.db import models


class AdvertisingData(models.Model):
    """Advertising data model"""

    datasource = models.CharField(verbose_name=u'Datasource', max_length=200)
    campaign = models.CharField(verbose_name=u'Campaign', max_length=200)
    clicks = models.IntegerField(verbose_name=u'Clicks')
    impressions = models.IntegerField(verbose_name=u'Impressions')
    date = models.DateTimeField()

    class Meta:
        verbose_name = u"Advertising Data"

    def __unicode__(self):
        return u"{campaign}".format(**self.__dict__)
