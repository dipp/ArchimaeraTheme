Description

    ArchimaeraTheme is a product that adds a new style to a Plone 2.5.x portal.
    It adds a new skin selection to the 'portal_skins' tool
    (called archimaera), and registers a custom stylesheet (called 
    archimaera.css) with the 'portal_css' tool.

    ArchimaeraTheme is based on DIYPloneStyle 2.5, a skeleton product
    ready for building new graphical designs for Plone.

Installation

    Place ArchimaeraTheme in the Products directory of your Zope instance
    and restart the server.

    The classic way:

      Go to the 'Site Setup' page in the Plone interface and click on the
      'Add/Remove Products' link.

      Choose the product (check its checkbox) and click the 'Install' button.

      Uninstall -- This can be done from the same management screen, but only
      if you installed it from the quick installer.

    The Generic Setup way:

      In the ZMI, go to 'portal_setup' and, (1) select the 'Properties' tab
      and choose ArchimaeraTheme in the popup list before clicking 'Update'.
      Then (2) go to the 'Import' tab and click 'Import all steps'.

      While adding a Plone Site to Zope (from the ZMI), you can select
      ArchimaeraTheme in the proposed Extension Profiles to have it installed
      automatically during the creation of the portal.

      Uninstall -- This must be done manually from the ZMI, as GenericSetup
      does not have an API for removing/uninstalling stuff (yet).

    Note: You may have to empty your browser cache to see the effects of the
    product installation.

Selecting a skin

    Depending on the values given in the skins tool profile (see
    profiles/default/skins.xml), the skin will be selected (or not) as default
    one while installing the product. If you need to switch from a default
    skin to another, go to the 'Site Setup' page, and choose 'Skins' (as
    portal manager). You can also decide from that page if members can choose
    their preferred skin and, in that case, if the skin cookie should be
    persistent.

    Note -- Don't forget to perform a full refresh of the page or reload all
    images (not from browser cache) after selecting a skin. In Firefox, you
    can do so by pressing the 'shift' key while reloading the page. In IE, use
    the key combination <Ctrl-F5>.

Written by

    John Doe <john.doe@dev.null>
