from urls.enlengthen import enlengthen
from django.http import HttpResponse, HttpResponseRedirect, Http404
from urls.models import UrlPair
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings


def index(request):

    if not 'url' in request.POST:
        return render_to_response('index.html', context_instance=RequestContext(request))

    url = request.POST['url']

    if url[0:4] != 'http':
        return render_to_response('index.html',
                {'error_message':'Post an url with a leading http'},
                context_instance=RequestContext(request))
    try:
        up = UrlPair.objects.get(url=url)

    except UrlPair.DoesNotExist:
        up = UrlPair(url=url, newUrl=enlengthen(url))
        up.save()

    if up:
        return HttpResponseRedirect(reverse('urls.views.posted', kwargs={'url':up.newUrl}))

def posted(request, url):
    u = get_object_or_404(UrlPair, newUrl = url)

    if u.url[0:4] != 'http':
        raise Http404

    pretty_url = settings.SITE_URL + 'r/' + u.newUrl
    main_page = reverse('urls.views.index')

    return render_to_response('posted.html', {'old':u.url, 'new':pretty_url, 'main_page':main_page})

def redirect(request, url):
    u = get_object_or_404(UrlPair, newUrl = url)

    if u.url[0:4] != 'http':
        raise Http404

    return HttpResponseRedirect(u.url)
