#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyflapjack.jsonapi.base import Resource, RelationMixin


class Contact(Resource):
    path = 'contacts'

    def __init__(self, id, first_name, last_name, email, timezone, **kwargs):
        super(Contact, self).__init__(
            id=id, first_name=first_name, last_name=last_name, email=email,
            timezone=timezone, **kwargs)


class ContactRelatedResource(Resource, RelationMixin):
    def __init__(self, **kwargs):
        RelationMixin.__init__(
            self, Contact.path, kwargs.pop('contact_id', None))
        super(ContactRelatedResource, self).__init__(**kwargs)


class Media(ContactRelatedResource):
    path = 'media'

    def __init__(
            self, type_, address, interval, rollup_threshold, **kwargs):
        super(Media, self).__init__(
            type=type_, address=address, interval=interval,
            rollup_threshold=rollup_threshold, **kwargs
        )


class PagerdutyCredentials(ContactRelatedResource):
    path = 'pagerduty_credentials'

    def __init__(self, service_key, subdomain, username, password, **kwargs):
        super(PagerdutyCredentials, self).__init__(
            service_key=service_key, subdomain=subdomain,
            username=username, password=password, **kwargs
        )


class NotificationRule(ContactRelatedResource):
    def __init__(
            self, contact_id, entities=None, regex_entities=None, tags=None,
            regex_tags=None, time_restrictions=None, unknown_media=None,
            warning_media=None, critical_media=None, unknown_blackhole=None,
            warning_blackhole=None, critical_blackhole=None, **kwargs):
        named = dict(
            entities=None, regex_entities=None, tags=None,
            regex_tags=None, time_restrictions=None, unknown_media=None,
            warning_media=None, critical_media=None, unknown_blackhole=None,
            warning_blackhole=None, critical_blackhole=None,
            contact_id=contact_id
        )
        for k, v in named.iteritems():
            if v is None:
                named[k] = []
        kwargs.update(named)
        super(NotificationRule, self).__init__(**kwargs)


class Entity(Resource):
    path = 'entities'

    def __init__(self, name, **kwargs):
        super(Entity, self).__init__(name=name, **kwargs)


class Check(Resource):
    path = 'checks'

    def __init__(self, name, **kwargs):
        super(Check, self).__init__(name=name, **kwargs)


class ScheduledMaintenance(Resource):
    def __init__(self, start_time, duration, summary):
        super(ScheduledMaintenance, self).__init__(
            start_time=start_time,
            duration=duration,
            summary=summary,
        )


class UnscheduledMaintenance(Resource):
    def __init__(self, duration, summary):
        super(UnscheduledMaintenance, self).__init__(
            duration=duration, summary=summary)


class EntityScheduledMaintenance(ScheduledMaintenance):
    path = 'scheduled_maintenances/entities'


class EntityUnscheduledMaintenance(UnscheduledMaintenance):
    path = 'unscheduled_maintenances'


class CheckScheduledMaintenance(ScheduledMaintenance):
    path = 'scheduled_maintenances/checks'


class CheckUnScheduledMaintenance(UnscheduledMaintenance):
    path = 'unscheduled_maintenances/checks'


class TestNotification(Resource):
    path = 'test_notifications'

    def __init__(self, summary):
        super(TestNotification, self).__init__(summary=summary)

