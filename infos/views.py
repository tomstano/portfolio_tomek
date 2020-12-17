from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def me_page(request):
    me_tmpl = loader.get_template('infos/me.html')
    me_cnt = {
        'title': 'Here should be a "me" content!',
        }
    return HttpResponse(me_tmpl.render(me_cnt))


def contact_page(request):
    contact_tmpl = loader.get_template('infos/contact.html')
    contact_cnt = {
        'title': 'Here should be a "contact" content!',
    }
    return HttpResponse(contact_tmpl.render(contact_cnt))
