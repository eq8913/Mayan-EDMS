from __future__ import unicode_literals

from django.conf.urls import url

from .api_views import (
    APIDocumentOCRView, APIDocumentPageOCRContentView,
    APIDocumentVersionOCRView
)
from .views import (
    DocumentOCRContent, DocumentOCRDownloadView, DocumentOCRErrorsListView,
    DocumentPageOCRContent, DocumentSubmitView, DocumentTypeSettingsEditView,
    DocumentTypeSubmitView, EntryListView
)

urlpatterns = [
    url(
        r'^document/page/(?P<pk>\d+)/content/$',
        DocumentPageOCRContent.as_view(), name='document_page_ocr_content'
    ),
    url(
        r'^document/(?P<pk>\d+)/content/$', DocumentOCRContent.as_view(),
        name='document_ocr_content'
    ),
    url(
        r'^document/(?P<pk>\d+)/submit/$', DocumentSubmitView.as_view(),
        name='document_submit'
    ),
    url(
        r'^document/type/submit/$', DocumentTypeSubmitView.as_view(),
        name='document_type_submit'
    ),
    url(
        r'^document/multiple/submit/$', DocumentSubmitView.as_view(),
        name='document_submit_multiple'
    ),
    url(
        r'^document_type/(?P<pk>\d+)/ocr/settings/$',
        DocumentTypeSettingsEditView.as_view(),
        name='document_type_ocr_settings'
    ),
    url(
        r'^documents/(?P<pk>\d+)/ocr/errors/$',
        DocumentOCRErrorsListView.as_view(), name='document_ocr_error_list'
    ),
    url(
        r'^documents/(?P<pk>\d+)/ocr/download/$',
        DocumentOCRDownloadView.as_view(), name='document_ocr_download'
    ),
    url(r'^all/$', EntryListView.as_view(), name='entry_list'),
]

api_urls = [
    url(
        r'^documents/(?P<pk>\d+)/submit/$', APIDocumentOCRView.as_view(),
        name='document-ocr-submit-view'
    ),
    url(
        r'^documents/(?P<document_pk>\d+)/versions/(?P<version_pk>\d+)/ocr/$',
        APIDocumentVersionOCRView.as_view(),
        name='document-version-ocr-submit-view'
    ),
    url(
        r'^documents/(?P<document_pk>\d+)/versions/(?P<version_pk>\d+)/pages/(?P<page_pk>\d+)/ocr/$',
        APIDocumentPageOCRContentView.as_view(),
        name='document-page-ocr-content-view'
    ),
]
