from edc_dashboard.view_mixins import (
    ShowHideViewMixin, SubjectIdentifierViewMixin, ConsentViewMixin)
from edc_metadata.view_mixins.metadata_view_mixin import MetaDataViewMixin
from edc_appointment.view_mixins import AppointmentViewMixin

from ....model_wrappers import AppointmentModelWrapper
from .visit_schedule_view_mixin import VisitScheduleViewMixin
from .subject_visit_view_mixin import SubjectVisitViewMixin
from .subject_locator_view_mixin import SubjectLocatorViewMixin


class BaseDashboardView(
        MetaDataViewMixin,
        ConsentViewMixin,
        SubjectLocatorViewMixin,
        SubjectVisitViewMixin,
        AppointmentViewMixin,
        VisitScheduleViewMixin,
        ShowHideViewMixin,
        SubjectIdentifierViewMixin):

    appointment_model_wrapper_cls = AppointmentModelWrapper
