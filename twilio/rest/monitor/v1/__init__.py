# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.monitor.v1.alert import AlertList
from twilio.rest.monitor.v1.event import EventList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Monitor

        :returns: V1 version of Monitor
        :rtype: V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._alerts = None
        self._events = None

    @property
    def alerts(self):
        """
        :rtype: twilio.rest.monitor.v1.alert.AlertList
        """
        if self._alerts is None:
            self._alerts = AlertList(self)
        return self._alerts

    @property
    def events(self):
        """
        :rtype: twilio.rest.monitor.v1.event.EventList
        """
        if self._events is None:
            self._events = EventList(self)
        return self._events

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Monitor.V1>'
