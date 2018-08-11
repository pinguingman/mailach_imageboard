from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Section, Thread, Message
from .forms import ThreadForm, MessageForm


class IndexView(generic.ListView):
    """ Show main page. """
    template_name = 'threads/index.html'
    context_object_name = 'sections'

    def get_queryset(self):
        """ Return all sections. """
        return Section.objects.all()


def section_view(request, section_name):
    section = get_object_or_404(Section, name=section_name)
    threads = Thread.objects.filter(sections__name=section_name).order_by('-last_message_pub_date')
    if request.method == 'POST':
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            new_thread = Thread(
                    title=form.cleaned_data['title'],
                    text=form.cleaned_data['text'],
                    pub_date=timezone.now(),
                    sections=section,
                    )
            if 'image' in request.FILES:
                new_thread.image = request.FILES['image']
            if 'video' in request.FILES:
                new_thread.video = request.FILES['video']
            new_thread.save()
            return HttpResponseRedirect(reverse(
                'threads:thread_url',
                kwargs={'section_name': section_name, 'thread_id': new_thread.id_threads_messages}
                ))
        else:
            return render(request, 'threads/section.html', {
                'section_name':     section.name,
                'threads':          threads,
                'form':             form
            })
    form = ThreadForm()
    return render(request, 'threads/section.html', {
        'section_name':     section.name,
        'threads':          threads,
        'form':             form
    })


def thread_view(request, section_name, thread_id):
    section = get_object_or_404(Section, name=section_name)
    threads = Thread.objects.filter(sections__name=section_name)
    thread = threads.get(id_threads_messages=thread_id)
    messages = thread.message_set.all()
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            num_in_thread = len(list(thread.message_set.all()))
            new_message = Message(
                    text=form.cleaned_data['text'],
                    pub_date=timezone.now(),
                    threads=thread
                    )
            if 'image' in request.FILES:
                new_message.image = request.FILES['image']
            if 'video' in request.FILES:
                new_message.video = request.FILES['video']
            new_message.save()
            return HttpResponseRedirect(reverse(
                'threads:thread_url',
                kwargs={'section_name': section_name, 'thread_id': thread_id}
                ))
        else:
            return render(request, 'threads/thread.html', {
                'section_name':     section.name,
                'thread_id':        thread.id_threads_messages,
                'thread':           thread,
                'messages':         messages,
                'form':             form
            })    
    form = MessageForm()
    return render(request, 'threads/thread.html', {
        'section_name':     section.name,
        'thread_id':        thread.id_threads_messages,
        'thread':           thread,
        'messages':         messages,
        'form':             form
    })
