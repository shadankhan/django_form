from django import forms
from django.core import validators

# def check_s(value):
# 	if value[0] != 's':
# 		raise forms.ValidationError("Name needs to start with 'S'")


class FormObj(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	number = forms.IntegerField()
	bot_catcher = forms.CharField(widget=forms.HiddenInput, required=False)

	def clean_bot_catcher(self):
		bot_catcher = self.cleaned_data['bot_catcher']
		if len(bot_catcher) > 0:
			raise forms.ValidationError("You can't submit this form, 'BOT'!")
			
		return bot_catcher




