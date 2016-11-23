#!/usr/bin/python
# -*- coding: utf-8 -*-
""" ShapeOut - info control panel
"""
from __future__ import division, print_function

import wx

from .controls_subpanel import SubPanel

# These are values hidden in the user interface
HIDDEN = ["shutter time",
          "video frameoffset",
          "bin ops",
          "blur",
          "diff_method",
          "margin",
          "shutter time",
          "tap code",
          "tap mode",
          "x-pos",
          "y-pos",
          ]


class SubPanelInfo(SubPanel):
    def __init__(self, *args, **kwargs):
        SubPanel.__init__(self, *args, **kwargs)

    def UpdatePanel(self, analysis):
        """  """
        self.ClearSubPanel()

        # Create three boxes containing information
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        genbox = self._box_from_cfg_read(analysis, "General", ignore=HIDDEN)
        imbox = self._box_from_cfg_read(analysis, "Image", ignore=HIDDEN)
        frbox = self._box_from_cfg_read(analysis, "Framerate", ignore=HIDDEN)
        roibox = self._box_from_cfg_read(analysis, "ROI", ignore=HIDDEN)
        # same size 
        h = genbox.GetMinSize()[1]
        h = max(h, imbox.GetMinSize()[1])
        h = max(h, frbox.GetMinSize()[1])
        h = max(h, roibox.GetMinSize()[1])
        h = max(h, 50)
        genbox.SetMinSize((-1, h))
        imbox.SetMinSize((-1, h))
        frbox.SetMinSize((-1, h))
        roibox.SetMinSize((-1, h))
        sizer.Add(genbox)
        sizer.Add(imbox)
        sizer.Add(frbox)
        sizer.Add(roibox)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()