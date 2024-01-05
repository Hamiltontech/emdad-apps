from emdad import models, api, fields

class WelcomeApp(models.Model):
    _name = "emdad.hello"

    name = fields.Char(string="Name")