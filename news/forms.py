from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "New Title", "class": "form-control"}))
    desc = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 10,
                "class": "form-control"
            }
        )
    )
    img = forms.FileField(widget=forms.FileInput(attrs={"placeholder": "Place an iamge", "class": "form-control"}))

    class Meta:
        model = Blog
        fields = [
            'title',
            'desc',
            'img'
        ]
