#!/usr/bin/env python

from datetime import datetime

today = datetime.now().isocalendar()

#: Generate the current version
version = "{0}.{1}.{2}".format(today[0]%100, today[1], today[2])
