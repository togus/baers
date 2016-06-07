# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join, getctime

import glob

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(searchpath="html/" ))
template = env.get_template("index.html")

allimages = [f for f in listdir("images/") if isfile(join("images/", f))]
newest = max(glob.iglob('images/*.*'), key=getctime)

#print allimages
#print newest
allimages.remove(newest.rsplit('/', 1)[-1])
print template.render(latest=newest, files=allimages)
