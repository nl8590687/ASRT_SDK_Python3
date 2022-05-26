#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2016-2099 Ailemon.net
#
# This file is part of ASRT Speech Recognition Tool Python SDK.
#
# ASRT is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# ASRT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ASRT.  If not, see <https://www.gnu.org/licenses/>.
# ============================================================================

"""
@author: nl8590687
ASRT语音识别Python SDK HTTP库模块
"""

import platform
import requests
from ..version import __version__


_HTTP_USER_AGENT = '%s%s%s%s%s' % ("ASRT-SDK client/", __version__,
    " (python", platform.python_version(), ") (https://asrt.ailemon.net/)")


def get_http_session():
    '''
    Get a http request session
    '''
    sess=requests.Session()
    sess.headers.update({"User-Agent":_HTTP_USER_AGENT})
    return sess
