# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from itertools import count

class CreateUserEmployee(models.Model):
    _inherit = "hr.employee"

    @api.model_create_multi
    def create(self, vals):
        recs = super(CreateUserEmployee, self).create(vals) #tạo ra 1 nvien
        for rec in recs:
            if self.env['res.users'].sudo().search([('login', '=', rec.work_email)]).id:
                raise ValidationError(_('This email is already used by another user'))
            elif not rec.user_id:
                user_info = {'name': rec.name,
                             'login': rec.work_email,
                             'email': rec.work_email,
                             'state': 'active',
                             'partner_id': rec.work_contact_id.id}
                account = self.env['res.users'].sudo().create(user_info)
                rec.user_id = account.id
        return recs


class HrApplicantInherit(models.Model):
    _inherit = 'hr.applicant'

    def _get_employee_create_vals(self):
        self.ensure_one()
        address_id = self.partner_id.address_get(['contact'])['contact']
        address_sudo = self.env['res.partner'].sudo().browse(address_id)
        return {
            'name': self.partner_name or self.partner_id.display_name,
            'work_contact_id': self.partner_id.id,
            'job_id': self.job_id.id,
            'job_title': self.job_id.name,
            'private_street': address_sudo.street,
            'private_street2': address_sudo.street2,
            'private_city': address_sudo.city,
            'private_state_id': address_sudo.state_id.id,
            'private_zip': address_sudo.zip,
            'private_country_id': address_sudo.country_id.id,
            'private_phone': address_sudo.phone,
            'private_email': address_sudo.email,
            'lang': address_sudo.lang,
            'department_id': self.department_id.id,
            'address_id': self.company_id.partner_id.id,
            'work_email': self.email_from, # To have a valid email address by default
            'work_phone': self.department_id.company_id.phone,
            'applicant_id': self.ids,
        }
