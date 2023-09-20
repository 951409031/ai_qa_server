from django.urls import path
from . import views

urlpatterns = [
    # 问题补全
    path('complete_question', views.complete_question, name='course.complete_question'),
    # 问题课程匹配度评估
    path('assess_subject', views.assess_subject, name='course.assess_subject'),
    # 根据文档回答问题
    path('answer_doc', views.answer_doc, name='course.answer_doc'),
    # 脱离文档回答问题
    path('answer_free', views.answer_free, name='course.answer_free'),
]
