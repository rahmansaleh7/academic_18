from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

class Attendee(models.Model):
    _name = 'academic.attendee'
    _description = 'Attendee'

    name = fields.Char(string='Name')
    session_id = fields.Many2one('academic.session', string='Session', ondelete='cascade')
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    course_id = fields.Many2one(related='session_id.course_id', store=True)

    # constraint di Session hanya jalan saat attendee_ids diubah lewat Session,
    # jadi dicek juga di sini untuk attendee yang dibuat langsung (menu / wizard)
    @api.constrains('partner_id', 'session_id')
    def _check_instructor(self):
        for rec in self:
            if rec.partner_id and rec.partner_id == rec.session_id.instructor_id:
                raise UserError(_('Instructor cannot be an attendee'))
