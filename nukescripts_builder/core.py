# Import third-party modules
from nukescripts_builder.nuke_template import NukeTemplate


def build_nukescripts(template, data, output_path):
    """Start build nuke scripts.

    Args:
        template (str): The absolute path of a template file or real body
            string of template.
        output_path (str): Absolute path of the file.
        data (dict): The data can used render in template.

    Returns:
        str: Absolute path of the file.

    Examples:
        >>> build_nukescripts('c:/your/template.txt', {'key': 'value'},
        ...               'c:/output.nk')

    """
    nuke_template = NukeTemplate(source=template, data=data)
    with open(output_path, 'w') as file_obj:
        file_obj.write(str(nuke_template))
    return output_path
