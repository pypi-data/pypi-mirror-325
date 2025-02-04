"""PAF Address"""

from .lineable import LineableMixin

class Address(LineableMixin):
    """Main PAF Address class"""

    def __init__(self, args):
        """Initialise Address elements"""
        for key in self.__class__.attrs:
            setattr(self, key, '')
        for key, val in args.items():
            if hasattr(self, key):
                setattr(self, key, val)
        self.extend_premises()

    def __repr__(self):
        """Return full representation of an Address"""
        args = {k: getattr(self, k) for k in self.__class__.attrs if getattr(self, k, None)}
        return self.__class__.__name__ + '(' + str(args) + ')'

    def __str__(self):
        """Return Address as string representation"""
        line = ', '.join(self.lines)
        if self.is_empty('postcode'):
            return line
        return '. '.join([line] + [getattr(self, 'postcode')])

    def __iter__(self):
        """Return Address as iterable"""
        yield from self.lines.__iter__()
        if not self.is_empty('postcode'):
            yield from [getattr(self, 'postcode')].__iter__()

    def str(self):
        """Return Address as string"""
        return str(self)

    def list(self):
        """Return Address as list of strings"""
        return list(self)
