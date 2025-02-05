import inspect
import re

from flask import g, has_request_context, url_for


def split_on_uppercase_char(string):
    return re.findall("[A-Z][^A-Z]*", str(string))


def cap_to_snake_case(string):
    return "_".join(split_on_uppercase_char(string)).lower()


endpoint_prefix_map = {"get": ["GET"], "post": ["POST"], "form": ["GET", "POST"]}


class Endpoint:
    def __init__(self, cls, func):
        # Store the original class and function
        self.cls = cls
        self.func = func

        self.method_prefix, self.endpoint_name = self.func.__name__.split("_", 1)

        self.http_methods = endpoint_prefix_map.get(self.method_prefix)

        url_prefix = "".join(
            f"/<{param}>"
            for param in list(inspect.signature(self.func).parameters.values())
        )
        if self.endpoint_name == "index":
            url_suffix = ""
        else:
            url_suffix = self.endpoint_name.replace("_", "-")
        self.url = f"{url_prefix}/{url_suffix}"

    def __call__(self, *args, **kwargs):
        # Make the instance callable and invoke the wrapped function
        return self.func.__func__(self.cls, *args, **kwargs)

    @property
    def client_name(self):
        return " ".join(word.capitalize() for word in self.endpoint_name.split("_"))

    def full_url(self, **kwargs):
        return url_for(f"{self.cls.namespace_name}.{self.endpoint_name}", **kwargs)


class ClassMethodsMeta(type):
    """Meta class for RouteNamespace.

    Some non pythonic modifications have been made to this class, so they're listed here:
        - All methods are classmethods by default
        - Methods with an HTTP method prefix (get, post, and form) are converted into Endpoint objects
        - Any attributes set on this meta class when there is a flask request context are silently
            added to the flask.g proxy object.  They are thus only available for that request context.
    """

    def __instancecheck__(self, instance):
        try:
            return self in instance.mro()
        except:
            return super().__instancecheck__(instance)

    def __new__(cls, name, bases, dct):
        for attr, value in dct.items():
            if callable(value) and not attr.startswith("__"):
                # Replace method with classmethod
                dct[attr] = classmethod(value)

        # Create the class with the modified dictionary
        new_class = super().__new__(cls, name, bases, dct)

        # Iterate over the class dictionary to find methods
        endpoints = []
        for attr in dir(new_class):
            value = getattr(new_class, attr)
            attr_prefix, *_ = attr.split("_", 1)

            if (
                not callable(value)
                or attr.startswith("__")
                or attr_prefix not in endpoint_prefix_map.keys()
            ):  # Exclude dunder methods
                continue

            if isinstance(value, Endpoint):
                endpoint = Endpoint(new_class, value.func)
            else:
                endpoint = Endpoint(new_class, value)

            # Add endpoint to list
            endpoints.append(endpoint)
            # Replace method with classmethod
            setattr(new_class, attr, endpoint)

        new_class._endpoints = endpoints

        return new_class

    def __setattr__(self, name, value):
        """
        If called when a flask request context context is available then the attribute is added to the flask.g proxy.
        Otherwise the super() method is called.
        """
        if not has_request_context():
            return super().__setattr__(name, value)
        setattr(g, name, value)

    def __getattribute__(self, name):
        """
        If called when a flask request context context is available then the attribute is searched for in flask.g first.
        If the attribute name is not found in flask.g then super() is called.  If no flask request context is available then super() is called.
        """
        try:
            if not has_request_context():
                raise AttributeError
            return getattr(g, name)
        except AttributeError:
            return super().__getattribute__(name)


class classproperty(property):
    def __get__(self, owner_self, owner_cls):
        return self.fget(owner_cls)


class NamespaceBase:
    class_definition_suffix = "Namespace"

    @classproperty
    def url_prefix(cls):
        class_name_prefix = cls.__name__.replace(cls.class_definition_suffix, "")
        return f"/{class_name_prefix}"

    @classproperty
    def namespace_name(cls):
        return cap_to_snake_case(cls.url_prefix.replace("/", ""))
