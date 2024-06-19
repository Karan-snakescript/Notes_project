from django import forms
from .models import Note, Comment

class MultipleFileInput(forms.ClearableFileInput):
    template_name = 'widgets/multiple_file_input.html'

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    # files = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Comment
        fields = ['text','file']
