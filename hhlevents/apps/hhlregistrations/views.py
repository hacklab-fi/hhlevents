# -*- coding: UTF-8 -*-
import datetime
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import RegForm
from .models import Event, Person, Registration


class RegView(FormView):
    form_class = RegForm
    template_name = 'hhlregistrations/register.html'
    success_url = reverse_lazy('registrations:regok_generic')

    def get_context_data(self, **kwargs):
        context = super(RegView, self).get_context_data(**kwargs)
        context['event'] = get_object_or_404(Event, pk=self.kwargs['event_id'])
        context['show_form'] = True

        context['registration_closed'] = False
        if (    context['event'].close_registrations
            and datetime.datetime.now() > context['event'].close_registrations):
            context['registration_closed'] = True
            context['show_form'] = False

        context['waiting_list'] = False
        if (    context['event'].max_registrations > 0
            and Registration.objects.filter(state__in=('AC', 'CC')).count() >= context['event'].max_registrations):
            context['waiting_list'] = True

        context['show_optional'] = True
        context['show_join'] = True
        if context['event'].hide_join_checkbox:
            context['show_join'] = False

        context['show_materials'] = False
        if (    context['event'].materials_cost
            and not context['event'].materials_mandatory):
            context['show_materials'] = True

        # Hide the whole optional section if we have nothing to show there
        if True not in (context['show_join'], context['show_materials']):
            context['show_optional'] = False

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        data = form.cleaned_data
        
        person, created = Person.objects.get_or_create(email=data['email'],
            defaults={
                'first_name': data['first_name'], 
                'last_name': data['last_name'], 
            }
        )

        # Just in case someone manages to sneak a double reg through the form
        registration, created = Registration.objects.get_or_create(person=person, event=context['event'],
            defaults={
                'state': 'AC', 
                'wants_materials': data['wants_materials'],
            }
        )
        
        if data['join']:
            mail = EmailMessage()
            mail.from_email = person.formatted_email
            # TODO: read this from settings
            mail.to = ['hallitus@helsinki.hacklab.fi', person.formatted_email]
            mail.subject = u'Jäsenhakemus (ilmoittautumislomakkeelta)'
            mail.body = """
Nimi: {lname}, {fname}
Paikkakunta: {city}

Haen jäseneksi, hyväksyn Helsinki Hacklab ry:n säännöt.
            """.format(fname=person.first_name, lname=person.last_name, city=data['city']).strip()
            
            # TODO: Do not ignore, catch the error and tell the user to send the mail themself
            mail.send(True)

        return super(RegView, self).form_valid(form)

class RegOKView(TemplateView):
    template_name = 'hhlregistrations/register_ok.html'

