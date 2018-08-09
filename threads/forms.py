from django import forms


class ThreadForm(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок треда.')
    text = forms.CharField(max_length=1000, label='Сообщение треда.', widget=forms.Textarea(attrs={'rows': 4, 'cols': 30}))
    image = forms.ImageField(required=False, label='Картинка.')
    video = forms.FileField(required=False, label='Видео.')


class MessageForm(forms.Form):
    text = forms.CharField(max_length=1000, label='Ваше сообщение.', widget=forms.Textarea(attrs={'rows': 4, 'cols': 30}))
    image = forms.ImageField(required=False, label='Ваша картинка.')
    video = forms.FileField(required=False, label='Ваше видео.')
