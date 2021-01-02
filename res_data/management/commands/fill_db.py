from django.core.management.base import BaseCommand, CommandError
from django.shortcuts import render
from django.http import HttpResponse
import csv
from res_data.models import Restaurant
import os


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', help="Please provide a CSV file")

    def handle(self, *args, **options):
        print("Command: Fill db")
        if os.path.isfile(options['csv_file']) and options['csv_file'].endswith(".csv"):
            print(f'csv file: {options["csv_file"]}')
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            with open(options['csv_file'], 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    restaurant_name = row[0]
                    if ',' not in row[1]:
                        reformat = row[1].split(' ', 1)[0]
                        open_days = ','.join(
                            days[days.index(reformat.split('-')[0]):days.index(reformat.split('-')[1])+1])
                        open_hour = row[1].split(' ', 1)[1]
                    else:
                        temp = row[1].split(',')
                        if '-' in temp[0]:
                            reformat = temp[0]
                            open_days1 = ','.join(
                                days[days.index(reformat.split('-')[0]):days.index(reformat.split('-')[1])+1])
                        else:
                            open_days1 = temp[0]
                        if '-' in temp[1].strip().split(' ', 1)[0]:
                            reformat = temp[1].strip().split(' ', 1)[0]
                            open_days2 = ','.join(
                                days[days.index(reformat.split('-')[0]):days.index(reformat.split('-')[1])+1])
                        else:
                            open_days2 = temp[1].strip().split(' ', 1)[0]
                        open_days = open_days1 + ',' + open_days2
                        open_hour = temp[1].strip().split(' ', 1)[1]
                    try:
                        res = Restaurant.objects.get(
                            restaurant_name=restaurant_name)
                    except Restaurant.DoesNotExist:
                        res = Restaurant(
                            restaurant_name=restaurant_name,
                            opening_days=open_days,
                            opening_hours=open_hour
                        )
                        res.save()
                self.stdout.write(self.style.SUCCESS(
                    'Data has been inserted into the database'))
        else:
            raise CommandError('The file does not exists or format is wrong')
