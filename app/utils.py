class A(dict):
    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            return A()

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return self.__dict__.has_key(k)

    def pop(self, k, d=None):
        return self.__dict__.pop(k, d)

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)