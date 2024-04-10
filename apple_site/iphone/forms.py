from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'







    # nikname = forms.CharField(max_length=200, label='Введите свой никнейм')
    # rev = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows':5}), label='Оставьте свой комментарий')

