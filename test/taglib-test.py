# encoding:	utf-8
# ----------------------------------------------------
# SCRIPT: 	taglib-test
# ----------------------------------------------------
# (C) Vassil Kateliev, 2021  
# (C) http://www.kateliev.com
# (C) https://github.com/kateliev
# ----------------------------------------------------

# No warranties. By using this you agree
# that you use it at your own risk!

import os, random
from taglib import svg_builder

# - Init
rand_int = lambda: random.randint(0,255)
work_path = os.getcwd()
svg_filename = 'svg-test-{count}.svg'
html_filename = 'svg-gallery.html'

# - Build SVGs
new_svg = svg_builder()

for f in range(10):
	inner_svg = new_svg.svg(version="1.1", xmlns="http://www.w3.org/2000/svg", x="0px", y="0px", width="255px", height="255px", viewBox="0 0 255 255", __r='xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve"')

	group = inner_svg.g(id="Some Circular items")
	for x in range(5):
		group.circle(cx=rand_int(), cy=rand_int(), r=int(rand_int()/(x+1)), fill='#%02X%02X%02X' %(rand_int(), rand_int(), rand_int()))

	group = inner_svg.g(id="Some rectangular items")
	for x in range(5):
		group.rect(x=rand_int(), y=rand_int(), width=int(rand_int()/(x+1)), height=int(rand_int()/(x+1)), fill='#%02X%02X%02X' %(rand_int(), rand_int(), rand_int()))

	new_svg.dump(os.path.join(work_path, 'svg' ,svg_filename.format(count=f)))
	new_svg.reset()