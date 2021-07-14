from unittest.mock import patch

from doc_switch.doc_type_sniffer import sniff_type


class TestDocSniffer:
    def setup_method(self):
        self.docstring = r"""
    \"""
   :param str sender: The person sending the message
   :param str recipient: The recipient of the message
   :param str message_body: The body of the message
   :param priority: The priority of the message, can be a number 1-5
   :type priority: integer or None
   :return: the message id
   :rtype: int
   :raises ValueError: if the message_body exceeds 160 characters
   :raises TypeError: if the message_body is not a basestring
   \"""
        """.strip()

    @patch(target="doc_switch.doc_type_sniffer.input", return_value="abc")
    def test_doc_sniffer(self, mock_input):
        sniff_type(self.docstring)
