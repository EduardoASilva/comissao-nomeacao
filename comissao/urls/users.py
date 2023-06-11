from django.urls import path

from comissao.views import users

urlpatterns = [
    path('login/', users.login, name='login'),
    path('login_user/', users.login_user, name='login_user'),
    path('logout/', users.logout, name='logout'),
    # path('find_users', users.find_users, name='find_users'),
    # path('add_user', users.add_user, name='add_user'),
    # path('usuario/view/<int:user_id>', users.view_user, name='view_user'),
    # path('usuario/editar/<int:user_id>', users.edit_user, name='edit_user'),
    # path('user/<str:token>/change_pass', users.change_pass, name='change_pass'),
    # path('user/change_pass', users.change_pass_done, name='change_pass_done'),
    # path('user/reset_password/<int:user_id>', users.reset_password, name='reset_password'),
    # path('user/del_user', users.del_user, name='del_user'),
]
