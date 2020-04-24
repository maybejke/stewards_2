from django.urls import path
from mainapp.views import IndexView, AboutView, ContactsView, DocumentsView, VacancyDetailView

app_name = 'mainapp'

urlpatterns = [
    path('', IndexView.as_view(), name="index_list"),
    path('blog_detail/', AboutView.as_view(), name="about"),
    path('contacts/', ContactsView.as_view(), name="contacts"),
    path('documents/', DocumentsView.as_view(), name="documents"),
    path('vacancy/<str:slug>/', VacancyDetailView.as_view(), name='vacancy_detail'),
]

