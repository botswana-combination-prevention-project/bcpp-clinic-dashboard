from edc_appointment.view_mixins import (
    AppointmentViewMixin as BaseAppointmentMixin)

from ....model_wrappers import AppointmentModelWrapper


class AppointmentViewMixin(BaseAppointmentMixin):

    appointment_model_wrapper_cls = AppointmentModelWrapper
    model = 'bcpp_clinic_subject.appointment'
