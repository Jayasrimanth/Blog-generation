class PromptTemplate:
    """
    Simple class to manage prompt templates.
    """
    def __init__(self, template):
        self.template = template

    def format(self, **kwargs):
        return self.template.format(**kwargs)
