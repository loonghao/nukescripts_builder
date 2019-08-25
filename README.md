# nukescripts_builder
[![build_nukescripts Status](https://travis-ci.com/loonghao/nukescripts_builder.svg?branch=master)](https://travis-ci.com/loonghao/nukescripts_builder)

Build a Nuke scripts from a template.

Features
--------
- Save Nuke license.
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
It's not easy to build_nukescripts complex `nukescripts` or `nuke gizmo` using the Nuke API.

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
from nukescripts_builder.core import build_nukescripts

source_string ="""
Read {
 inputs 0
 ## If the variable does not exist, ignore it directly
 #if $getVar('file_type', ''):
 file_type $file_type
 #end if
 file $read_file
 origset true
 name Read1
 selected true
 xpos 54
 ypos -162
}
OCIOColorSpace {
 in_colorspace linear
 out_colorspace linear
 name OCIOColorSpace1
 selected true
 xpos 54
 ypos -47
}
Write {
 file $write_file
 name Write1
 selected true
 xpos 54
 ypos -6
 }
"""
file_path = 'c:/test.exr'
write_file = 'c:/test.jpg'
output_path = 'c:/my_nukescripts.nk'
data = {
    'read_file': file_path,
    'write_file': write_file
}
build_nukescripts(template=source_string, output_path=output_path,
                  data=data)
```

Basic syntax of the template
----------------------------
Based on third party package [Cheetah](https://cheetahtemplate.org/users_guide/language.html)
