#!/usr/bin/env python

import click
import fabric


def deploy(c):
    with c.cd("/var/www/theraphael0000.ch/blog.theraphael0000.ch"):
        c.run("git status")
        if not click.confirm("Stash and deploy to main ?", default=True):
            exit()
        c.run("git stash")
        c.run("git checkout master")
        c.run("git pull")
        c.run("hugo")


c = fabric.Connection(host="theraphael0000.ch", user="root", port=22)
deploy(c)