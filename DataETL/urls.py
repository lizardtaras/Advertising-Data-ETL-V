from django.conf.urls import url

from .views import ShowAdvertisingDataView

urlpatterns = [
    url('showadvertisingview/', ShowAdvertisingDataView.as_view()),
]
