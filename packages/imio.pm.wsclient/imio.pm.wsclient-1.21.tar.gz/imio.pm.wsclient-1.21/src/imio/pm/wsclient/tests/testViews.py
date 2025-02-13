# -*- coding: utf-8 -*-
#
# File: testItemMethods.py
#
# GNU General Public License (GPL)
#

from imio.pm.ws.config import POD_TEMPLATE_ID_PATTERN
from imio.pm.wsclient.config import ANNEXID_MANDATORY_ERROR
from imio.pm.wsclient.config import CORRECTLY_SENT_TO_PM_INFO
from imio.pm.wsclient.config import FILENAME_MANDATORY_ERROR
from imio.pm.wsclient.config import MISSING_FILE_ERROR
from imio.pm.wsclient.config import UNABLE_TO_CONNECT_ERROR
from imio.pm.wsclient.config import UNABLE_TO_DETECT_MIMETYPE_ERROR
from imio.pm.wsclient.tests.WS4PMCLIENTTestCase import cleanMemoize
from imio.pm.wsclient.tests.WS4PMCLIENTTestCase import createDocument
from imio.pm.wsclient.tests.WS4PMCLIENTTestCase import WS4PMCLIENTTestCase
from mock import Mock
from mock import patch
from Products.statusmessages.interfaces import IStatusMessage

import base64


class testViews(WS4PMCLIENTTestCase):
    """
        Tests the browser.settings SOAP client methods
    """
    def test_generateItemTemplateView(self):
        """
          Test the BrowserView that generates a given template of an item
        """
        self.changeUser('admin')
        messages = IStatusMessage(self.request)
        document = createDocument(self.portal)
        DOCUMENT_ABSOLUTE_URL = document.absolute_url()
        # we must obviously be connected to PM...
        view = document.restrictedTraverse('@@generate_document_from_plonemeeting')
        # nothing is generated, just redirected to the context
        self.assertFalse(view() != DOCUMENT_ABSOLUTE_URL)
        self.assertTrue(len(messages.show()) == 1)
        self.assertTrue(messages.show()[0].message == UNABLE_TO_CONNECT_ERROR)
        # _soap_connectToPloneMeeting is memoized...
        cleanMemoize(self.request)
        item = self._sendToPloneMeeting(document)
        # a statusmessage for having created the item successfully
        self.assertEqual(messages.show()[-1].message, CORRECTLY_SENT_TO_PM_INFO)
        view = document.restrictedTraverse('@@generate_document_from_plonemeeting')
        # with no templateFormat defined, the mimetype can not be determined
        # an error statusmessage is displayed
        # last added statusmessage
        # nothing is generated, just redirected to the context
        self.assertFalse(view() != DOCUMENT_ABSOLUTE_URL)
        self.assertEqual(messages.show()[-1].message, UNABLE_TO_DETECT_MIMETYPE_ERROR)
        self.request.set('templateFormat', 'odt')
        # if no templateFilename, an error is displayed, nothing is generated
        view = document.restrictedTraverse('@@generate_document_from_plonemeeting')
        # nothing is generated, just redirected to the context
        self.assertFalse(view() != DOCUMENT_ABSOLUTE_URL)
        self.assertEqual(messages.show()[-1].message, FILENAME_MANDATORY_ERROR)
        # if not valid itemUID defined, the item can not be found and so accessed
        self.request.set('templateFilename', 'filename')
        view = document.restrictedTraverse('@@generate_document_from_plonemeeting')
        # nothing is generated, just redirected to the context
        self.assertFalse(view() != DOCUMENT_ABSOLUTE_URL)
        self.assertEqual(
            messages.show()[-1].message, u"An error occured while generating the document in "
            "PloneMeeting!  The error message was : Server raised fault: 'You can not access this item!'"
        )
        # now with a valid itemUID but no valid templateId
        self.request.set('itemUID', item.UID())
        view = document.restrictedTraverse('@@generate_document_from_plonemeeting')
        # nothing is generated, just redirected to the context
        self.assertFalse(view() != DOCUMENT_ABSOLUTE_URL)
        self.assertEqual(
            messages.show()[-1].message, u"An error occured while generating the document in "
            "PloneMeeting!  The error message was : Server raised fault: 'You can not access this template!'"
        )
        # now with all valid infos
        self.request.set('templateId', POD_TEMPLATE_ID_PATTERN.format('itemTemplate', 'odt'))
        view = document.restrictedTraverse('@@generate_document_from_plonemeeting')
        res = view()
        # with have a real result, aka not redirected to the context, a file
        self.assertTrue(view() != DOCUMENT_ABSOLUTE_URL)
        self.assertTrue(len(res) > 10000)
        self.assertEquals(self.request.response.headers,
                          {'content-type': 'application/vnd.oasis.opendocument.text',
                           'location': '{0}/document'.format(self.portal.absolute_url()),
                           'content-disposition': 'inline;filename="filename.odt"'})

    def test_DownloadAnnexFromItemView_without_annex_id(self):
        """
          Test the BrowserView that return the annex of an item
        """
        messages = IStatusMessage(self.request)
        self.changeUser('admin')
        download_annex = self.portal.restrictedTraverse('@@download_annex_from_plonemeeting')
        # mock connexion to PloneMeeting
        download_annex.ws4pmSettings._soap_connectToPloneMeeting = Mock(return_value=True)
        download_annex()
        self.assertEqual(messages.show()[-1].message, ANNEXID_MANDATORY_ERROR)

    @patch('imio.pm.wsclient.browser.settings.WS4PMClientSettings._soap_getItemInfos')
    def test_DownloadAnnexFromItemView_with_no_result(self, _soap_getItemInfos):
        """
          Test the BrowserView that return the annex of an item
        """
        # return no annex
        _soap_getItemInfos.return_value = None
        messages = IStatusMessage(self.request)
        self.changeUser('admin')
        document = createDocument(self.portal)
        self.request.set('annex_id', 'my_annex')
        download_annex = document.restrictedTraverse('@@download_annex_from_plonemeeting')
        # mock connexion to PloneMeeting
        download_annex.ws4pmSettings._soap_connectToPloneMeeting = Mock(return_value=True)
        download_annex()
        self.assertEqual(messages.show()[-1].message, MISSING_FILE_ERROR)

    @patch('imio.pm.wsclient.browser.settings.WS4PMClientSettings._soap_getItemInfos')
    def test_DownloadAnnexFromItemView(self, _soap_getItemInfos):
        """
          Test the BrowserView that return the annex of an item
        """
        # return an annex
        annex_id = 'my_annex'
        _soap_getItemInfos.return_value = [type(
            'ItemInfo', (object,), {
                'annexes': [
                    type(
                        'AnnexInfo', (object,), {
                            'id': annex_id,
                            'filename': 'my_annex.pdf',
                            'file': base64.b64encode('Hello!')
                        }
                    )
                ]
            }
        )]
        self.changeUser('admin')
        document = createDocument(self.portal)
        self.request.set('annex_id', annex_id)
        download_annex = document.restrictedTraverse('@@download_annex_from_plonemeeting')
        # mock connexion to PloneMeeting
        download_annex.ws4pmSettings._soap_connectToPloneMeeting = Mock(return_value=True)
        annex = download_annex()
        self.assertEqual(annex, 'Hello!')
        self.assertEqual(self.request.RESPONSE.headers.get('content-type'), 'application/pdf')
        self.assertEqual(
            self.request.RESPONSE.headers.get('content-disposition'),
            'inline;filename="my_annex.pdf"'
        )


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    # add a prefix because we heritate from testMeeting and we do not want every tests of testMeeting to be run here...
    suite.addTest(makeSuite(testViews, prefix='test_'))
    return suite
