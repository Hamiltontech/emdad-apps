from emdad import api, fields, models

class EmdadProducts(models.Model):
    _name="emdad.products"

    name=fields.Char(string="Name")