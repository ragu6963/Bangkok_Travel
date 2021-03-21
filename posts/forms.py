from django import forms
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    # content = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(widget=CKEditorWidget())

    CHOICES = [
        ("asia", "아시아"),
        ("north_amrica", "북아메리카"),
        ("south america", "남아메리카"),
        ("europe", "유럽"),
        ("oceania", "오세아니아"),
        ("africa", "아프리카"),
    ]
    category = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    url = forms.URLField()