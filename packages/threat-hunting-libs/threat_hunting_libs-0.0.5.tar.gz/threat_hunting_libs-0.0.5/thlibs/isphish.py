import os
import sys
import requests
import base64
import json

class isPhish(object):
    """
    isPhish

    Class to check URLs against multiple Phish Verification APIs in a single-shot. PLOW!

    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.APIKey_CheckPhish = os.getenv("APIKey_CheckPhish")
        self.APIKey_PhishTank = os.getenv("APIKey_PhishTank")

    def scan_with_checkphish(self, url=None, scan_type="full"):
        """
        scan_with_checkphish

        :param url:
        :param scan_type:
        :return:

        Scan a website URL with CheckPhish API and return the JSON response that includes the jobID to be
        checked with get_result_from_checkphish for the results

        """
        if url is None:
            url = self.url

        if self.APIKey_CheckPhish is None:
            raise Exception("Sorry, you must set an environment variable for APIKey_CheckPhish before your continue")

        headers = {"Content-Type": "application/json"}

        # scanType: quick|full
        data = {"apiKey": self.APIKey_CheckPhish,
                "urlInfo": {"url": f"{url}"},
                "scanType": f"{scan_type}"
                }

        response = requests.post("https://developers.bolster.ai/api/neo/scan", headers=headers, json=data)

        return response.json()

    def get_result_from_checkphish(self, id=None):
        """
        get_result_from_checkphish

        :param id:
        :return:

        Return the results of a jobID from a CheckPhish scan

        """
        if id is None:
            raise Exception("Sorry, you must provide a job 'id' before your continue")

        if self.APIKey_CheckPhish is None:
            raise Exception("Sorry, you must set an environment variable for APIKey_CheckPhish before your continue")

        headers = {"Content-Type": "application/json"}

        data = {"apiKey": self.APIKey_CheckPhish,
                "jobID": f"{id}",
                "insights": "true"
                }

        response = requests.post("https://developers.bolster.ai/api/neo/scan/status", headers=headers, json=data)

        return response.json()

    def scan_with_phishtank(self, url=None):
        """
        scan_with_phishtank

        :param url:
        :return:

        Return PhishTank results in JSON format
        
        """
        if url is None:
            url = self.url

        headers = {"User-Agent": "phishtank/F4T4L"}

        data = {"url": f"{url}",
                "format": "json"}

        if self.APIKey_PhishTank is not None:
            data['app_key'] = self.APIKey_PhishTank

        response = requests.post("https://checkurl.phishtank.com/checkurl/", headers=headers, data=data)

        return response.json()

