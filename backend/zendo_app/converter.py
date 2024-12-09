from django.urls.converters import StringConverter


class IntOrStrConverter(StringConverter):
    regex = r"[0-9]+|[a-zA-Z]+"

    def to_python(self, value):
        try:
            return int(value)
        except ValueError:
            return value

    def to_url(self, value):
        return str(value)
