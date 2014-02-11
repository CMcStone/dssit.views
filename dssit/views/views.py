from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_acquire, aq_inner
from DateTime import DateTime

from dssit.views.interfaces import ITabularEventsView
from dssit.views.interfaces import ITileNewsView

class TabularEventsView(BrowserView):
    """
    tabular events browser view
    """
    implements(ITabularEventsView)
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        


    def getBodyText(self):
        return self.context.getBodyText()

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()  

class TileNewsView(BrowserView):
    """
    tabular events browser view
    """
    implements(ITileNewsView)
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        


    def getBodyText(self):
        return self.context.getBodyText()

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()  
