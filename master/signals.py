from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('#----------Signal Login Testing Started--------------')
    print('Sender : ',sender)
    print('Request : ',request)
    print('User : ',user)
    print('User Password : ',user.password)
    print(f'Kwargs : {kwargs}')
    print('#----------Signal Login Testing Ended--------------')

@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    print('#----------Signal Logout Testing Started--------------')
    print('Sender : ',sender)
    print('Request : ',request)
    print('User : ',user)
    print('User Password : ',user.password)
    print(f'Kwargs : {kwargs}')
    print('#----------Signal Logout Testing Ended--------------')

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print('#----------Signal Login Failed Testing Started------')
    print('Sender : ',sender)
    print('Credentials : ',credentials)
    print('Request : ',request)
    print(f'Kwargs : {kwargs}')
    print('#----------Signal Login Failed Testing Ended---------')

# user_logged_in.connect(login_success, sender=User)
# user_logged_out.connect(logout_success, sender=User)
# user_login_failed.connect(login_failed)

@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print('#----------Pre Save Signal Testing Started------')
    print('Sender : ',sender)
    print('Instance : ',instance)
    print(f'Kwargs : {kwargs}')
    print('#----------Pre Save Signal Testing Ended---------')
    
@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print('#----------Post Save Signal Testing Started------')
        print('Record : New Record')
        print('Sender : ',sender)
        print('Instance : ',instance)
        print(f'Kwargs : {kwargs}')
        print('#----------Post Save Signal Testing Ended---------')
    else:
        print('#----------Post Save Signal Testing Started------')
        print('Record : Update Record')
        print('Sender : ',sender)
        print('Instance : ',instance)
        print(f'Kwargs : {kwargs}')
        print('#----------Post Save Signal Testing Ended---------') 
    
@receiver(pre_delete, sender=User)
def at_ending_save(sender, instance, **kwargs):
    print('#----------Pre Delete Signal Testing Started------')
    print('Sender : ',sender)
    print('Instance : ',instance)
    print(f'Kwargs : {kwargs}')
    print('#----------Pre Delete Signal Testing Ended---------')
    
@receiver(post_delete, sender=User)
def at_ending_save(sender, instance, **kwargs):
    print('#----------Post Delete Signal Testing Started------')
    print('Sender : ',sender)
    print('Instance : ',instance)
    print(f'Kwargs : {kwargs}')
    print('#----------Post Delete Signal Testing Ended---------')
    
@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print('#----------pre init Signal Testing Started------')
    print('Sender : ',sender)
    print(f'Args : {args}')
    print(f'Kwargs : {kwargs}')
    print('#----------pre init Signal Testing Ended---------')
    
@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print('#----------Post init Signal Testing Started------')
    print('Sender : ',sender)
    print(f'Args : {args}')
    print(f'Kwargs : {kwargs}')
    print('#----------Post init Signal Testing Ended---------')

@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print('#----------At Beginning Request Signal Testing Started------')
    print('Sender : ',sender)
    print('Environ : ',environ)
    print(f'Kwargs : {kwargs}')
    print('#----------At Beginning Request Signal Testing Ended---------')

@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
    print('#----------At Request Exception Signal Testing Started------')
    print('Sender : ',sender)
    print('Request : ',request)
    print(f'Kwargs : {kwargs}')
    print('#----------At Request Exception Signal Testing Ended---------')
      
@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('#----------Before Install App Signal Testing Started------')
    print('Sender : ',sender)
    print('App Config : ',app_config)
    print('Verbosity : ',verbosity)
    print('Interactive : ',interactive)
    print('Using : ',using)
    print('Plan : ',plan)
    print('Apps : ',apps)
    print(f'Kwargs : {kwargs}')
    print('#----------Before Install App Signal Testing Ended---------')
      
@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('#----------At End Migrate Flush Signal Testing Started------')
    print('Sender : ',sender)
    print('App Config : ',app_config)
    print('Verbosity : ',verbosity)
    print('Interactive : ',interactive)
    print('Using : ',using)
    print('Plan : ',plan)
    print('Apps : ',apps)
    print(f'Kwargs : {kwargs}')
    print('#----------At End Migrate Flush Signal Testing Ended---------')
      
@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print('#----------Intial Connection To The Database Testing Started------')
    print('Sender : ',sender)
    print('Connection : ',connection)
    print(f'Kwargs : {kwargs}')
    print('#----------Intial Connection To The Database Testing Ended---------')
    






