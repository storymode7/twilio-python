# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class ServiceTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://ip-messaging.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "consumption_report_interval": 100,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "default_channel_creator_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_channel_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_service_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "links": {},
                "notifications": {},
                "post_webhook_url": "post_webhook_url",
                "pre_webhook_url": "pre_webhook_url",
                "reachability_enabled": false,
                "read_status_enabled": false,
                "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "typing_indicator_timeout": 100,
                "url": "http://www.example.com",
                "webhook_filters": [
                    "webhook_filters"
                ],
                "webhook_method": "webhook_method",
                "webhooks": {}
            }
            '''
        ))

        actual = self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://ip-messaging.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.services.create(friendly_name="friendly_name")

        values = {
            'FriendlyName': "friendly_name",
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://ip-messaging.twilio.com/v1/Services',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "consumption_report_interval": 100,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "default_channel_creator_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_channel_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_service_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "links": {},
                "notifications": {},
                "post_webhook_url": "post_webhook_url",
                "pre_webhook_url": "pre_webhook_url",
                "reachability_enabled": false,
                "read_status_enabled": false,
                "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "typing_indicator_timeout": 100,
                "url": "http://www.example.com",
                "webhook_filters": [
                    "webhook_filters"
                ],
                "webhook_method": "webhook_method",
                "webhooks": {}
            }
            '''
        ))

        actual = self.client.ip_messaging.v1.services.create(friendly_name="friendly_name")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.services.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://ip-messaging.twilio.com/v1/Services',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://ip-messaging.twilio.com/v1/Services?Page=0&PageSize=50",
                    "key": "services",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 0,
                    "previous_page_url": null,
                    "url": "https://ip-messaging.twilio.com/v1/Services"
                },
                "services": []
            }
            '''
        ))

        actual = self.client.ip_messaging.v1.services.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://ip-messaging.twilio.com/v1/Services?Page=0&PageSize=50",
                    "key": "services",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 1,
                    "previous_page_url": null,
                    "url": "https://ip-messaging.twilio.com/v1/Services"
                },
                "services": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "consumption_report_interval": 100,
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "default_channel_creator_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "default_channel_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "default_service_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "friendly_name",
                        "links": {},
                        "notifications": {},
                        "post_webhook_url": "post_webhook_url",
                        "pre_webhook_url": "pre_webhook_url",
                        "reachability_enabled": false,
                        "read_status_enabled": false,
                        "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "typing_indicator_timeout": 100,
                        "url": "http://www.example.com",
                        "webhook_filters": [
                            "webhook_filters"
                        ],
                        "webhook_method": "webhook_method",
                        "webhooks": {}
                    }
                ]
            }
            '''
        ))

        actual = self.client.ip_messaging.v1.services.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://ip-messaging.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "consumption_report_interval": 100,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "default_channel_creator_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_channel_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_service_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "links": {},
                "notifications": {},
                "post_webhook_url": "post_webhook_url",
                "pre_webhook_url": "pre_webhook_url",
                "reachability_enabled": false,
                "read_status_enabled": false,
                "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "typing_indicator_timeout": 100,
                "url": "http://www.example.com",
                "webhook_filters": [
                    "webhook_filters"
                ],
                "webhook_method": "webhook_method",
                "webhooks": {}
            }
            '''
        ))

        actual = self.client.ip_messaging.v1.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.assertIsNotNone(actual)
