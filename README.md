# Advertising-Data-ETL-V
API for Advertising Data project

In order to add data form CSV file to database use management command:

python manage.py import_adverts_from_csv --path='/home/lizardtaras/Downloads/DAMKBAoDBwoDBAkOBAYFCw.csv'

API Usage:
http://127.0.0.1:8080/showadvertisingview/  in order the view all advert Advertising data

To filter: http://127.0.0.1:8081/showadvertisingview/?datasource=Google%20Adwords,Facebook%20Ads&campaign=Like%20Ads

All output will be presented in JSON
