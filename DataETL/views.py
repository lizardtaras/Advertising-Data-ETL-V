# encoding: utf-8

from django.http import JsonResponse
from django.views.generic import View

from .models import AdvertisingData


class ShowAdvertisingDataView(View):
    http_method_names = ['get']     # In this case I've assumed that we will be using GET method for API

    def get(self, request, *args, **kwargs):

        params = self.get_params(request)

        if params:
            #Prepairing filter values
            filtered_params_dict = {'%s__in' % k: v.split(',') for k,v in params.items()}

            return_data = list(AdvertisingData.objects.filter(**filtered_params_dict).values('date', 'datasource',
                                                                                             'campaign', 'clicks',
                                                                                             'impressions'))
            # Providing only selected choices for datasource_list and campaign
            self.appned_return_data_with_choices(return_data, query=filtered_params_dict)
            return JsonResponse(return_data, safe=False)
        else:
            return_data = list(AdvertisingData.objects.all().values('date', 'datasource', 'campaign', 'clicks',
                                                                    'impressions'))
            # Return all list of choices
            self.appned_return_data_with_choices(return_data)
            return JsonResponse(return_data, safe=False)

    def get_params(self, request):

        available_params = ['datasource', 'campaign']
        request_params = request.GET
        return {i: request_params.get(i) for i in request_params if i in available_params} if request_params else {}

    def get_datasource_and_campaign_choices(self, query=None):

        if not query:
            datasource_queryset = AdvertisingData.objects.all().values_list('datasource', flat=True).distinct()
            campaign_queryset = AdvertisingData.objects.all().values_list('campaign', flat=True).distinct()
        else:
            datasource_queryset = AdvertisingData.objects.filter(**query).values_list('datasource',
                                                                                      flat=True).distinct()
            campaign_queryset = AdvertisingData.objects.filter(**query).values_list('campaign', flat=True).distinct()
        return datasource_queryset, campaign_queryset

    def appned_return_data_with_choices(self, return_data, query=None):
        """In this method we are obtaining choices and selected choices"""

        if query:
            datasource_queryset, campaign_queryset = self.get_datasource_and_campaign_choices(query=query)
            return_data.append({'datasource_list_selected': list(datasource_queryset)})
            return_data.append({'campaign_list_selected': list(campaign_queryset)})
        datasource_queryset, campaign_queryset = self.get_datasource_and_campaign_choices()
        return_data.append({'datasource_list': list(datasource_queryset)})
        return_data.append({'campaign': list(campaign_queryset)})
