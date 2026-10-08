from odoo import fields, models, api



class Partner(models.Model):
    _inherit = "res.partner"

    customer_code = fields.Char(string="کد اشتراک")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])