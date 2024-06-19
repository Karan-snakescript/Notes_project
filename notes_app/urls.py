from django.urls import path
from .views import signup_view, login_view, logout_view, home_view, add_note_view, edit_note_view, delete_note_view, note_detail_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),
    path('note/add/', add_note_view, name='add_note'),
    path('note/<int:note_id>/edit/', edit_note_view, name='edit_note'),
    path('note/<int:note_id>/delete/', delete_note_view, name='delete_note'),
    path('note/<int:note_id>/', note_detail_view, name='note_detail'),
]
