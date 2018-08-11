from django.db import models
from django.utils import timezone

import os


class Section(models.Model):
    """
    example .b/ vape./ etc
    """
    name = models.CharField(max_length=20)
    number_of_threads_and_messages = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def inc_number(self):
        self.number_of_threads_and_messages += 1
        self.save()


class Thread(models.Model):
    """
    Model of thread. Contains messages of users.
    """
    id_threads_messages = models.IntegerField(default=0)
    title = models.CharField(max_length=100, default='Title')
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField()
    last_message_pub_date = models.DateTimeField()
    sections = models.ForeignKey(Section, null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='threads/static/threads/images')
    video = models.FileField(null=True, blank=True, upload_to='threads/static/threads/videos')

    def get_last_messages(self, count=3):
        message_count = len(self.message_set.all())
        if message_count > 3:
            return self.message_set.all()[message_count - count:]
        else:
            return self.message_set.all()

    def messages_count(self, count=3):
        return len(self.message_set.all()) - count

    def save(self, is_new=True, *args, **kwargs):
        if is_new:
            self.last_message_pub_date = timezone.now()
            self.sections.inc_number()
            self.id_threads_messages = self.sections.number_of_threads_and_messages
        super().save(args, kwargs)

    def __str__(self):
        return self.title

    def set_image(self, image):
        self.image = image

    def image_name(self):
        if self.image.name == '':
            return 'False'
        return 'threads/images/' + os.path.basename(self.image.name)

    def video_name(self):
        if self.video.name == '':
            return 'False'
        return 'threads/videos/' + os.path.basename(self.video.name)


class Message(models.Model):
    """
    Model of user message in thread.
    """
    id_threads_messages = models.IntegerField(default=0)
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField()
    threads = models.ForeignKey(Thread, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='threads/static/threads/images')
    video = models.FileField(null=True, blank=True, upload_to='threads/static/threads/videos')

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.threads.last_message_pub_date = timezone.now()
        self.threads.save(is_new=False)
        self.threads.sections.inc_number()
        self.id_threads_messages = self.threads.sections.number_of_threads_and_messages
        super().save(args, kwargs)


    def image_name(self):
        if self.image.name == '':
            return 'False'
        return 'threads/images/' + os.path.basename(self.image.name)

    def video_name(self):
        if self.video.name == '':
            return 'False'
        return 'threads/videos/' + os.path.basename(self.video.name)
