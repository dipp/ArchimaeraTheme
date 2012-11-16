## Script (Python) "subnav"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##

# -*- coding: utf-8 -*-
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
