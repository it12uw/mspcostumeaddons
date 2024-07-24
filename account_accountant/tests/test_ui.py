# -*- coding: utf-8 -*-
# Part of flectra. See LICENSE file for full copyright and licensing details.

import flectra.tests

@flectra.tests.common.at_install(False)
@flectra.tests.common.post_install(True)
class TestUi(flectra.tests.HttpCase):
    def test_ui(self):
        self.phantom_js("/web", "flectra.__DEBUG__.services['web_tour.tour'].run('account_reports_widgets', 'test')", "flectra.__DEBUG__.services['web_tour.tour'].tours.account_reports_widgets", login='admin')
