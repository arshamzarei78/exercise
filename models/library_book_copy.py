from odoo.exceptions import ValidationError

from odoo import api, models, fields
from odoo.exceptions import UserError


class LibraryBookCopy(models.Model):
    _name = "library.book.copy"

    name = fields.Char(string='نام نسخه')
    book_id = fields.Many2one('library.book', string='کتاب', required=True)

    author = fields.Char(related='book_id.author', string='نویسنده', store=True)

    publisher = fields.Char(related='book_id.publisher', string='ناشر', store=True)
