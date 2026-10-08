from odoo import fields, models, api



class Partner(models.Model):
    _inherit = "res.partner"

    customer_code = fields.Char(string="کد اشتراک")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    book_ids = fields.One2many("library.loan",'buyer_id')