## Script (Python) "getPastasRaiz"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
path={ "query": "/automator", 'depth': 1 }
pastas = context.portal_catalog.searchResults(Type=['Folder'], sort_on="getObjPositionInParent", review_state="published", path=path)

return pastas
