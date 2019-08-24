# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""

# Import built-in modules
import os

# Import local modules
from nukescripts_builder.core import build


def test_build_nukescripts(tmpdir):
    source_string = """Read {
 inputs 0
 file_type jpeg
 file @file_path
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
 file @output
 name Write1
 selected true
 xpos 54
 ypos -6
 }
"""
    file_path = 'Y:/113803nya2022gg2pe65ka.jpg'
    output_path = str(tmpdir.join('test.nk'))
    build(source_string,
          {'file_path': file_path,
           'output': 'c:/test.exr'},
          output_path)
    assert os.path.isfile(output_path)
    with open(output_path, 'r') as file_obj:
        assert 'file {}'.format(file_path) in file_obj.read()
