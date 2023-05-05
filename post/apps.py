from django.apps import AppConfig
from django.templatetags.static import static


class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'


    # def ready(self):
    #     from ckeditor_uploader.fields import RichTextUploadingFormField
    #     from ckeditor.configs import DEFAULT_CONFIG
    #     config = DEFAULT_CONFIG.copy()
    #     config['toolbar'] = 'Custom'
    #     config['toolbar_Custom'] = [
    #         ['Bold', 'Italic', 'Underline'],
    #         ['Link', 'Unlink'],
    #         ['RemoveFormat', 'Source'],
    #     ]
    #     config['contentsCss'] = [
    #         static('css/ckeditor.css'),
    #     ]
    #     RichTextUploadingFormField.default_config = config
