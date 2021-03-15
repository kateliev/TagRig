# TagLib
A simple and tiny markup document generator library.

## Introduction
**TagLib** can turn any tag based markup language into dynamic python object that could be used for building simple documents. It is not bound to any specific language - you could use it for HTML, SVG, XML or anything that could be parsed later. Where it really shines is helping you create documents that have many repetitive elements - just imagine a huge HTML table containing any data or gallery made of numerous divs. I've created this simple tool to help me build HTML based typeface specimens and proof-sheets. Also I use it as a simple SVG writer for exporting glyph outlines, but you could use it for anything...

## How to use
**TagLib** is currently semi-well documented, but only inside the code, so please take a look there. Also take your time to check the examples included in `/test` folder.

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

A little bit more complex example follows...
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
        <strong>
            alpha
        </strong>
    </span>
    <div class="dropdown-content">        
        <p>
            Menu-Item-00
        </p>
        <p>
            Menu-Item-01
        </p>
        <p>
            Menu-Item-02
        </p>
    </div>
</div>
<div class="dropdown">    
    <span>        
        <strong>
            betha
        </strong>
    </span>
    <div class="dropdown-content">        
        <p>
            Menu-Item-00
        </p>
        <p>
            Menu-Item-01
        </p>
    </div>
</div>
<div class="dropdown">    
    <span>        
        <strong>
            gamma
        </strong>
    </span>
    <div class="dropdown-content">        
        <p>
            Menu-Item-00
        </p>
        <p>
            Menu-Item-01
        </p>
        <p>
            Menu-Item-02
        </p>
        <p>
            Menu-Item-03
        </p>
        <p>
            Menu-Item-04
        </p>
    </div>
</div>
</body>
```
Where any taglib **builder object** upon calling `.dump(path_to_file)` will write the markup document as file.