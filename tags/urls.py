from django.urls import path


from tags.views import (

    TagListView,
    TagDetailView,
    TagDeleteView,
    TagCreateView,
    TagUpdateView,

)

urlpatterns = [
    path("", TagListView.as_view(), name="tag_list"),
    path("<int:pk>/", TagDetailView.as_view(), name="tag_detail"),
    path("new/", TagCreateView.as_view(), name="tag_new"),
    path("<int:pk>/update", TagUpdateView.as_view(), name="tag_edit"),
    path("<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete")
]
