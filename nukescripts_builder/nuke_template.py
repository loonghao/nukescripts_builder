# Import built-in modules
import os

# Import third-party modules
from Cheetah.Template import Template


class NukeTemplate(Template):
    def __init__(self, source, data):
        if os.path.isfile(source):
            source = self.getFileContents(source)
        super(NukeTemplate, self).__init__(source=source, namespaces=data)
