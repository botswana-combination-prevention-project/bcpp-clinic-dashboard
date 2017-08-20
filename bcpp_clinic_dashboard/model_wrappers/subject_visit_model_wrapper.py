from django.apps import apps as django_apps
from edc_model_wrapper import ModelWrapper


class SubjectVisitModelWrapper(ModelWrapper):

    model = 'bcpp_clinic_subject.subjectvisit'
    next_url_name = django_apps.get_app_config(
        'bcpp_clinic_dashboard').dashboard_url_name
    next_url_attrs = ['subject_identifier', 'appointment']

    @property
    def appointment(self):
        return self.object.appointment.id
