from django.core.management.base import BaseCommand
from quay.helper.fetch import QuayReport
from quay.helper.push import CreateAndPushGeckoboardDataSet


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            report = QuayReport()
            geckoboard = CreateAndPushGeckoboardDataSet(
                report.vulnerabilitiesReport())
            geckoboard.push()
            self.stdout.write(self.style.SUCCESS("OK"))
        except Exception as err:
            print(err)
