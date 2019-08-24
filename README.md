# nukescripts_builder
[![build Status](https://travis-ci.com/loonghao/nukescripts_builder.svg?branch=master)](https://travis-ci.com/loonghao/nukescripts_builder)

Build a Nuke scripts from a template.

Features
--------
- No need for Nuke license.
- Easy to use.
- High performance.
- Autoescaping.
- Template inheritance.
- Supports native python expressions.

install
-------
Clone from github.
```cmd
git clone https://github.com/loonghao/nukescripts_builder.git
```
Install package.
```cmd
python setup.py install
```

Why?
====
It's not easy to build complex `nukescripts` or `nuke gizmo` using the Nuke API.

You need to understand `Nuke` and need to understand the `Nuke` Python API.

```python
import nuke
read = nuke.createNode('Read')
read.knob('file').setValue('c:/test.exr')
colorspace = nuke.createNode('OCIOColorSpace')
read = nuke.createNode('Write')
read.knob('file').setValue('c:/test.jpg')
nuke.scriptSave('c:/my_nukescripts.nk')
```

You just need to understand `Nuke` and know a little bit of Python.

```python
from nukescripts_builder.core import build

source_string ="""
Read {
 file @file_path
 origset true
 name Read
 selected true
 xpos 54
 ypos -162
}
OCIOColorSpace {
 in_colorspace linear
 out_colorspace linear
 name OCIOColorSpace
 selected true
 xpos 54
 ypos -47
}
Write {
 file @output
 name Write
 selected true
 xpos 54
 ypos -6
 }
"""
build(source_string,
      {'file_path': 'c:/test.exr',
       'output': 'c:/test.jpg'}, 'c:/my_nukescripts.nk')
```

Basic syntax of the template
----------------------------
Based on third party package [Quik](https://github.com/avelino/quik/blob/master/README.rst)
