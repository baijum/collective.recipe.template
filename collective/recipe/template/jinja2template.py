import zc.buildout
from collective.recipe.template import Recipe as Base


class Recipe(Base):
    def _execute(self):
        from jinja2 import Template
        from jinja2.exceptions import UndefinedError

        template = Template(self.source)
        try:
            self.result = template.render(parts=self.buildout, options=self.options)
        except UndefinedError, e:
            raise zc.buildout.UserError("Error in template %s:\n%s" % (self.input, e.msg))
