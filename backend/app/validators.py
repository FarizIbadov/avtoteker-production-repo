from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

import phonenumbers


@deconstructible
class ContentTypeValidator:
    message = 'File mime_type “%(mime_type)s” is not allowed. Allowed mime_types are: %(mime_types)s.'
    
    code = 'invalid_mime_type'

    def __init__(self, mime_types=None, message=None, code=None):
        if mime_types is not None:
            mime_types = [mime_type.lower() for mime_type in mime_types]
        self.mime_types = mime_types
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if value and value._file:
            mime_type = value._file.content_type.lower()
            if self.mime_types is not None and mime_type not in self.mime_types:
                raise ValidationError(
                    self.message,
                    code=self.code,
                    params={
                        'mime_type': mime_type,
                        'mime_types': ', '.join(self.mime_types),
                        'value': value,
                    }
                )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.mime_types == other.mime_types and
            self.message == other.message and
            self.code == other.code
        )


@deconstructible
class PhoneValidator:
    message = 'Invalid phone number'  
    
    code = 'invalid_phone_number'

    def __call__(self,value):
        try:
            phone_number = phonenumbers.parse(value,region="AZ")

            if not phonenumbers.is_valid_number(phone_number):
                raise phonenumbers.NumberParseException("error","error")
            return value
        except phonenumbers.NumberParseException:
            raise ValidationError(self.message)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) 
        )


class CustomValidators:
    @staticmethod
    def check_mime_type(value):
        MIME_TYPES = ['image/svg+xml','image/png','image/jpeg']
        if value._file:
            content_type = value._file.content_type
            try:
                MIME_TYPES.index(content_type)
            except ValueError:
                raise ValidationError("Invalid File")