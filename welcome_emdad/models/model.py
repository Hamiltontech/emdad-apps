from emdad import models, api, fields

class ResContact(models.Model):
    _name="Contacts"
    name = fields.Char(string="Name")