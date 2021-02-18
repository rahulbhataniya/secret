from .models import DigitalCertificate, Message
from django.forms import ModelForm
from Crypto.Cipher import AES
from base64 import encodebytes 
from base64 import decodebytes 
from .modified_AES import AESCipher

class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = ['user_name', 'message', 'encrypted_message', 'hashed_message']

        labels = {
            'user_name': 'To',
            'encrypted_message': 'Cipher Text',
            'hashed_message': 'SHA3 Hashed'
        }
    def clean_encrypted_message(self):
        obj=AESCipher("This is a key123")
        encrypted_msg=obj.encrypt(self.cleaned_data['message'])
        return encrypted_msg
    def clean_hashed_message(self):
        obj=AESCipher("This is a key123")
        hased_msg=obj.has_message(self.cleaned_data['message'])
        return hased_msg

