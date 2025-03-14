from flectra.exceptions import UserError
from flectra.tests import common


class TestDocumentPageShowDiff(common.TransactionCase):
    """document_page_show_diff test class."""

    def test_show_demo_page1_diff(self):
        """Show test page history difference."""
        page = self.env.ref('document_page.demo_page1')

        show_diff_object = self.env['wizard.document.page.history.show_diff']

        history_document = self.env['document.page.history']
        history_pages = history_document.search([('page_id', '=', page.id)])

        self.assertTrue(
            show_diff_object.with_context(
                active_ids=[i.id for i in history_pages]
            )._get_diff()
        )

        page.write({'content': 'Text content updated'})
        page.write({'content': 'Text updated'})

        history_pages = history_document.search([('page_id', '=', page.id)])

        with self.assertRaises(UserError):
            show_diff_object.with_context(
                active_ids=[i.id for i in history_pages]
            )._get_diff()
