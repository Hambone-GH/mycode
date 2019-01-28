#!/usr/bin/env python3
#this renames things foo
import shutil
import os

os.chdir('/home/student/mycode/')
shutil.move('raynor.obj', 'ceph_storage/')

xname = input('What new name you want for kerrigan.obj, foo?')

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

