
from openmdao.core.component import Component

class Problem(Component):
    def __init__(self, root=None, driver=None):
        self.root = root
        self.driver = driver

    def run(self):
        pass
