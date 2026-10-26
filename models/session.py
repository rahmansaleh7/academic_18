from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

class Session(models.Model):
    _name = 'academic.session'
    _description = 'Session'
    _order = 'start_date desc'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date', default=fields.Date.context_today)
    duration = fields.Integer(string='Duration', help='Durasi (hari)')
    seats = fields.Integer(string='Number of seats')
    active = fields.Boolean(string='Active', default=True)
    course_id = fields.Many2one('academic.course', string='Course',
                                ondelete='cascade', required=True)
    instructor_id = fields.Many2one('res.partner', string='Instructor')
    taken_seats = fields.Float(string='Taken Seats', compute='_compute_taken_seats',
                               store=True, aggregator='avg')
    attendee_ids = fields.One2many('academic.attendee', 'session_id', string='Attendees')
    end_date = fields.Date(string='End Date', compute='_compute_end_date', store=True)
    image = fields.Image(string='Image', max_width=512, max_height=512)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ], string='Status', default='draft', required=True)

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for rec in self:
            d = max(rec.duration - 1, 0)
            rec.end_date = rec.start_date and fields.Date.add(rec.start_date, days=d)

    @api.depends('seats', 'attendee_ids')
    def _compute_taken_seats(self):
        for rec in self:
            if not rec.seats:
                rec.taken_seats = 0.0
            else:
                rec.taken_seats = (100.0 * len(rec.attendee_ids)) / rec.seats

    @api.onchange('seats', 'attendee_ids')
    def _onchange_seats(self):
        if self.seats < 0:
            return {'warning': {
                'title': _('Incorrect seats value'),
                'message': _('Seats cannot be negative'),
            }}
        if self.seats < len(self.attendee_ids):
            return {'warning': {
                'title': _('Too many attendees'),
                'message': _('Add seats or remove attendees'),
            }}

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor(self):
        for rec in self:
            if rec.instructor_id and rec.instructor_id in rec.attendee_ids.partner_id:
                raise UserError(_('Instructor cannot be an attendee'))

    def action_confirm(self):
        self.write({'state': 'confirmed'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_draft(self):
        self.write({'state': 'draft'})
