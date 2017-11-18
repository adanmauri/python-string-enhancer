#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @license
# Copyright 2017 Adán Mauri Ungaro <adan.mauri@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

def union(str1, str2):
    tmpStr1 = str1;
    tmpStr2 = str2;

    if (len(tmpStr1) < len(tmpStr2)):
        tmpStr2 = tmpStr2[:len(tmpStr1)]
    else:
        if (len(tmpStr2) < len(tmpStr1)):
            tmpStr1 = tmpStr1[len(tmpStr1)-len(tmpStr2):len(tmpStr1)]
	
    while True:
        if (tmpStr2 in tmpStr1):
            break
        tmpStr1 = tmpStr1[1:]
        tmpStr2 = tmpStr2[:len(tmpStr2)-1]

    return str1 + str2[len(tmpStr2):len(str2)]
