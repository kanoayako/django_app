from django import forms
from.models import Friend

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'birthday', 'size', 'heel', 'fvbr', 'fvshbr', 'fvclbr', 'zodata', "appdata", 'add', 'ofadd', 'ofty', 'posi', 'out', 'pur', 'situ']
class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)
# class HelloForm(forms.Form):
#     name = forms.CharField(label='NAME')
#     mailadd = forms.EmailField(label='MAIL')
#     birthday = forms.DateField(label='BIRTHDAY')
#     size = forms.IntegerField(label='SIZE')
#     heel = forms.IntegerField(label='HEEL')
#     fvbr = forms.CharField(label='FAVORIT BRAND')
#     fvshbr = forms.CharField(label='FAVORIT SHOES BRAND')
#     fvclbr = forms.CharField(label='FAVORIT CLOTHES BRAND')
#     zodata = forms.CharField(label='ZOZO DATA')
#     appdata = forms.CharField(label='APP DATA')
#     add = forms.CharField(label='ADDRESS')
#     ofadd = forms.CharField(label='OFFICE ADRESS')
#     ofty = forms.CharField(label='業種')
#     posi = forms.CharField(label='POSITION')
#     out = forms.CharField(label='外出の有無')
#     pur = forms.CharField(label='今回のサービス利用の目的')
#     situ = forms.CharField(label='今回のサービス利用のシチュエーション')

        # id = forms.IntegerField(label='ID')

#     name = forms.CharField(label='name')
#     mail = forms.CharField(label='mail')
#     age = forms.IntegerField(label='age')
#     data=[
#             ('one','item 1'),
#             ('two','item 2'),
#             ('three','item 3'),
#             ('four','item 4'),
#             ('five','item 5'),
#     ]
#     choice =forms.MultipleChoiceField(label='radio', \
#             choices=data, widget=forms.SelectMultiple(attrs={'size': 6}))
    
    # check = forms.NullBooleanField(label='Check')

#     name = forms.CharField(label='name')
#     mail = forms.CharField(label='mail')
#     age = forms.IntegerField(label='age')
