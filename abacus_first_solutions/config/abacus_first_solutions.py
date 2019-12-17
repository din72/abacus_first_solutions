from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Abacus First Solutions"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Store Information",
              "onboard": 1,
              "label": _("Store Information"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Abacus Supervisor",
              "onboard": 1,
              "label": _("Abacus Supervisor"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "District Manager",
              "onboard": 1,
              "label": _("District Manager"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Shift Manager",
              "onboard": 1,
              "label": _("Shift Manager"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "District",
              "label": _("District"),
              "description": _("Articles which members issue and return."),
            },

          ]
      }
  ]