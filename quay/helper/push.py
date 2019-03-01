import geckoboard as gb
from django.conf import settings


class CreateAndPushGeckoboardDataSet:
    GECKO_API_TOKEN = settings.GECKO_TOKEN

    def __init__(self, report):
        self._report = report

    def __find_or_create_dataset(self):

        gbClient = gb.client(self.GECKO_API_TOKEN)

        try:
            gbClient.ping()
        except:
            print("GeckoBoard Failed: Wrong API KEY")

        dataset = gbClient.datasets.find_or_create(
            'quay.security.scan.by_name',
            {
                'repository': {'type': 'string', 'name': 'Repository:Tag'},
                'critical': {'type': 'number', 'name': 'Critical'},
                'high': {'type': 'number', 'name': 'High'},
                'medium': {'type': 'number', 'name': 'Medium'}
            },
            ['repository']
        )

        dataset.put([])

        formated_data = []

        for repository, vulnerabilitie in (self._report).items():
            formated_data.append(
                {'repository': repository, 'critical': vulnerabilitie['critical'], 'high': vulnerabilitie['high'], 'medium': vulnerabilitie['medium']})

        dataset.put(formated_data)

    def push(self):
        self.__find_or_create_dataset()
