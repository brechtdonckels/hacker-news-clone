from django.views.generic import DetailView, ListView

from stories.models import Story


class StoryListView(ListView):
    model = Story
    ordering = ["-upvotes"]


class StoryDetailView(DetailView):
    model = Story
