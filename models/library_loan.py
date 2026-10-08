import string

from odoo import fields,models

class LibraryLoan(models.Model):

    _name = 'library.loan'
    _description = 'Library Loan'


    loan_date = fields.Date(string='تاریخ گرفتن امانت')
    loan_expire = fields.Date(string='تاریخ انقضا')
    status = fields.Selection(selection=[
        ('ative', 'فعال'), ('returned','باز گرداننده شده'),
        ('late','دیرکرد')
    ])

    buyer_id = fields.Many2one("res.partner", string="امانت گیرنده")
    book_id = fields.Many2one("library.book",string="کتاب")
    copy_ids = fields.Many2one("library.book.copy",string="نسخه")
