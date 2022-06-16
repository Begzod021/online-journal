from django.urls import path
from .views import *

urlpatterns = [
    path('rating-post/', JournalPostRetings.as_view(), name='rating-post'),
    path('journal-list/', JournalList.as_view(), name='journal-list'),
    path('journal/', JournalForPupilDetailView.as_view(), name="journal"),
    path('journal/<int:pk>/', JournalForTeacherAdminDetailView.as_view(), name="get_journal")
]
