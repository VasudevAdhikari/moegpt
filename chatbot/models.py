from django.db import models
from django.contrib.auth.models import User

class Module(models.Model):
    module_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module_time = models.DateTimeField(null=False, auto_now=True)
    module_title = models.TextField(null=False)
    is_current = models.BooleanField(default=False)

    class Meta:
        db_table = 'chatbot_module'

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    question = models.TextField(null=False)
    answer = models.TextField()

    class Meta:
        db_table = 'chatbot_chat'