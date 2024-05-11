from django.urls import path

from apis.views import *

urlpatterns = [
    path('init', init),

    path('create_space', create_space),
    path('get_space', get_space),
    path('update_space', update_space),
    path('end_active_conference', end_active_conference),

    path('list_conference_records', list_conference_records),
    path('get_conference_record', get_conference_record),

    path('list_participants', list_participants),
    path('get_participant', get_participant),
    path('list_participant_sessions', list_participant_sessions),
    path('get_participant_session', get_participant_session),
]
