from django.shortcuts import render

from stories.models import Story


def homepage(request):
    stories = Story.objects.all().order_by("-upvotes")
    return render(request, "core/homepage.html", {"stories": stories})
