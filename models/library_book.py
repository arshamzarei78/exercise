from odoo.exceptions import ValidationError

from odoo import api, models, fields
from odoo.exceptions import UserError


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"
    #_inherit = ["mail.thread","mail.activity.mixin"]

    name = fields.Char(string='عنوان', required=True)
    author = fields.Char(string='نویسنده')
    publisher = fields.Char(string='ناشر')
    ISBN = fields.Integer(string='شابک')
    category = fields.Selection([('scifi', 'علمی و تخیلی'), ('politic', 'سیاسی'), ('business', 'اقتصاد'), ('university', 'دانشگاهی'), ('konkour', 'کنکور')],
                                          string='دسته بندی')
    date = fields.Char(string='تاریخ انتشار',default=lambda self: fields.Date.today().strftime('%Y-%m'))
    language = fields.Char(string='زبان')
    price = fields.Integer(string='قیمت کتاب')
    description = fields.Text(string='توضیحات')
    active = fields.Boolean(string='فعال', default=True)
    status = fields.Selection([('exist', 'موجود'), ('all_loaned', 'همگی امانت داده شده اند'), ('lost', 'مفقود'),('Discontinued', 'رد شده')],string='وضعیت')
    copy_ids = fields.One2many('library.book.copy','book_id',string='نسخه‌ها')



    _sql_constraints = [('ISBN_unique','UNIQUE(ISBN)','ISBN must be unique!')]