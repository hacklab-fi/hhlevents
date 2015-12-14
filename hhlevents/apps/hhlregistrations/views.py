# -*- coding: UTF-8 -*-
import datetime
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView, DetailView
from .forms import RegForm
from .models import Event, Person, Registration
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone


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
            and timezone.now() > context['event'].close_registrations): # timezone!
            context['registration_closed'] = True
            context['show_form'] = False

        context['waiting_list'] = False
        if (    context['event'].max_registrations > 0
            and Registration.objects.filter(state__in=('AC', 'CC')).count() >= context['event'].max_registrations):
            context['waiting_list'] = True

        context['show_optional'] = False
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



class ListDetailMixin(object):
   def get_context_data(self, **kwargs):
      return super(ListDetailMixin, self).get_context_data(**kwargs)

# could need AdminPlus for showing on the admin main page, for now, use URL /admin/reg_sum/
class Summary(ListDetailMixin, ListView, DetailView):
   context_object_name = 'reg_sum'
   template_name = 'hhlregistrations/summary.html'
   queryset = Event.objects.all()
   slug_field = 'event_slug'
   
   def get(self, request, *args, **kwargs):
       self.object = self.get_object()
       return super(Summary, self).get(self, request, *args, **kwargs)
   
   def post(self, request, *args, **kwargs):
       self.object = self.get_object()
       print(self.object)
       return self.send_email(request, *args, **kwargs)
   
   def get_object(self, queryset=None):
       try:
           sel_event = Event.objects.get(uuid=self.kwargs['slug'])
           print(self.kwargs['slug'])
       except:
           sel_event = None
       return sel_event
   
   def send_email(self, request, *args, **kwargs):
       subject = request.POST.get('subject', '')
       message = request.POST.get('message', '')
       from_email = request.POST.get('reply_to', '')
       extra_cc = [request.POST.get('extra_recipient', '')]
       bcc_to = []
       participants = self.object.getParticipants()
       for r in participants:
           bcc_to.append(r.person.email)
       msg = EmailMultiAlternatives(subject, message, from_email, [], bcc=bcc_to, cc=extra_cc)
       print(bcc_to)
       print(msg)
       if subject and message and from_email:
           try:
               msg.send()
           except BadHeaderError:
               return HttpResponse('Invalid header found.')
           messages.add_message(request, messages.INFO, 'Lähetetty viesti: "' + message + '   ---  Vastaanottajille: ' + ' '.join(bcc_to) +' '+ ' '.join(extra_cc))
           return super(Summary, self).get(self, request, *args, **kwargs)
       else:
           return HttpResponse('Make sure all fields are entered and valid.')

