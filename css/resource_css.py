# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.14.1)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x01\x43\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xff\x61\
\x00\x00\x01\x0a\x49\x44\x41\x54\x38\x8d\xad\x53\xcb\xb1\x83\x30\
\x0c\xd4\x81\x75\x0d\xcc\xc4\xd6\x50\x42\x3a\x78\x74\x02\x1d\xe1\
\xce\xe0\x26\x91\x1c\x42\x07\xd0\x81\xdf\x21\x10\x13\x63\xde\x67\
\x26\x9a\xf1\xc9\x96\x76\x57\xde\x25\x4a\x4a\x4a\xaa\xd4\xa1\x53\
\x46\xaf\x6c\xc2\xf3\xa0\x57\x87\x4e\x4a\xaa\xd2\xf7\x6f\xa5\x16\
\x5e\xd9\x04\x75\x18\xd4\xc2\x8b\x43\x2b\x0e\xad\x5a\x78\x75\x18\
\xd6\xbb\x2e\xdf\xec\x30\x28\x63\x11\x87\xf6\x0c\x40\x1c\x5a\x65\
\x2c\xca\xe8\x33\xc8\x58\x6e\x17\x5c\x7f\xa4\x48\x44\xb7\x0b\xae\
\xca\x58\xd4\xc2\x47\xcd\x6c\x42\x0e\x59\x6c\x51\xdf\x6d\xf1\x95\
\x67\x62\x82\x94\x54\xd1\xa6\xef\x88\x62\x1e\x71\x89\xe6\x91\xb2\
\x13\x36\x93\x5a\x78\xda\x16\x76\xb8\x8c\xcd\xaf\x21\x19\xd9\x3d\
\xa5\xf4\xc5\x16\x75\xa6\x39\x28\x9b\x20\xb6\xa8\x53\x19\x1f\x18\
\xf0\x47\x09\xc2\x66\x3a\x48\x70\x18\xa2\x96\x64\x89\xfb\x21\xc2\
\x66\x3a\x5d\xe2\x6f\xdf\xb8\xa7\x9d\xd2\x7f\x59\x7b\x65\x31\xff\
\xc3\x48\x73\x2a\x7b\xb3\xf2\x3c\x32\x9a\xb3\xe6\xd5\xca\x73\xea\
\x9b\x38\x64\x0b\xd3\x9a\xbe\x91\xd1\x8c\x8c\xe6\x99\xce\xd5\x58\
\x29\xf2\x01\xa5\xa4\xea\x2d\x7d\xfb\x74\x66\xe2\xfc\x0d\x01\xf7\
\xe7\x51\xe7\xe8\xed\xdc\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\
\x60\x82\
"

qt_resource_name = b"\
\x00\x03\
\x00\x00\x6a\xa3\
\x00\x63\
\x00\x73\x00\x73\
\x00\x04\
\x00\x06\xfa\x5e\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\
\x00\x0b\
\x01\x64\x80\x07\
\x00\x63\
\x00\x68\x00\x65\x00\x63\x00\x6b\x00\x65\x00\x64\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x0c\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x1a\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x0c\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x1a\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x71\xb4\x7f\x09\x36\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
