#!/usr/bin/env python

import libtaxii as t
import libtaxii.clients as tc
from libtaxii.common import generate_message_id
from libtaxii.messages_11 import CollectionInformationRequest
from libtaxii.constants import *
from dateutil.tz import tzutc

from urlparse import urlparse

class CollectionRequest:

    def __init__(self, url):
        self.url = urlparse(url)

    def run(self):
        client = tc.HttpClient()
        #client.set_auth_type(tc.AUTH_NONE)
        client.set_use_https(False)

        r = CollectionInformationRequest(generate_message_id())
        col_xml = r.to_xml(pretty_print=True)

        http_resp = client.call_taxii_service2(self.url.netloc, self.url.path, VID_TAXII_XML_11, col_xml)
        taxii_message = t.get_message_from_http_response(http_resp, r.message_id)
        return taxii_message.to_dict()


def main():
    """Send a Feed Information Request to a Taxii 1.0 Service"""
    script = CollectionRequest(url='http://hailataxii.com/taxii-discovery-service/')
    script.run()

if __name__ == "__main__":
    main()
