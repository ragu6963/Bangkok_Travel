from django import forms
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "제목을 입력하세요",
                "class": "form-control form-control-lg",
            }
        ),
    )
    url = forms.URLField(
        label="",
        label_suffix="",
        widget=forms.URLInput(
            attrs={
                "placeholder": "구글 스트리트뷰 주소를 입력해주세요",
                "class": "form-control form-control-sm",
            }
        ),
    )
    # content = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(
        label="",
        label_suffix="",
        widget=CKEditorWidget(attrs={}),
    )

    CHOICES = [
        ("asia", "아시아"),
        ("north_amrica", "북아메리카"),
        ("south america", "남아메리카"),
        ("europe", "유럽"),
        ("oceania", "오세아니아"),
        ("africa", "아프리카"),
    ]
    # category = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    url = forms.URLField(
        label="",
        label_suffix="",
        widget=forms.URLInput(
            attrs={
                "placeholder": "구글 스트리트뷰 주소를 입력해주세요",
            }
        ),
    )
