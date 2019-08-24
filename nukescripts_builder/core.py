# Import built-in modules
import os

# Import third-party modules
from quik import FileLoader
from quik import Template


def build(template, data, output_path):
    """Start build nuke template.

    Args:
        template (str): The absolute path of a template file or real body
            string of template.
        data (dict): The data can used render in template.
        output_path (str): Absolute path of the file.

    Returns:
        str: Absolute path of the file.

    Examples:
        >>> build('c:/your/template.txt', {'key': 'value'}, 'c:/output.nk')

    """
    if os.path.isfile(template):
        root, file_name = os.path.split(template)
        loader = FileLoader(root)
        template_ = loader.load_template(file_name)
    else:
        template_ = load_template(template)
    with open(output_path, 'w') as dst_file:
        dst_strings = template_.render(data)
        dst_file.write(dst_strings)
    return output_path


def load_template(body_strings):
    template_ = Template(body_strings)
    template_.ensure_compiled()
    return template_
