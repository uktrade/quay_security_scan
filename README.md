# Quay Security Scan

#### Purpose
Purpose of this project is to , fetch vulnerabilities from Orgnization repository in quay and, display the counts of each type of severity per repository per tag (aka branch )

#### Environment Variables
```bash
DEBUG=True
SECRET_KEY=<django-secret-key>
ALLOWED_HOSTS='localhost,127.0.0.1'
QUAY_API_BASE_URL="https://quay.io/api/v1"
QUAY_APP_TOKEN='<quay application token>'
QUAY_ORG_NAME='<org name>'
GECKO_TOKEN='<gecko board token>'
```

#### Usage
To push/update data from Quay to Geckoboard
```
curl -k https://<webhost>/push
```