from django.apps import AppConfig

class SignalsDemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signalsdemo'

    def ready(self):
        # Import signals here so they are active
        import signalsdemo.sync_signal
        import signalsdemo.same_thread
        import signalsdemo.same_transaction
