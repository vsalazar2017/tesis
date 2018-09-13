from odoo.addons.account.tests.account_test_users import AccountTestUsers
import datetime


class TestAccountCustomerInvoice(AccountTestUsers):

    def test_customer_invoice(self):
        super(TestAccountCustomerInvoice, self).test_customer_invoice()
        #Agregando Test de check
        assert (self.account_invoice_customer0.check == False), "Debe ser Verdadero"
