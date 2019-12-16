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
              "label": _("Store Information"),
              "description": _("Articles which members issue and return."),
            },
            # {
            #   "type": "doctype",
            #   "name": "Partner Information",
            #   "label": _("Partner Information"),
            #   "description": _("Articles which members issue and return."),
            # },
            {
              "type": "doctype",
              "name": "District",
              "label": _("District"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "District Manager",
              "label": _("District Manager"),
              "description": _("Articles which members issue and return."),
            },
            {
              "type": "doctype",
              "name": "Shift Manager",
              "label": _("Shift Manager"),
              "description": _("Articles which members issue and return."),
            },

          ]
      }
  ]