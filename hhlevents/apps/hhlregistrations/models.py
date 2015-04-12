from django.db import models
import datetime
from happenings.models import Event as HappeningsEvent

class Event(HappeningsEvent):
    extra_url = models.URLField(blank=True)
    gforms_url = models.URLField(blank=True)
    require_registration = models.BooleanField(default=False)
    max_registrations = models.PositiveSmallIntegerField(default=0)
    close_registrations = models.DateTimeField(blank=True, null=True)
    payment_due = models.DateTimeField(blank=True, null=True)
    event_cost = models.PositiveSmallIntegerField(default=0)
    materials_cost = models.PositiveSmallIntegerField(default=0)
    materials_mandatory = models.BooleanField(default=False)


class Person(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    banned = models.DateTimeField(blank=True, null=True, verbose_name=u'Automatically put to waiting list')

    def __unicode__(self):
        return u'%s, %s <%s>' % (self.last_name, self.first_name, self.email)


class Registration(models.Model):
    STATES = (
        ( 'AC', 'Assumed coming'),
        ( 'CC', 'Confirmed coming'),
        ( 'WL', 'Waiting-list'),
        ( 'CA', 'Cancelled'),
        ( 'WB', 'Waiting-list (due to ban)'),
    )

    paid = models.DateTimeField(blank=True, null=True)
    event = models.ForeignKey(Event, related_name='persons', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, related_name='events', on_delete=models.CASCADE)
    registered = models.DateTimeField(default=datetime.datetime.now)
    cancelled = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=2, choices=STATES)
    wants_materials = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s, %s <%s> (%s)' % (self.person.last_name, self.person.first_name, self.person.email, self.state)
