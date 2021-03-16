# TagLib
A simple and tiny markup document generator library.

## Introduction
**TagLib** can turn any tag based markup language into dynamic python object that could be used for building simple documents. It is not bound to any specific language - you could use it for HTML, SVG, XML or anything that could be parsed later. Where it really shines is helping you create documents that have many repetitive elements - just imagine a huge HTML table containing any data or gallery made of numerous divs. I've created this simple tool to help me build HTML based typeface specimens and proof-sheets. Also I use it as a simple SVG writer for exporting glyph outlines, but you could use it for anything...

## How to use
**TagLib** is currently semi-well documented, but only inside the code, so please take a look there. Also take your time to check the examples included in `/test` folder. With 170 lines of text this help is way longer then the library code itself :)

### An HTML example
Consider the following simple code...
```
from taglib import html_builder

new_document = html_builder()
new_document.body().div().p('Hello TagLib', style="text-align:center")

print(new_document.dumps())
```
...that returns the following string...
```
<body>
<div>    
    <p style="text-align:center">
        Hello TagLib
    </p>
</div>
</body>
```
Where any taglib **builder object** upon calling `.dumps()` will return the markup document as string. 

Nested tags could utilize dot syntax and tag attributes are given as keyword arguments. In cases where an attribute name is not allowed in Python syntax, such as `class="my_class"`, where `class` is a reserved word or attributes containing hyphens or column `xml:space="preserve"` there are special keyword arguments for injecting plain text as attributes: `__raw__` , `__r` , `__string__` or `__s`.

A little bit more complex example ...
```
import random
from taglib import html_builder

my_menus = ['alpha', 'betha', 'gamma']
new_document = html_builder()

new_document.head().link(rel="stylesheet", href="mystyle.css")
my_body = new_document.body()

for menu in my_menus:
    new_menu = my_body.div('', __r = 'class="dropdown"')
    new_menu.span().strong(menu)
    new_menu = new_menu.div('', __r = 'class="dropdown-content"')
    
    for menu_item in range(random.randint(1,5)):
        new_menu.p('Menu-Item-0%s' %menu_item)

new_document.dump('my_test_doc.html')
```
...will create a file called `my_test_doc.html` containing...

```
<!DOCTYPE html>
<!-- Generator: TagLib ver.1.2 (https://github.com/kateliev/taglib) -->

<head>
<link rel="stylesheet" href="mystyle.css"/>
</head>
<body>
<div class="dropdown">    
    <span>        
        <strong> alpha </strong>
    </span>
    <div class="dropdown-content">        
        <p> Menu-Item-00 </p>
        
         .......
        
        <p> Menu-Item-02 </p>
    </div>
</div>

  .......

<div class="dropdown">    
    <span>        
        <strong> gamma </strong>
    </span>
    <div class="dropdown-content">        
        <p> Menu-Item-00 </p>

        .......

        <p> Menu-Item-04 </p>
    </div>
</div>
</body>
```
Where any taglib **builder object** upon calling `.dump(path_to_file)` will write the markup document as file.

### An SVG example 
The following code...

```
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
```
... will generate 10 SVG files filled with random rectangular and circular elements, each containing something similar to ....
```
<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: TagLib ver.1.2 (https://github.com/kateliev/taglib) -->
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="255px" height="255px" viewBox="0 0 255 255" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve">
<g id="Some Circular items">
    <circle cx="155" cy="148" r="141" fill="#845E83" />
     ......
    <circle cx="62" cy="4" r="5" fill="#AA8C7E" />
</g>
<g id="Some rectangular items">
    <rect x="15" y="27" width="167" height="202" fill="#66D559" />
     ......
    <rect x="7" y="67" width="37" height="48" fill="#60A3F4" />
</g>
</svg>
```

### Making your own
You could create your own builder for any tag based markup language...
```
from taglib.objects import abstract_builder, markup_config

class my_builder(abstract_builder):
    def __init__(self):
        my_lingo = markup_config()
        my_lingo.tags = ['foo', 'bar', 'baz']
        super(my_builder, self).__init__(my_lingo)

my_document = my_builder()
my_document.foo().bar(style="wroom").baz('Hello TagLib!', style="zoom")

print(my_document.dumps())
```
...will produce...
```
<foo>
<bar style="wroom">    
    <baz style="zoom">
        Hello TagLib
    </baz>
</bar>
</foo>
```

