# Phishing & Threat Hunting Classes

You may install this directly into your projects by using PIP. See: https://pypi.org/project/threat-hunting-libs/

```bash
pip install threat-hunting-libs
```

## Whois Class

Whois class usage example

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

SSLChecker class usage example

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



