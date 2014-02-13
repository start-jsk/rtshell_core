#!/usr/bin/env python

PKG = 'rtshell'
NAME = 'run_rtshell_test'

import os
import sys
import time
import unittest
import yaml

import rostest

from subprocess import Popen, PIPE, check_call, call

class TestRtshellOnline(unittest.TestCase):

    def setUp(self):
        self.vals = set()
        self.msgs = {}

    def test_roslaunch(self):
        # network is initialized
        cmd = 'rtls'

        # check if rtshell runs
        check_call([cmd])

if __name__ == '__main__':
    rostest.run(PKG, NAME, TestRtshellOnline, sys.argv)
