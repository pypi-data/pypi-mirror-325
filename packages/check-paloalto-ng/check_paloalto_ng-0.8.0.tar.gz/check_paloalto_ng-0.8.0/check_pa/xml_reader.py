# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from nagiosplugin import CheckError


class XMLReader:
    """Extracts XML Data from Palo Alto REST API."""

    def __init__(self, host, token, verify_ssl, verbose, cmd):
        """Init XML Reader with required information.

        :param host: PaloAlto Firewall
        :param token: Generated token to access REST API.
        :param cmd: Command for the desired XML output.

        :return: the XMLReader object.
        """
        self.host = host
        self.token = token
        self.verify_ssl = verify_ssl
        self.cmd = cmd
        self.verbose = verbose

    def read(self):
        """Performs a request with a given command to the XML API and reads
        the output.

        :return: The XML output parsed by soup.
        """
        requests.packages.urllib3.disable_warnings()

        try:
            resp = requests.get(self.build_request_url(), verify=self.verify_ssl)
        except requests.RequestException as e:
            if self.verbose >= 1:
                raise CheckError("Error connecting to XML API: %s" % str(e))
            else:
                raise CheckError("Error connecting to XML API: %s" % str(e.__class__.__name__))

        if resp.status_code != 200:
            raise CheckError('Expected status code: 200 (OK), returned'
                             ' status code was: %d' % resp.status_code)
        soup = BeautifulSoup(resp.content, "lxml-xml")
        result = soup.response['status']
        if result != 'success':
            raise CheckError('Request didn\'t succeed, result was %s'
                             % result)
        return soup

    def report(self):
        """Performs a request with a given command to the XML API and reads
        the output.

        :return: The XML output parsed by soup.
        """
        requests.packages.urllib3.disable_warnings()

        try:
            resp = requests.get(self.build_request_url(report=True), verify=self.verify_ssl)
        except Exception as e:
            raise CheckError("Error connecting to XML API: %s" % str(e.__class__.__name__))

        if resp.status_code != 200:
            raise CheckError('Expected status code: 200 (OK), returned'
                             ' status code was: %d' % resp.status_code)
        soup = BeautifulSoup(resp.content, "lxml-xml")
        result = soup.report['reportname']
        if result != self.cmd:
            raise CheckError('Request didn\'t succeed, result was %s'
                             % result)
        return soup

    def build_request_url(self,report=False):
        """Creates the URL for a specific XML request.

        :return: URL.
        """
        if report:
            request_url = 'https://%s/api/?key=%s&type=report&async=no&reporttype=dynamic&period=last-15-minutes&reportname=%s' % (
                self.host, self.token, self.cmd)
        else:
            request_url = 'https://%s/api/?key=%s&type=op&cmd=%s' % (
                self.host, self.token, self.cmd)
        return request_url


class Finder:
    @staticmethod
    def find_item(item, s):
        """
        Tries to find an item in a XML-structure.

        :param item: a tag object
        :param s: the search string
        :return: text of the first child-element found
        """
        try:
            return item.find(s).text
        except AttributeError:
            raise CheckError('Couldn\'t find any matching item %s' % s)
