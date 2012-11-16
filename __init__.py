# Register our skins directory - this makes it available via portal_skins.
# register our profile

from Products.CMFCore.DirectoryView import registerDirectory

from Products.GenericSetup import EXTENSION, profile_registry
from Products.CMFPlone.interfaces import IPloneSiteRoot

GLOBALS = globals()
registerDirectory('skins', GLOBALS)

profile_registry.registerProfile(
                    'archimaeratheme',
                    'ArchimaeraTheme',
                    'Extension profile for ArchimaeraTheme Product',
                    'profile',
                    'ArchimaeraTheme',
                    EXTENSION,
                    for_=IPloneSiteRoot)
