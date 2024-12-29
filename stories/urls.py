from django.urls import path

from stories.views import StoryDetailView, StoryListView

app_name = "stories"

urlpatterns = [
    path("", StoryListView.as_view(), name="list"),
    path("stories/<int:pk>/", StoryDetailView.as_view(), name="detail"),
]
