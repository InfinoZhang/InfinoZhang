from django.test import TestCase

from .models import Contract


class ContractModelTests(TestCase):
    def test_contract_table_uses_required_name_and_form_fields(self):
        field_names = {field.name for field in Contract._meta.fields}

        self.assertEqual(Contract._meta.db_table, 'contract')
        self.assertTrue(
            {
                'company',
                'name',
                'email',
                'phone',
                'category',
                'sku',
                'timeline',
                'asset_type',
                'budget',
                'platform',
                'note',
                'created_at',
            }.issubset(field_names)
        )

# Create your tests here.
