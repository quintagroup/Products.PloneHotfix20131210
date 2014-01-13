# In Plone 2.0.x the imagePatch requires tag to have docstring, thus 
# it should import and run before the docstring is removed by this patch.
try:
    from Products.CMFPlone import imagePatch
except:
    pass
from OFS.Image import Image

del Image.tag.im_func.__doc__
