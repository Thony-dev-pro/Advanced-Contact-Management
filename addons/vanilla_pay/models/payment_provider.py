from odoo import models, fields

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Char(string='Vanilla Pay', help='vanilla')
    
    def _compute_feature_support_fields(self):
        super()._compute_feature_support_fields()
        self.filtered(lambda p: p.code == 'custom').update({
            'support_express_checkout': False,
            'support_manual_capture': False,
            'support_refund': 'none',
            'support_tokenization': False,
        })