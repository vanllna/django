from django import forms


class UserCommentForm(forms.Form):
    coures = forms.IntegerField(required=True)
    content = forms.CharField(required=True,min_length=1,max_length=100)

