#!/usr/bin/env python3
import os
import sys
import subprocess

def workdir_cleaning():
    basedir = '/data/vre-storage'
    projects = os.listdir(basedir)
    print(projects)
    if not projects:
        exit()
    for project in projects:
        dir = '/'.join([basedir, project, 'workdir/'])
        print("cleaning " + dir)
        args = ["find", dir, "-mtime", "+1", "-type", "f", "-exec", "rm", "-f", "{}", ";"]
        subprocess.call(args)
        print("cleaning " + dir + " Done")


workdir_cleaning()

