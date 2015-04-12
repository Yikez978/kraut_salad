# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

from django.core.urlresolvers import reverse
from menu import Menu, MenuItem

incident_children = (
    MenuItem("List Incidents",
            reverse("incidents:list"),
            weight=10,
            image="images/Incident.png"),
    MenuItem("New Incident",
            reverse("incidents:new"),
            weight=80,
            separator=True),
)

Menu.add_item("incident", MenuItem("Incidents",
    reverse("incidents:home"),
    weight=10,
    children=incident_children)
)
