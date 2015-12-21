#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import pytz
from time import tzname


def get_current_time_in_utc():
    UTC_tz = pytz.timezone('UTC')
    return UTC_tz.localize(datetime.datetime.utcnow())
