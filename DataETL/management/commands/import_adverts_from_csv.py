# encoding: utf-8

import csv
import datetime
import sys

from django.core.management import base

from ...models import AdvertisingData


class Command(base.BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-p', '--path', type=str, help=u'Path to CSV', )

    def handle(self, *args, **options):

        if not options.get('path'):
            print u'Please provide CSV file!'
            sys.exit(1)

        self.path = options['path']

        sheet = open(self.path, 'r')
        csv_reader = csv.reader(sheet, delimiter=',')
        csv_reader.next()
        counter = 0
        for row in csv_reader:
            csv_data={
                'date': datetime.datetime.strptime(row[0], '%d.%m.%Y'),
                'datasource': row[1],
                'campaign': row[2],
                'clicks': row[3],
                'impressions': row[4],
            }
            try:
                AdvertisingData.objects.create(**csv_data)
                counter += 1
            except ValueError:
                pass
        print u"Imported %s records from CSV" % counter
