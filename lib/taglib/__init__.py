# encoding:	utf-8
# ----------------------------------------------------
# MODULE: 	TagLib
# DESC:		A simple and tiny markup language library.
# ----------------------------------------------------
# (C) Vassil Kateliev, 2021  
# (C) http://www.kateliev.com
# (C) https://github.com/kateliev
# ----------------------------------------------------

# NOTE:		Module is kept Python 2 and 3 compatible!

# No warranties. By using this you agree
# that you use it at your own risk!

# - Dependencies -------------------------------------
from __future__ import absolute_import, print_function, unicode_literals
from taglib.objects import markup_config, abstract_builder

# - Init --------------------------------------------
__version__ = 1.2

# - Classes -------------------------------------------
# -- Language specific ---------------------------------
class html_builder(abstract_builder):
	'''A simple HTML builder'''
	def __init__(self):
		html_config = markup_config()
		html_config.tags = 'a,abbr,acronym,address,applet,area,article,aside,audio,b,base,basefont,bdi,bdo,big,blockquote,body,br,button,canvas,caption,center,cite,code,col,colgroup,data,datalist,dd,del,details,dfn,dialog,dir,div,dl,dt,em,embed,fieldset,figcaption,figure,font,footer,form,frame,frameset,h1,head,header,hr,html,i,iframe,img,input,ins,kbd,label,legend,li,link,main,map,mark,meta,meter,nav,noframes,noscript,object,ol,optgroup,option,output,p,param,picture,pre,progress,q,rp,rt,ruby,s,samp,script,section,select,small,source,span,strike,strong,style,sub,summary,sup,svg,table,tbody,td,template,textarea,tfoot,th,thead,time,title,tr,track,tt,u,ul,var,video,wbr'.split(',')
		html_config.template_start_end = '{fh}<{tag} {attrib}>{fch}{content}{ft}</{tag}>'
		html_config.template_empty = '{fh}<{tag} {attrib} />'
		html_config.document = '<!DOCTYPE html>\n<!-- Generator: TagLib ver.{} (https://github.com/kateliev/taglib) -->\n'.format(__version__)

		super(html_builder, self).__init__(html_config)

class svg_builder(abstract_builder):
	'''A simple SVG builder'''
	def __init__(self):
		html_config = markup_config()
		html_config.tags = 'a,animate,animateMotion,animateTransform,circle,clipPath,color-profile,defs,desc,discard,ellipse,feBlend,feColorMatrix,feComponentTransfer,feComposite,feConvolveMatrix,feDiffuseLighting,feDisplacementMap,feDistantLight,feDropShadow,feFlood,feFuncA,feFuncB,feFuncG,feFuncR,feGaussianBlur,feImage,feMerge,feMergeNode,feMorphology,feOffset,fePointLight,feSpecularLighting,feSpotLight,feTile,feTurbulence,filter,foreignObject,g,hatch,hatchpath,image,line,linearGradient,marker,mask,mesh,meshgradient,meshpatch,meshrow,metadata,mpath,path,pattern,polygon,polyline,radialGradient,rect,script,set,solidcolor,stop,style,svg,switch,symbol,text,textPath,title,tspan,unknown,use,view'.split(',')
		html_config.template_start_end = '{fh}<{tag} {attrib}>{fch}{content}{ft}</{tag}>'
		html_config.template_empty = '{fh}<{tag} {attrib} />'
		html_config.document = '<?xml version="1.0" encoding="utf-8"?>\n<!-- Generator: TagLib ver.{} (https://github.com/kateliev/taglib) -->\n'.format(__version__)

		super(svg_builder, self).__init__(html_config)

# - Test -----------------------------------------------
if __name__ == "__main__":
	
	import random
	rand_int = lambda: random.randint(0,255)

	new_svg = svg_builder()

	inner_svg = new_svg.svg(version="1.1", xmlns="http://www.w3.org/2000/svg", x="0px", y="0px", width="255px", height="255px", viewBox="0 0 255 255", __r='xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve"')

	group = inner_svg.g(id="Some Circular items")
	for x in range(5):
		group.circle(cx=rand_int(), cy=rand_int(), r=int(rand_int()/(x+1)), fill='#%02X%02X%02X' %(rand_int(), rand_int(), rand_int()))

	group = inner_svg.g(id="Some rectangular items")
	for x in range(5):
		group.rect(x=rand_int(), y=rand_int(), width=int(rand_int()/(x+1)), height=int(rand_int()/(x+1)), fill='#%02X%02X%02X' %(rand_int(), rand_int(), rand_int()))

	print(new_svg.dumps())

