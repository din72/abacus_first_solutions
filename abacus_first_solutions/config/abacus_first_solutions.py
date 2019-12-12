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

          ]
      }
  ]