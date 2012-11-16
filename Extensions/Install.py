from Products.CMFCore.utils import getToolByName

def install(portal):
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.setImportContext('profile-ArchimaeraTheme:archimaeratheme')
    setup_tool.runAllImportSteps()
    setup_tool.setImportContext('profile-CMFPlone:plone')
    return "Ran all import steps."