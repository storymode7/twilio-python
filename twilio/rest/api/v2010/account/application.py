# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.instance_context import InstanceContext
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource

from twilio import values
from twilio.base import deserialize, values
from twilio.base.page import Page


class ApplicationList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the ApplicationList

        :param Version version: Version that contains the resource
        :param account_sid: A string that uniquely identifies this resource

        :returns: twilio.rest.api.v2010.application.ApplicationList
        :rtype: twilio.rest.api.v2010.application.ApplicationList
        """
        super(ApplicationList, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Applications.json'.format(**self._solution)

    def create(self, friendly_name, api_version=values.unset,
               voice_url=values.unset, voice_method=values.unset,
               voice_fallback_url=values.unset, voice_fallback_method=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               voice_caller_id_lookup=values.unset, sms_url=values.unset,
               sms_method=values.unset, sms_fallback_url=values.unset,
               sms_fallback_method=values.unset, sms_status_callback=values.unset,
               message_status_callback=values.unset):
        """
        Create a new ApplicationInstance

        :param unicode friendly_name: Human readable description of this resource
        :param unicode api_version: The API version to use
        :param unicode voice_url: URL Twilio will make requests to when relieving a call
        :param unicode voice_method: HTTP method to use with the URL
        :param unicode voice_fallback_url: Fallback URL
        :param unicode voice_fallback_method: HTTP method to use with the fallback url
        :param unicode status_callback: URL to hit with status updates
        :param unicode status_callback_method: HTTP method to use with the status callback
        :param bool voice_caller_id_lookup: True or False
        :param unicode sms_url: URL Twilio will request when receiving an SMS
        :param unicode sms_method: HTTP method to use with sms_url
        :param unicode sms_fallback_url: Fallback URL if there's an error parsing TwiML
        :param unicode sms_fallback_method: HTTP method to use with sms_fallback_method
        :param unicode sms_status_callback: URL Twilio with request with status updates
        :param unicode message_status_callback: URL to make requests to with status updates

        :returns: Newly created ApplicationInstance
        :rtype: twilio.rest.api.twilio.com.2010-04-01.application.ApplicationList
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'ApiVersion': api_version,
            'VoiceUrl': voice_url,
            'VoiceMethod': voice_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceFallbackMethod': voice_fallback_method,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'VoiceCallerIdLookup': voice_caller_id_lookup,
            'SmsUrl': sms_url,
            'SmsMethod': sms_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsStatusCallback': sms_status_callback,
            'MessageStatusCallback': message_status_callback,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return ApplicationInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams ApplicationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode friendly_name: Filter by friendly name
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            friendly_name=friendly_name,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists ApplicationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode friendly_name: Filter by friendly name
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, friendly_name=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ApplicationInstance records from the API.
        Request is executed immediately

        :param unicode friendly_name: Filter by friendly name
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ApplicationInstance
        :rtype: Page
        """
        params = values.of({
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ApplicationPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ApplicationContext

        :param sid: Fetch by unique Application Sid

        :returns: twilio.rest.api.v2010.application.ApplicationContext
        :rtype: twilio.rest.api.v2010.application.ApplicationContext
        """
        return ApplicationContext(
            self._version,
            account_sid=self._solution['account_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a ApplicationContext

        :param sid: Fetch by unique Application Sid

        :returns: twilio.rest.api.v2010.application.ApplicationContext
        :rtype: twilio.rest.api.v2010.application.ApplicationContext
        """
        return ApplicationContext(
            self._version,
            account_sid=self._solution['account_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ApplicationList>'


class ApplicationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ApplicationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: A string that uniquely identifies this resource

        :returns: twilio.rest.api.v2010.application.ApplicationPage
        :rtype: twilio.rest.api.v2010.application.ApplicationPage
        """
        super(ApplicationPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ApplicationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.application.ApplicationInstance
        :rtype: twilio.rest.api.v2010.application.ApplicationInstance
        """
        return ApplicationInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ApplicationPage>'


class ApplicationContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        """
        Initialize the ApplicationContext

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param sid: Fetch by unique Application Sid

        :returns: twilio.rest.api.v2010.application.ApplicationContext
        :rtype: twilio.rest.api.v2010.application.ApplicationContext
        """
        super(ApplicationContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Applications/{sid}.json'.format(**self._solution)

    def delete(self):
        """
        Deletes the ApplicationInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def fetch(self):
        """
        Fetch a ApplicationInstance

        :returns: Fetched ApplicationInstance
        :rtype: twilio.rest.api.twilio.com.2010-04-01.application.ApplicationList
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ApplicationInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def update(self, friendly_name=values.unset, api_version=values.unset,
               voice_url=values.unset, voice_method=values.unset,
               voice_fallback_url=values.unset, voice_fallback_method=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               voice_caller_id_lookup=values.unset, sms_url=values.unset,
               sms_method=values.unset, sms_fallback_url=values.unset,
               sms_fallback_method=values.unset, sms_status_callback=values.unset,
               message_status_callback=values.unset):
        """
        Update the ApplicationInstance

        :param unicode friendly_name: Human readable description of this resource
        :param unicode api_version: The API version to use
        :param unicode voice_url: URL Twilio will make requests to when relieving a call
        :param unicode voice_method: HTTP method to use with the URL
        :param unicode voice_fallback_url: Fallback URL
        :param unicode voice_fallback_method: HTTP method to use with the fallback url
        :param unicode status_callback: URL to hit with status updates
        :param unicode status_callback_method: HTTP method to use with the status callback
        :param bool voice_caller_id_lookup: True or False
        :param unicode sms_url: URL Twilio will request when receiving an SMS
        :param unicode sms_method: HTTP method to use with sms_url
        :param unicode sms_fallback_url: Fallback URL if there's an error parsing TwiML
        :param unicode sms_fallback_method: HTTP method to use with sms_fallback_method
        :param unicode sms_status_callback: URL Twilio with request with status updates
        :param unicode message_status_callback: URL to make requests to with status updates

        :returns: Updated ApplicationInstance
        :rtype: twilio.rest.api.twilio.com.2010-04-01.application.ApplicationList
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'ApiVersion': api_version,
            'VoiceUrl': voice_url,
            'VoiceMethod': voice_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceFallbackMethod': voice_fallback_method,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'VoiceCallerIdLookup': voice_caller_id_lookup,
            'SmsUrl': sms_url,
            'SmsMethod': sms_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsStatusCallback': sms_status_callback,
            'MessageStatusCallback': message_status_callback,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return ApplicationInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.ApplicationContext {}>'.format(context)


class ApplicationInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the ApplicationInstance

        :returns: twilio.rest.api.v2010.application.ApplicationInstance
        :rtype: twilio.rest.api.v2010.application.ApplicationInstance
        """
        super(ApplicationInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'api_version': payload['api_version'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'message_status_callback': payload['message_status_callback'],
            'sid': payload['sid'],
            'sms_fallback_method': payload['sms_fallback_method'],
            'sms_fallback_url': payload['sms_fallback_url'],
            'sms_method': payload['sms_method'],
            'sms_status_callback': payload['sms_status_callback'],
            'sms_url': payload['sms_url'],
            'status_callback': payload['status_callback'],
            'status_callback_method': payload['status_callback_method'],
            'uri': payload['uri'],
            'voice_caller_id_lookup': payload['voice_caller_id_lookup'],
            'voice_fallback_method': payload['voice_fallback_method'],
            'voice_fallback_url': payload['voice_fallback_url'],
            'voice_method': payload['voice_method'],
            'voice_url': payload['voice_url'],
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ApplicationContext for this ApplicationInstance
        :rtype: twilio.rest.api.v2010.application.ApplicationContext
        """
        if self._context is None:
            self._context = ApplicationContext(
                self._version,
                account_sid=self._solution['account_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: A string that uniquely identifies this resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def api_version(self):
        """
        :returns: The API version to use
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def date_created(self):
        """
        :returns: Date this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: Date this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: Human readable description of this resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def message_status_callback(self):
        """
        :returns: URL to make requests to with status updates
        :rtype: unicode
        """
        return self._properties['message_status_callback']

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def sms_fallback_method(self):
        """
        :returns: HTTP method to use with sms_fallback_method
        :rtype: unicode
        """
        return self._properties['sms_fallback_method']

    @property
    def sms_fallback_url(self):
        """
        :returns: Fallback URL if there's an error parsing TwiML
        :rtype: unicode
        """
        return self._properties['sms_fallback_url']

    @property
    def sms_method(self):
        """
        :returns: HTTP method to use with sms_url
        :rtype: unicode
        """
        return self._properties['sms_method']

    @property
    def sms_status_callback(self):
        """
        :returns: URL Twilio with request with status updates
        :rtype: unicode
        """
        return self._properties['sms_status_callback']

    @property
    def sms_url(self):
        """
        :returns: URL Twilio will request when receiving an SMS
        :rtype: unicode
        """
        return self._properties['sms_url']

    @property
    def status_callback(self):
        """
        :returns: URL to hit with status updates
        :rtype: unicode
        """
        return self._properties['status_callback']

    @property
    def status_callback_method(self):
        """
        :returns: HTTP method to use with the status callback
        :rtype: unicode
        """
        return self._properties['status_callback_method']

    @property
    def uri(self):
        """
        :returns: URI for this resource
        :rtype: unicode
        """
        return self._properties['uri']

    @property
    def voice_caller_id_lookup(self):
        """
        :returns: True or False
        :rtype: bool
        """
        return self._properties['voice_caller_id_lookup']

    @property
    def voice_fallback_method(self):
        """
        :returns: HTTP method to use with the fallback url
        :rtype: unicode
        """
        return self._properties['voice_fallback_method']

    @property
    def voice_fallback_url(self):
        """
        :returns: Fallback URL
        :rtype: unicode
        """
        return self._properties['voice_fallback_url']

    @property
    def voice_method(self):
        """
        :returns: HTTP method to use with the URL
        :rtype: unicode
        """
        return self._properties['voice_method']

    @property
    def voice_url(self):
        """
        :returns: URL Twilio will make requests to when relieving a call
        :rtype: unicode
        """
        return self._properties['voice_url']

    def delete(self):
        """
        Deletes the ApplicationInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch a ApplicationInstance

        :returns: Fetched ApplicationInstance
        :rtype: twilio.rest.api.twilio.com.2010-04-01.application.ApplicationList
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset, api_version=values.unset,
               voice_url=values.unset, voice_method=values.unset,
               voice_fallback_url=values.unset, voice_fallback_method=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               voice_caller_id_lookup=values.unset, sms_url=values.unset,
               sms_method=values.unset, sms_fallback_url=values.unset,
               sms_fallback_method=values.unset, sms_status_callback=values.unset,
               message_status_callback=values.unset):
        """
        Update the ApplicationInstance

        :param unicode friendly_name: Human readable description of this resource
        :param unicode api_version: The API version to use
        :param unicode voice_url: URL Twilio will make requests to when relieving a call
        :param unicode voice_method: HTTP method to use with the URL
        :param unicode voice_fallback_url: Fallback URL
        :param unicode voice_fallback_method: HTTP method to use with the fallback url
        :param unicode status_callback: URL to hit with status updates
        :param unicode status_callback_method: HTTP method to use with the status callback
        :param bool voice_caller_id_lookup: True or False
        :param unicode sms_url: URL Twilio will request when receiving an SMS
        :param unicode sms_method: HTTP method to use with sms_url
        :param unicode sms_fallback_url: Fallback URL if there's an error parsing TwiML
        :param unicode sms_fallback_method: HTTP method to use with sms_fallback_method
        :param unicode sms_status_callback: URL Twilio with request with status updates
        :param unicode message_status_callback: URL to make requests to with status updates

        :returns: Updated ApplicationInstance
        :rtype: twilio.rest.api.twilio.com.2010-04-01.application.ApplicationList
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            api_version=api_version,
            voice_url=voice_url,
            voice_method=voice_method,
            voice_fallback_url=voice_fallback_url,
            voice_fallback_method=voice_fallback_method,
            status_callback=status_callback,
            status_callback_method=status_callback_method,
            voice_caller_id_lookup=voice_caller_id_lookup,
            sms_url=sms_url,
            sms_method=sms_method,
            sms_fallback_url=sms_fallback_url,
            sms_fallback_method=sms_fallback_method,
            sms_status_callback=sms_status_callback,
            message_status_callback=message_status_callback,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.ApplicationInstance {}>'.format(context)
