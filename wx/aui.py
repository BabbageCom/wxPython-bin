# This file is generated by wxPython's SIP generator.  Do not edit by hand.
#
# Copyright: (c) 2017 by Total Control Software
# License:   wxWindows License

"""
`wx.aui` provides a set of classes for implementing an "Advanced User Interface".
More specifically, these classes enable to you present some of your application in
floating or dockable panels, notebooks with floatable tabs, etc.

There is also a pure-python implementation of these classes available in the
`wx.lib.agw.aui` package.
"""

from ._aui import *

import wx

def _AuiPaneInfoArray___repr__(self):
    return "AuiPaneInfoArray: " + repr(list(self))
AuiPaneInfoArray.__repr__ = _AuiPaneInfoArray___repr__
del _AuiPaneInfoArray___repr__
EVT_AUI_PANE_BUTTON = wx.PyEventBinder( wxEVT_AUI_PANE_BUTTON )
EVT_AUI_PANE_CLOSE = wx.PyEventBinder( wxEVT_AUI_PANE_CLOSE )
EVT_AUI_PANE_MAXIMIZE = wx.PyEventBinder( wxEVT_AUI_PANE_MAXIMIZE )
EVT_AUI_PANE_RESTORE = wx.PyEventBinder( wxEVT_AUI_PANE_RESTORE )
EVT_AUI_PANE_ACTIVATED = wx.PyEventBinder( wxEVT_AUI_PANE_ACTIVATED )
EVT_AUI_RENDER = wx.PyEventBinder( wxEVT_AUI_RENDER )
EVT_AUI_FIND_MANAGER = wx.PyEventBinder( wxEVT_AUI_FIND_MANAGER )

def _AuiDockInfoArray___repr__(self):
    return "AuiDockInfoArray: " + repr(list(self))
AuiDockInfoArray.__repr__ = _AuiDockInfoArray___repr__
del _AuiDockInfoArray___repr__
def _AuiDockUIPartArray___repr__(self):
    return "AuiDockUIPartArray: " + repr(list(self))
AuiDockUIPartArray.__repr__ = _AuiDockUIPartArray___repr__
del _AuiDockUIPartArray___repr__
def _AuiPaneButtonArray___repr__(self):
    return "AuiPaneButtonArray: " + repr(list(self))
AuiPaneButtonArray.__repr__ = _AuiPaneButtonArray___repr__
del _AuiPaneButtonArray___repr__
def _AuiPaneInfoPtrArray___repr__(self):
    return "AuiPaneInfoPtrArray: " + repr(list(self))
AuiPaneInfoPtrArray.__repr__ = _AuiPaneInfoPtrArray___repr__
del _AuiPaneInfoPtrArray___repr__
def _AuiDockInfoPtrArray___repr__(self):
    return "AuiDockInfoPtrArray: " + repr(list(self))
AuiDockInfoPtrArray.__repr__ = _AuiDockInfoPtrArray___repr__
del _AuiDockInfoPtrArray___repr__
EVT_AUITOOLBAR_TOOL_DROPDOWN = wx.PyEventBinder( wxEVT_AUITOOLBAR_TOOL_DROPDOWN, 1 )
EVT_AUITOOLBAR_OVERFLOW_CLICK = wx.PyEventBinder( wxEVT_AUITOOLBAR_OVERFLOW_CLICK, 1 )
EVT_AUITOOLBAR_RIGHT_CLICK = wx.PyEventBinder( wxEVT_AUITOOLBAR_RIGHT_CLICK, 1 )
EVT_AUITOOLBAR_MIDDLE_CLICK = wx.PyEventBinder( wxEVT_AUITOOLBAR_MIDDLE_CLICK, 1 )
EVT_AUITOOLBAR_BEGIN_DRAG = wx.PyEventBinder( wxEVT_AUITOOLBAR_BEGIN_DRAG, 1 )

def _AuiToolBarItemArray___repr__(self):
    return "AuiToolBarItemArray: " + repr(list(self))
AuiToolBarItemArray.__repr__ = _AuiToolBarItemArray___repr__
del _AuiToolBarItemArray___repr__
def _AuiNotebookPageArray___repr__(self):
    return "AuiNotebookPageArray: " + repr(list(self))
AuiNotebookPageArray.__repr__ = _AuiNotebookPageArray___repr__
del _AuiNotebookPageArray___repr__
def _AuiTabContainerButtonArray___repr__(self):
    return "AuiTabContainerButtonArray: " + repr(list(self))
AuiTabContainerButtonArray.__repr__ = _AuiTabContainerButtonArray___repr__
del _AuiTabContainerButtonArray___repr__
EVT_AUINOTEBOOK_PAGE_CLOSE = wx.PyEventBinder( wxEVT_AUINOTEBOOK_PAGE_CLOSE, 1 )
EVT_AUINOTEBOOK_PAGE_CLOSED = wx.PyEventBinder( wxEVT_AUINOTEBOOK_PAGE_CLOSED, 1 )
EVT_AUINOTEBOOK_PAGE_CHANGED = wx.PyEventBinder( wxEVT_AUINOTEBOOK_PAGE_CHANGED, 1 )
EVT_AUINOTEBOOK_PAGE_CHANGING = wx.PyEventBinder( wxEVT_AUINOTEBOOK_PAGE_CHANGING, 1 )
EVT_AUINOTEBOOK_BUTTON = wx.PyEventBinder( wxEVT_AUINOTEBOOK_BUTTON, 1 )
EVT_AUINOTEBOOK_BEGIN_DRAG = wx.PyEventBinder( wxEVT_AUINOTEBOOK_BEGIN_DRAG, 1 )
EVT_AUINOTEBOOK_END_DRAG = wx.PyEventBinder( wxEVT_AUINOTEBOOK_END_DRAG, 1 )
EVT_AUINOTEBOOK_DRAG_MOTION = wx.PyEventBinder( wxEVT_AUINOTEBOOK_DRAG_MOTION, 1 )
EVT_AUINOTEBOOK_ALLOW_DND = wx.PyEventBinder( wxEVT_AUINOTEBOOK_ALLOW_DND, 1 )
EVT_AUINOTEBOOK_DRAG_DONE = wx.PyEventBinder( wxEVT_AUINOTEBOOK_DRAG_DONE, 1 )
EVT_AUINOTEBOOK_TAB_MIDDLE_DOWN = wx.PyEventBinder( wxEVT_AUINOTEBOOK_TAB_MIDDLE_DOWN, 1 )
EVT_AUINOTEBOOK_TAB_MIDDLE_UP = wx.PyEventBinder( wxEVT_AUINOTEBOOK_TAB_MIDDLE_UP, 1 )
EVT_AUINOTEBOOK_TAB_RIGHT_DOWN = wx.PyEventBinder( wxEVT_AUINOTEBOOK_TAB_RIGHT_DOWN, 1 )
EVT_AUINOTEBOOK_TAB_RIGHT_UP = wx.PyEventBinder( wxEVT_AUINOTEBOOK_TAB_RIGHT_UP, 1 )
EVT_AUINOTEBOOK_BG_DCLICK = wx.PyEventBinder( wxEVT_AUINOTEBOOK_BG_DCLICK, 1 )

