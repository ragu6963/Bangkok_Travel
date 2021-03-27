from django import forms
from .models import Comment
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "autocomplete": "off",
                "placeholder": "제목을 작성하세요",
                "class": "form-control form-control-lg mb-3",
            }
        ),
    )
    url = forms.URLField(
        label="",
        label_suffix="",
        widget=forms.URLInput(
            attrs={
                "autocomplete": "off",
                "placeholder": "구글 스트리트뷰 주소를 작성하세요",
                "class": "form-control form-control-sm mb-3",
            }
        ),
    )
    content = forms.CharField(
        label="",
        label_suffix="",
        widget=CKEditorWidget(),
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


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label="",
        label_suffix="",
        widget=forms.TextInput(
            attrs={
                "autocomplete": "off",
                "placeholder": "댓글을 작성하세요",
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = Comment
        exclude = [
            "post",
            "user",
        ]
