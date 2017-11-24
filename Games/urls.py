from django.conf.urls import url, include
# from .views import (character, registration, register_in_site_post, 
# 				   login_site, login_in_site, logout_in_site, register_character_post,
# 				   registration_character)
from .views import index, send_message, registration, register_in_site_post, gomoku, lines, login_in_site, resume, login_site, logout_in_site, plus_gomoku_game, allgames, bowling, processing_bowling_throw, show_gomoku_game

urlpatterns = [

    # url(r'^register/$', registration, name="registration"),
    url(r'^register/post$', register_in_site_post, name = "post_registration"),
    # url(r'^character/(?P<id>[\w-]+)/$', character, name="character"),
    # url(r'^login/$', login_site, name="login"),
    url(r'^logout/$', logout_in_site, name="logout"),
    url(r'^login/post$', login_in_site, name="login_post"),
    #  url(r'^registercharacter/$', registration_character, name="registration_character"),
    # url(r'^registercharacter/post$', register_character_post, name = "register_character_post"),
    url(r'^$', index, name = 'index'),
    url(r'^Games/$', allgames, name = 'allgames'),
    url(r'^Resume/$', resume, name = 'resume'),
    url(r'^Games/gomoku/$', gomoku, name = 'gomoku'),
    url(r'^Games/bowling/$', bowling, name = 'bowling'),
    url(r'^Games/lines/$', lines, name = 'lines'),
    url(r'^Resume/send_message$', send_message, name = 'send_message'),
    url(r'^Games/gomoku/plus_gomoku_game/$', plus_gomoku_game, name = 'plus_gomoku_game'),
    url(r'^Games/gomoku/show_gomoku_game/$', show_gomoku_game, name = 'show_gomoku_game'),
    url(r'^Games/bowling/processing_bowling_throw/$', processing_bowling_throw, name = 'processing_bowling_throw'),
    
]