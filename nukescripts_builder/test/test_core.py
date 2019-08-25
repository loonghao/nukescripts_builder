# -*- coding: utf-8 -*-
"""
module author: Long Hao <hoolongvfx@gmail.com>
"""

# Import built-in modules
import os

# Import local modules
from nukescripts_builder.core import build_nukescripts


def test_build_nukescripts(tmpdir):
    source_string = """
Read {
 inputs 0
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
    file_path = 'Y:/113803nya2022gg2pe65ka.jpg'
    write_file = 'c:/test.exr'
    output_path = str(tmpdir.join('test.nk'))
    build_nukescripts(template=source_string, output_path=output_path, data={
        'read_file': file_path,
        'write_file': write_file
    })
    assert os.path.isfile(output_path)
    with open(output_path, 'r') as file_obj:
        assert 'file {}'.format(file_path) in file_obj.read()
        assert 'file_type' not in file_obj.read()
