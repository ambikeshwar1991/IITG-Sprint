#!/usr/bin/env python
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
import time

class local_source(gr.sync_block):
    """
    docstring for block timer_rises
    """
    def __init__(self, sig, part, tstart, tstop, tstep):
        gr.sync_block.__init__(self,
            name="local_source",
            in_sig=None,
            out_sig=[numpy.float32])
        self.i = 0
        self.sig = sig
        self.part = part
        self.tstart = tstart
        self.tstop = tstop
        self.tstep = tstep
	self.num = (tstop-tstart)/tstep


    def evenn(self):
	x=numpy.array(numpy.arange(self.tstart,self.tstop,self.tstep))
	if self.sig==1:
	    self.a1=numpy.sin(x)
	    self.a2=numpy.sin(-x)
	    if self.part==1:
	        self.y = self.a1+self.a2
	    elif self.part==2:
		self.y = self.a1-self.a2
	elif self.sig==2:
	    self.a1=numpy.cos(x)
	    self.a2=numpy.cos(-x)
	    if self.part==1:
                self.y = self.a1+self.a2
            elif self.part==2:
                self.y = self.a1-self.a2



    def work(self, input_items, output_items):
#        in0 = input_items[0]
        out = output_items[0]
        self.evenn()
        out[:] = self.y[self.i]
        self.i = self.i+1
        if self.i >= self.num:
            self.i = 0
        print "i val\n",self.i

    # <+signal processing here+>
        return len(output_items[0])

