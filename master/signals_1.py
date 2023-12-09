
from django.dispatch import Signal, receiver

# Creating Signals
notification = Signal()

# Reciever Function
@receiver(notification)
def show_notification(sender, **kwargs):
    print('#----------------Notification-----------------')
    print('Sender : ',sender)
    print('Kwargs : ',kwargs)


