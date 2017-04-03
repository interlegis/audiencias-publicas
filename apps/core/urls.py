from django.conf.urls import url
from apps.core.views import (VideoDetail, RoomQuestionList, ClosedVideos,
                             VideoReunionDetail, QuestionDetail, index)
from apps.core.api import (api_root, MessageListAPI, QuestionListAPI,
                           VoteListAPI, UserListAPI, RoomAPI, RoomListAPI)


urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^pergunta/(?P<pk>\d+)/?$', QuestionDetail.as_view(),
        name='question_detail'),
    url(r'^sala/(?P<pk>\d+)/?$', VideoDetail.as_view(), name='video_room'),
    url(r'^sala/reuniao/(?P<cod_reunion>\d+)/?$', VideoReunionDetail.as_view(),
        name='video_reunion_room'),
    url(r'^sala/(?P<pk>\d+)/perguntas/?$', RoomQuestionList.as_view(),
        name='questions_list'),
    url(r'^fechadas/?$', ClosedVideos.as_view(), name='video_list'),
]

urlpatterns += [
    url(r'^api/$', api_root),
    url(r'^api/messages/$', MessageListAPI.as_view(), name='message_list_api'),
    url(r'^api/question/$', QuestionListAPI.as_view(),
        name='question_list_api'),
    url(r'^api/room/$', RoomListAPI.as_view(), name='room_list_api'),
    url(r'^api/room/(?P<pk>\d+)$', RoomAPI.as_view(),
        name='room_detail_api'),
    url(r'^api/vote/$', VoteListAPI.as_view(), name='vote_list_api'),
    url(r'^api/user/$', UserListAPI.as_view(), name='user_list_api'),
]
