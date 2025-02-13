# Phishing & Threat Hunting Classes

You may install this directly into your projects by using PIP. See: https://pypi.org/project/threat-hunting-libs/

```bash
pip install threat-hunting-libs
```

## Whois Class

Whois is used to perform lookups on the domain and determine when it was registered, who it was registered with
and what the abuse contact email is on file. The Whois class usage examples are shown below.

$ python3

```python
from thlibs.whois import Whois
w = Whois(domain="example.com")
output = w.get_whois_response()
dict_data = w.parse_whois_response_to_dict(output)

print(dict_data)
{'Domain Name': 'EXAMPLE.COM', 'Registry Domain ID': '2336799_DOMAIN_COM-VRSN', 'Registrar WHOIS Server': 'whois.iana.org', 'Registrar': 'RESERVED-Internet Assigned Numbers Authority', 'Registrar IANA ID': '376', 'Registrar Abuse Contact Email': '', 'Name Server': 'B.IANA-SERVERS.NET', 'DNSSEC': 'signedDelegation', 'DNSSEC DS Data': '370 13 2 BE74359954660069D5C63D200C39F5603827D7DD02B56F120EE9F3A86764247C', 'domain': 'EXAMPLE.COM', 'organisation': 'Internet Assigned Numbers Authority', 'created': '1992-01-01', 'source': 'IANA'}

w.dict_to_json_str(data=dict_data)
'{"Domain Name": "EXAMPLE.COM", "Registry Domain ID": "2336799_DOMAIN_COM-VRSN", "Registrar WHOIS Server": "whois.iana.org", "Registrar": "RESERVED-Internet Assigned Numbers Authority", "Registrar IANA ID": "376", "Registrar Abuse Contact Email": "", "Name Server": "B.IANA-SERVERS.NET", "DNSSEC": "signedDelegation", "DNSSEC DS Data": "370 13 2 BE74359954660069D5C63D200C39F5603827D7DD02B56F120EE9F3A86764247C", "domain": "EXAMPLE.COM", "organisation": "Internet Assigned Numbers Authority", "created": "1992-01-01", "source": "IANA"}'

```


## SSLChecker Class

SSLChecker is used to verify that a website domain has a valid SSL Certificate. 
The SSLChecker class usage examples are shown below.

$ python3

```python
from thlibs.sslchecker import SSLChecker
sslc = SSLChecker(domain='example.com', port=443)

sslc.get_ssl_full_details_as_dict()
{'subject': [[['countryName', 'US']], [['stateOrProvinceName', 'California']], [['localityName', 'Los Angeles']], [['organizationName', 'Internet Corporation for Assigned Names and Numbers']], [['commonName', '*.example.com']]], 'issuer': [[['countryName', 'US']], [['organizationName', 'DigiCert Inc']], [['commonName', 'DigiCert Global G3 TLS ECC SHA384 2020 CA1']]], 'version': 3, 'serialNumber': '0AD893BAFA68B0B7FB7A404F06ECAF9A', 'notBefore': 'Jan 15 00:00:00 2025 GMT', 'notAfter': 'Jan 15 23:59:59 2026 GMT', 'subjectAltName': [['DNS', '*.example.com'], ['DNS', 'example.com']], 'OCSP': ['http://ocsp.digicert.com'], 'caIssuers': ['http://cacerts.digicert.com/DigiCertGlobalG3TLSECCSHA3842020CA1-2.crt'], 'crlDistributionPoints': ['http://crl3.digicert.com/DigiCertGlobalG3TLSECCSHA3842020CA1-2.crl', 'http://crl4.digicert.com/DigiCertGlobalG3TLSECCSHA3842020CA1-2.crl']}

sslc.get_ssl_important_details_as_dict()
{'notBefore': '2025-01-15T00:00:00 UTC', 'notAfter': '2026-01-15T23:59:59 UTC', 'caIssuers': ['http://cacerts.digicert.com/DigiCertGlobalG3TLSECCSHA3842020CA1-2.crt'], 'serialNumber': '0AD893BAFA68B0B7FB7A404F06ECAF9A', 'countryName': 'US', 'stateOrProvinceName': 'California', 'localityName': 'Los Angeles', 'organizationName': 'Internet Corporation for Assigned Names and Numbers', 'issuer': {'countryName': 'US', 'organizationName': 'DigiCert Inc', 'commonName': 'DigiCert Global G3 TLS ECC SHA384 2020 CA1'}}

sslc.verify_ssl_certificate()
True

sslc.verify_ssl_active()
True

```

## isPhish Class

isPhish is used to scan website URLs against various services that check for Phishing. This class will require
you to have a valid API Key for each service you intend to use.

You can use any method you like to insert your API Keys into the environment so that they are
static between logins or just available when your application is run. 

The isPhish class usage examples are shown below.

```bash
vim venv/bin/activate

[PASTE YOUR ENV VARIABLES AT THE END OF THE ACTIVATE FILE]

export APIKey_CheckPhish="your_actual_api_key"
export APIKey_PhishTank="your_actual_api_key"

source venv/bin/activate
```

$ python

```python
from thlibs.isphish import isPhish
isp = isPhish()

cpr = isp.scan_with_checkphish(url="https://example.com", scan_type="full")
print(cpr)
{'jobID': '249ad32c-3976-4af4-8d14-54abe2af0beb', 'timestamp': 1738792650318}

r = isp.get_result_from_checkphish(id='249ad32c-3976-4af4-8d14-54abe2af0beb')
print(r)
{'job_id': '249ad32c-3976-4af4-8d14-54abe2af0beb', 'status': 'DONE', 'url': 'https://example.com/', 'url_sha256': '0f115db062b7c0dd030b16878c99dea5c354b49dc37b38eb8846179c7783e9d7', 'disposition': 'clean', 'brand': 'unknown', 'insights': 'https://checkphish.ai/insights/url/1738792650331/0f115db062b7c0dd030b16878c99dea5c354b49dc37b38eb8846179c7783e9d7', 'resolved': False, 'screenshot_path': 'https://bst-prod-screenshots.s3-us-west-2.amazonaws.com/20250205/0f115db062b7c0dd030b16878c99dea5c354b49dc37b38eb8846179c7783e9d7_1738792650331.png', 'scan_start_ts': 1738792650318, 'scan_end_ts': 1738792656866, 'error': False, 'image_objects': [], 'categories': ['domain_purchase']}
```

```python
from thlibs.isphish import isPhish
isp = isPhish()

isp.scan_with_phishtank(url="http://trezor-iouppstart.webflow.io")
{'meta': {'timestamp': '2025-02-06T06:42:58+00:00', 'serverid': 'e5f3084e', 'status': 'success', 'requestid': '172.17.128.1.67a459f21efa92.13439159'}, 'results': {'url': 'http://trezor-iouppstart.webflow.io', 'in_database': True, 'phish_id': 8963829, 'phish_detail_page': 'http://www.phishtank.com/phish_detail.php?phish_id=8963829', 'verified': True, 'verified_at': '2025-02-06T06:12:39+00:00', 'valid': True}}
```


## Creating A PyPi (PIP) Package

If you have added additional libraries/modules or made modifications and would like to create your 
own package you will first need to register to pypi.org, verify your account and turn on 2FA.

Once complete, install the following packages into your Python Virtual Environment.

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install tqdm
python -m pip install --upgrade twine
```

Now, create a setup.py file as follows. Be sure to update the install_requires array with any additional packages 
required by your additions or changes to the code.

```python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="<PACKAGE_NAME>",
    version="0.0.1",
    author="<USERNAME>",
    author_email="<EMAIL ADDRESS>",
    description="Libraries and modules to assist in threat hunting and research.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/<USERNAME>/<PACKAGE_URL>",
    packages=setuptools.find_packages(),
    install_requires=['certifi', 'pytz'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
```

Before pushing the package to PyPI you want to create a file named .pypirc. At least, that is how I learned to do it,
but the username, and password fields no longer seem required as I am still asked for my API key even though it is
included in my .pypirc.

```bash
touch .pypirc
vim .pypirc
```

Insert the following

```ini
[distutils] 
index-servers=pypi

[pypi]
repository: https://upload.pypi.org/legacy/ 
username: <your username>
password: <your api token>

[testpypi]
repository: https://test.pypi.org/legacy/
username: <your username>
password: <your api token>
```

Now, you can push up your package to PyPI.

```bash
python3 setup.py sdist bdist_wheel
python -m twine upload dist/*
```

Congratulations, you have now created your own package.

To test it out, create a test project with a Python Virtual Environment and install your package.

```bash
cd ~/
mkdir test_proj
cd test_proj
python3 -m venv venv
source venv/bin/activate
pip install <PACKAGE_NAME>
touch test.py
vim test.py
```

Write a little code that uses your packages libraries/modules and give it a go!



