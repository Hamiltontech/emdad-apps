# -*- coding: utf-8 -*-
# Part of emdad. See LICENSE file for full copyright and licensing details.

from emdad.addons.phone_validation.tools import phone_validation
from emdad.exceptions import UserError
from emdad.tests import tagged
from emdad.tests.common import BaseCase


@tagged('phone_validation')
class TestPhonenumbers(BaseCase):

    def test_country_code_falsy(self):
        self.assertEqual(
            phone_validation.phone_format('0456998877', 'BE', '32', force_format='E164'),
            '+32456998877'
        )
        # no country code -> UserError, no internal traceback
        with self.assertRaises(UserError):
            self.assertEqual(
                phone_validation.phone_format('0456998877', None, '32', force_format='E164'),
                '+32456998877'
            )

    def test_get_region_data_for_number(self):
        for source, (exp_code, exp_national_number, exp_phone_code) in zip(
            [
                '+32456998877',  # all hail Philippe
                '+1-613-555-0177',  # canada, same phone_code as US
                '+1-202-555-0124',  # us, same phone_code as CA
            ],
            [
                ('BE', '456998877', '32'),
                ('CA', '6135550177', '1'),
                ('US', '2025550124', '1'),
            ],
        ):
            with self.subTest(source=source):
                self.assertDictEqual(
                    phone_validation.phone_get_region_data_for_number(source),
                    {
                        'code': exp_code,
                        'national_number': exp_national_number,
                        'phone_code': exp_phone_code,
                    }
                )
