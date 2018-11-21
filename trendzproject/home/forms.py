from django import forms
from home.models import Post

class create_post_form(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(
		attrs={

			'class':'form-control',
			'placeholder':'Add your Trend...'

		}
		))

	class Meta:
		model = Post

		fields = (
			'post',
			'post_image'
			)
