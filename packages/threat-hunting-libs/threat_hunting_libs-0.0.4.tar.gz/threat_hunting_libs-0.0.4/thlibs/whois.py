import sys
import subprocess
import json

class Whois(object):
    """
    Whois

    Class to make whois requests on a Linux system and return a response in text format, dict, and JSON str

    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def get_whois_response(self, domain=None):
        """
        get_whois_response

        :param domain:
        :return:

        Return the whois response for a domain.

        """
        if domain is None:
            domain = self.domain

        command = f"whois {domain}"

        response = subprocess.check_output(command, shell=True)

        # Decode the output from bytes to string
        response = response.decode("utf-8")

        return response

    def parse_whois_response_to_dict(self, data=None):
        """
        parse_whois_response_to_dict

        :param data:
        :return:

        Turn the data from get_whois_data into a dict that can be used as is or parsed to json

        """
        if not data:
            print("You must provide valid whois data..")
            sys.exit(1)

        important_lines = "\n".join(x for x in data.splitlines() if ":" in x)

        data_list = important_lines.split("\n")

        data_dict = {}

        for item in data_list:
            if ":" in item:
                try:
                    key, value = item.split(":")
                    key = key.replace("\t", "").replace("   ", "")

                    if ("Last update" not in key and \
                            "NOTICE" not in key and \
                            "TERMS OF USE" not in key and \
                            "URL of the ICANN" not in key and \
                            ">>>" not in key and \
                            "For more information" not in key and \
                            "Registrar Abuse Contact Phone" not in key and \
                            "under no circumstances will you use this data to" not in key and \
                            "http" not in key and \
                            "to" not in key and \
                            "by the" not in key):
                        value = value.lstrip()
                        value = value.rstrip()

                        data_dict[key] = value
                except Exception as err:
                    pass

        return data_dict

    def dict_to_json_str(self, data=None):
        """
        dict_to_json_str

        :param data:
        :return:

        Turn a dict into a json string. I know, basically the same thing as far as Python is concerned
        
        """
        json_str = json.dumps(data)
        return json_str




