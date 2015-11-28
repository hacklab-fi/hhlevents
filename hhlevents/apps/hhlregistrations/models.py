import datetime
import uuid
from django.db import models
from django_markdown.models import MarkdownField
from django_markdown.fields import MarkdownFormField
from happenings.models import Event as HappeningsEvent
from django.utils import timezone
from django.core.urlresolvers import reverse

class Event(HappeningsEvent):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    extra_url = models.URLField(blank=True)
    gforms_url = models.URLField(blank=True)
    require_registration = models.BooleanField(default=False)
    max_registrations = models.PositiveSmallIntegerField(default=0)
    close_registrations = models.DateTimeField(blank=True, null=True)
    payment_due = models.DateTimeField(blank=True, null=True)
    event_cost = models.PositiveSmallIntegerField(default=0)
    materials_cost = models.PositiveSmallIntegerField(default=0)
    materials_mandatory = models.BooleanField(default=False)
    hide_join_checkbox = models.BooleanField(default=False)
    
    def formLink(self):
        tag = '<a href="' + reverse('registrations:register', args=[str(self.id)]) + '">Form</a>'
        if not self.require_registration:
            # in italics if registration is optional
            tag = '<i>(' + tag + ')</i>'
        return tag
    formLink.allow_tags = True
    formLink.short_description = 'Form link'
    
    def getParticipants(self):
        return Registration.objects.all().filter(event = self.event).order_by('state', 'registered')
    
    def getStatsHTML(self):
        n_AC = Registration.objects.all().filter(event = self.event).filter(state = 'AC').count()
        n_CC = Registration.objects.all().filter(event = self.event).filter(state = 'CC').count()
        n_WL = Registration.objects.all().filter(event = self.event).filter(state = 'WL').count()
        n_CA = Registration.objects.all().filter(event = self.event).filter(state = 'CA').count()
        n_WB = Registration.objects.all().filter(event = self.event).filter(state = 'WB').count()
        return u'Assumed coming (AC): %s<br/>Confirmed coming (CC): %s<br/>Waiting-list (WL): %s<br/>Cancelled (CA): %s<br/>Waiting-list (due to ban) (WB): %s' % (n_AC, n_CC, n_WL, n_CA, n_WB)
    
    class Meta:
        ordering = ["-end_date"]
    
    def isPast(self):
        if timezone.now() > self.end_date:
            return True
        return False
    def isCancelled(self):
        if self.check_if_cancelled(timezone.now()):
            return True
        return False
    def hasMoreOccurrences(self):
        if self.will_occur(timezone.now()) and not self.repeats('NEVER'):
            return True
        return False

class Person(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    banned = models.DateTimeField(blank=True, null=True, verbose_name=u'Automatically put to waiting list')

    def __unicode__(self):
        return self.formatted_email

    @property
    def formatted_email(self):
        return u'%s, %s <%s>' % (self.last_name, self.first_name, self.email)


class Registration(models.Model):
    STATES = (
        ( 'AC', 'Assumed coming'),
        ( 'CC', 'Confirmed coming'),
        ( 'WL', 'Waiting-list'),
        ( 'CA', 'Cancelled'),
        ( 'WB', 'Waiting-list (due to ban)'),
    )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    paid = models.DateTimeField(blank=True, null=True)
    event = models.ForeignKey(Event, related_name='persons', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, related_name='events', on_delete=models.CASCADE)
    registered = models.DateTimeField(default=datetime.datetime.now)
    cancelled = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=2, choices=STATES)
    wants_materials = models.BooleanField(default=False)

    class Meta:
        unique_together = (('event', 'person'),)

    def __unicode__(self):
        return u'%s, %s <%s> (%s)' % (self.person.last_name, self.person.first_name, self.person.email, self.state)
