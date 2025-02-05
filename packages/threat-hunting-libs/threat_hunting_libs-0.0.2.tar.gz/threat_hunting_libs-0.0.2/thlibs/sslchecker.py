import sys
import subprocess
import ssl
import certifi
import socket
import json
from datetime import datetime
import pytz


class SSLChecker(object):
    """
    SSLCheck

    Class to  check if sites have an SSL Certificate, the SSL details and if that SSL is valid

    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def convert_to_dict(self, data=None):
        """
        convert_to_dict

        Converts a dictionary of tuples of tuples into a Python dictionary.

        """

        # Convert tuples to lists for JSON serialization
        def convert_inner_tuples(item):
            if isinstance(item, tuple):
                return list(convert_inner_tuples(x) for x in item)
            return item

        converted_data = {k: convert_inner_tuples(v) for k, v in data.items()}
        return converted_data

    def get_ssl_full_details_as_dict(self, domain=None, port=None):
        """
        get_ssl_full_details_as_dict

        :param domain:
        :param port:
        :return:

        Returns all the SSL details as a Python dict

        """
        if domain is None:
            domain = self.domain

        if port is None:
            port = self.port

        # With Certifi
        context = ssl.create_default_context(cafile=certifi.where())

        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                ssock.do_handshake()
                cert = ssock.getpeercert()

                ssl_dict = self.convert_to_dict(data=cert)

                return ssl_dict

    def get_ssl_important_details_as_dict(self, domain=None, port=None):
        """
        get_ssl_important_details_as_dict

        :param domain:
        :param port:
        :return:

        Returns only the most important details that we are typically interested in

        """
        ssl_response = self.get_ssl_full_details_as_dict(domain=domain, port=port)

        date_format = "%b %d %H:%M:%S %Y %Z"

        ssl_dict = {}

        ssl_dict['notBefore'] = datetime.strptime(ssl_response['notBefore'],
                                                  date_format).replace(tzinfo=pytz.UTC).strftime("%Y-%m-%dT%H:%M:%S %Z")
        ssl_dict['notAfter'] = datetime.strptime(ssl_response['notAfter'],
                                                 date_format).replace(tzinfo=pytz.UTC).strftime("%Y-%m-%dT%H:%M:%S %Z")
        ssl_dict['caIssuers'] = ssl_response['caIssuers']
        ssl_dict['serialNumber'] = ssl_response['serialNumber']
        ssl_dict['countryName'] = ssl_response['subject'][0][0][1]
        ssl_dict['stateOrProvinceName'] = ssl_response['subject'][1][0][1]
        ssl_dict['localityName'] = ssl_response['subject'][2][0][1]
        ssl_dict['organizationName'] = ssl_response['subject'][3][0][1]
        ssl_dict['issuer'] = {"countryName": ssl_response['issuer'][0][0][1],
                              "organizationName": ssl_response['issuer'][1][0][1],
                              "commonName": ssl_response['issuer'][2][0][1]
                              }

        return ssl_dict

    def verify_has_ssl_certificate(self, domain=None, port=None):
        """
        verify_has_ssl_certificate

        :param domain:
        :param port:
        :return:

        Returns True if the domain has an SSL Certificate

        """
        if domain is None:
            domain = self.domain

        if port is None:
            port = self.port

        # With Certifi
        context = ssl.create_default_context(cafile=certifi.where())

        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                try:
                    ssock.do_handshake()
                    cert = ssock.getpeercert()
                    return True
                except Exception as error:
                    return False

    def verify_ssl_active(self, domain=None, port=None):
        """
        verify_ssl_active

        :param domain:
        :param port:
        :return:

        Returns True if the SSL Certificate is within a valid datetime

        """
        ssl_response = self.get_ssl_full_details_as_dict(domain=domain, port=port)

        date_format = "%b %d %H:%M:%S %Y %Z"

        notAfter = datetime.strptime(ssl_response['notAfter'],
                                     date_format).replace(tzinfo=pytz.UTC)

        notBefore = datetime.strptime(ssl_response['notBefore'],
                                      date_format).replace(tzinfo=pytz.UTC)

        today = datetime.now(pytz.utc)

        valid = False

        if today < notAfter and today >= notBefore:
            valid = True

        return valid
