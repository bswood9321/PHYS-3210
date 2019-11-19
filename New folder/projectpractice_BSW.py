# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:26:02 2019

@author: BSWOOD9321
"""
import numpy as np
import mayavi.mlab

x,y,z=np.ogrid[-10:10:20j,-10:10:20j,-10:10,20j]
s = np.sin(x*y*z)/(x*y*z)

mlab.pipeline.volume(mlab.pipeline.scalar_field(s))
mlab.show()