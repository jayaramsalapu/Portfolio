from django import forms

class CKEditorWidget(forms.Textarea):
    class Media:
        js = (
            'https://cdn.ckeditor.com/ckeditor5/41.1.0/classic/ckeditor.js',
            'js/ckeditor_init.js',
        )

    def __init__(self, attrs=None):
        default_attrs = {
            'class': 'ckeditor-5',
            'rows': 15,
            'cols': 80,
        }
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)
