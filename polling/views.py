from django.shortcuts import render

from django.http import Http404
from polling.models import Poll

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PollListView(ListView):
    model = Poll
    template_name = "polling/list.html"


class PollDetailView(DetailView):
    model = Poll
    template_name = "polling/detail.html"

    def get(self, request, *args, **kwargs):
        poll = self.get_object()
        context = {"polli": poll, "object": poll}
        return render(request, "polling/detail.html", context)

    def post(self, request, *args, **kwargs):
        poll = self.get_object()

        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

        context = {"polli": poll, "object": poll}
        return render(request, "polling/detail.html", context)


def detail_view(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

    context = {"poll": poll}
    return render(request, "polling/detail.html", context)
