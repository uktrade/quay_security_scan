import requests
import json
from django.conf import settings


class QuayReport:

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer %s" % settings.QUAY_APP_TOKEN
    }

    org_name = settings.QUAY_ORG_NAME

    def __request(self, uri):
        req = requests.get(settings.QUAY_API_BASE_URL +
                           uri, headers=self.headers)
        return req.json()

    def __repo_list(self):
        result = self.__request(
            '/repository?namespace=' + self.org_name)

        repositories = []

        for repo in result['repositories']:
            repositories.append(repo['name'])
        return repositories

    def __repo_tags(self):

        repo_with_tags_and_manifest = {}

        for repo in self.__repo_list():
            result = self.__request(
                '/repository/' + self.org_name + '/' + repo)

            tags_with_manifest = dict()
            for tag in result['tags']:
                tags_with_manifest.update(
                    {tag: result['tags'][tag]['manifest_digest']})

            repo_with_tags_and_manifest[repo] = tags_with_manifest

        return repo_with_tags_and_manifest

    def vulnerabilitiesReport(self):
        result = None
        report = dict()

        for repo, tags in (self.__repo_tags()).items():
            tags_report = dict()
            for tag, manifest_digest in tags.items():
                result = self.__request(
                    '/repository/' + self.org_name + '/' + repo + '/manifest/' + manifest_digest + '/security?vulnerabilities=true&fixable=true')
                critical = 0
                high = 0
                medium = 0

                if 'Features' in result['data']['Layer']:
                    for vulnerabilities in result['data']['Layer']['Features']:
                        if 'Vulnerabilities' in vulnerabilities:
                            for v in vulnerabilities['Vulnerabilities']:
                                if v['Severity'].lower() == "critical":
                                    critical += 1
                                elif v['Severity'].lower() == "high":
                                    high += 1
                                elif v['Severity'].lower() == "medium":
                                    medium += 1

                    tags_report.update({repo + ':' + tag: {'critical': critical, 'high': high,
                                                           'medium': medium}})

            if tags_report:
                report.update(tags_report)

        return report
