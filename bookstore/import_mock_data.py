#!/usr/bin/env python

"""
    Script to import book data from .csv file to Model Database DJango
    To execute this script run: 
                                1) manage.py shell
                                2) exec(open('import_mock_data.py').read())
                                or 
                                python manage.py shell < import_mock_data.py
"""

import csv
from api.models import Book

CSV_PATH = '../MOCK_DATA.csv'

contSuccess = 0
# Remove all data from Table
Book.objects.all().delete()

with open(CSV_PATH, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    print('Loading...')
    for row in reader:
        Book.objects.create(**row)
        contSuccess += 1
    print(f'{str(contSuccess)} inserted successfully! ')
    