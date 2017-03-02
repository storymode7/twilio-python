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
from twilio.rest.api.v2010.account.queue.member import MemberList


class QueueList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the QueueList

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid

        :returns: twilio.rest.api.v2010.queue.QueueList
        :rtype: twilio.rest.api.v2010.queue.QueueList
        """
        super(QueueList, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/Queues.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams QueueInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

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
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists QueueInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of QueueInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of QueueInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return QueuePage(self._version, response, self._solution)

    def create(self, friendly_name, max_size=values.unset):
        """
        Create a new QueueInstance

        :param unicode friendly_name: A user-provided string that identifies this queue.
        :param unicode max_size: The max number of calls allowed in the queue

        :returns: Newly created QueueInstance
        :rtype: twilio.rest.api.twilio.com.2010-04-01.queue.QueueList
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'MaxSize': max_size,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return QueueInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def get(self, sid):
        """
        Constructs a QueueContext

        :param sid: Fetch by unique queue Sid

        :returns: twilio.rest.api.v2010.queue.QueueContext
        :rtype: twilio.rest.api.v2010.queue.QueueContext
        """
        return QueueContext(
            self._version,
            account_sid=self._solution['account_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a QueueContext

        :param sid: Fetch by unique queue Sid

        :returns: twilio.rest.api.v2010.queue.QueueContext
        :rtype: twilio.rest.api.v2010.queue.QueueContext
        """
        return QueueContext(
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
        return '<Twilio.Api.V2010.QueueList>'


class QueuePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the QueuePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The account_sid

        :returns: twilio.rest.api.v2010.queue.QueuePage
        :rtype: twilio.rest.api.v2010.queue.QueuePage
        """
        super(QueuePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of QueueInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.queue.QueueInstance
        :rtype: twilio.rest.api.v2010.queue.QueueInstance
        """
        return QueueInstance(
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
        return '<Twilio.Api.V2010.QueuePage>'


class QueueContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        """
        Initialize the QueueContext

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param sid: Fetch by unique queue Sid

        :returns: twilio.rest.api.v2010.queue.QueueContext
        :rtype: twilio.rest.api.v2010.queue.QueueContext
        """
        super(QueueContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Queues/{sid}.json'.format(**self._solution)

        # Dependents
        self._members = None

    def fetch(self):
        """
        Fetch a QueueInstance

        :returns: Fetched QueueInstance
        :rtype: twilio.rest.api.twilio.com.2010-04-01.queue.QueueList
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return QueueInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def update(self, friendly_name=values.unset, max_size=values.unset):
        """
        Update the QueueInstance

        :param unicode friendly_name: A human readable description of the queue
        :param unicode max_size: The max number of members allowed in the queue

        :returns: Updated QueueInstance
        :rtype: twilio.rest.api.twilio.com.2010-04-01.queue.QueueList
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'MaxSize': max_size,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return QueueInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the QueueInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def members(self):
        """
        Access the members

        :returns: twilio.rest.api.v2010.member.MemberList
        :rtype: twilio.rest.api.v2010.member.MemberList
        """
        if self._members is None:
            self._members = MemberList(
                self._version,
                account_sid=self._solution['account_sid'],
                queue_sid=self._solution['sid'],
            )
        return self._members

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.QueueContext {}>'.format(context)


class QueueInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the QueueInstance

        :returns: twilio.rest.api.v2010.queue.QueueInstance
        :rtype: twilio.rest.api.v2010.queue.QueueInstance
        """
        super(QueueInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'average_wait_time': deserialize.integer(payload['average_wait_time']),
            'current_size': deserialize.integer(payload['current_size']),
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'max_size': deserialize.integer(payload['max_size']),
            'sid': payload['sid'],
            'uri': payload['uri'],
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

        :returns: QueueContext for this QueueInstance
        :rtype: twilio.rest.api.v2010.queue.QueueContext
        """
        if self._context is None:
            self._context = QueueContext(
                self._version,
                account_sid=self._solution['account_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def average_wait_time(self):
        """
        :returns: Average wait time of members in the queue
        :rtype: unicode
        """
        return self._properties['average_wait_time']

    @property
    def current_size(self):
        """
        :returns: The count of calls currently in the queue.
        :rtype: unicode
        """
        return self._properties['current_size']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: A user-provided string that identifies this queue.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def max_size(self):
        """
        :returns: The max number of calls allowed in the queue
        :rtype: unicode
        """
        return self._properties['max_size']

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this queue
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: unicode
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch a QueueInstance

        :returns: Fetched QueueInstance
        :rtype: twilio.rest.api.twilio.com.2010-04-01.queue.QueueList
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset, max_size=values.unset):
        """
        Update the QueueInstance

        :param unicode friendly_name: A human readable description of the queue
        :param unicode max_size: The max number of members allowed in the queue

        :returns: Updated QueueInstance
        :rtype: twilio.rest.api.twilio.com.2010-04-01.queue.QueueList
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            max_size=max_size,
        )

    def delete(self):
        """
        Deletes the QueueInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def members(self):
        """
        Access the members

        :returns: twilio.rest.api.v2010.member.MemberList
        :rtype: twilio.rest.api.v2010.member.MemberList
        """
        return self._proxy.members

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.QueueInstance {}>'.format(context)
