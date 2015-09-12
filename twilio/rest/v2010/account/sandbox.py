# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.util import (
    parse_date,
    parse_iso_date,
)
from twilio.rest.resources.base import InstanceResource
from twilio.rest.resources.base import ListResource
from twilio.rest.resources.base import GetQuery
from twilio.rest.resources.base import UpdateQuery


class Sandbox(InstanceResource):
    """
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: pin
    
        The pin
    
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: phone_number
    
        The phone_number
    
    .. attribute:: application_sid
    
        The application_sid
    
    .. attribute:: api_version
    
        The api_version
    
    .. attribute:: voice_url
    
        The voice_url
    
    .. attribute:: voice_method
    
        The voice_method
    
    .. attribute:: sms_url
    
        The sms_url
    
    .. attribute:: sms_method
    
        The sms_method
    
    .. attribute:: status_callback
    
        The status_callback
    
    .. attribute:: status_callback_method
    
        The status_callback_method
    
    .. attribute:: uri
    
        The uri
    """
    id_key = "sid"

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super(Sandbox, self).__init__(parent, None)

    def load(self, *args, **kwargs):
        super(Sandbox, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update the instance
        
        :param str sms_method: The sms_method
        :param str sms_url: The sms_url
        :param str status_callback: The status_callback
        :param str status_callback_method: The status_callback_method
        :param str voice_method: The voice_method
        :param str voice_url: The voice_url
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Sandbox`
        """
        return self.update_instance(kwargs)


class Sandboxes(ListResource):
    name = "Sandbox"
    mount_name = "sandbox"
    key = "sandbox"
    instance = Sandbox

    def __init__(self, *args, **kwargs):
        super(Sandboxes, self).__init__(*args, **kwargs)

    def get(self, **kwargs):
        """ Get the Sandbox """
        return GetQuery(self, self.uri, self.use_json_extension,
                        params=kwargs)

    def update(self, **kwargs):
        """
        Update the :class:`Sandbox`
        
        :param str sms_method: The sms_method
        :param str sms_url: The sms_url
        :param str status_callback: The status_callback
        :param str status_callback_method: The status_callback_method
        :param str voice_method: The voice_method
        :param str voice_url: The voice_url
        
        :raises TwilioRestException: when the request fails on execute
        """
        return UpdateQuery(self, self.uri, kwargs,
            self.use_json_extension)

    def load_instance(self, data):
        """ Override because Sandbox does not have a sid """
        instance = self.instance(self)
        instance.load(data)
        instance.load_subresources()
        return instance