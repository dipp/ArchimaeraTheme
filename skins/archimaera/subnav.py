# -*- coding: utf-8 -*-
## Script (Python) "subnav"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

# Wird vom Portlet portlet_menulogo aufgerufen, um die URL des
# Elternordners zu erhalten, wenn dort die Property menu_logo
# gesetzt ist

request  = container.REQUEST
RESPONSE = request.RESPONSE

has_menu_logo = False
parent = context

while has_menu_logo == False:
    if parent.hasProperty("menu_logo"):
        has_menu_logo = True
    else:
        parent = parent.getParentNode()


return parent.absolute_url()
