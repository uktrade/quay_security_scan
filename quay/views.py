from django.shortcuts import render
from django.views.generic import TemplateView
from quay.helper.fetch import QuayReport
from quay.helper.push import CreateAndPushGeckoboardDataSet
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class VulnerabilitiesReport(TemplateView):
    template_name = 'report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            # report = QuayReport()
            # geckoboard = CreateAndPushGeckoboardDataSet(
            #     report.vulnerabilitiesReport())
            # geckoboard.push()
            context['status'] = 'OK'
        except:
            context['status'] = 'Error'
        return context
