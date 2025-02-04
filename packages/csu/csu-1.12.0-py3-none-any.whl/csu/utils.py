import sys
from collections.abc import Callable
from decimal import Decimal
from importlib import import_module
from inspect import Parameter
from inspect import signature
from typing import TypeVar

ZERO = Decimal(0)
DOT01 = Decimal("0.01")
DOT001 = Decimal("0.001")
DOT0001 = Decimal("0.0001")
ONE00 = Decimal("100.0")


def validate_no_required_arguments(func):
    if isinstance(func, staticmethod):
        func = func.__func__
    required = [param for param in signature(func).parameters.values() if param.default is Parameter.empty]
    if required:
        raise TypeError(f"{func} cannot have mandatory arguments: {required}")


_T = TypeVar("_T")


def singleton_memoize(func: Callable[[], _T]) -> _T:
    validate_no_required_arguments(func)

    unset = object()

    class Singleton:
        value = unset

        def __get__(self, instance, owner):
            return self

        def __call__(self):
            if self.value is unset:
                value = self.value = func()
            else:
                value = self.value
            return value

    return Singleton()


def singleton_property(func: Callable[[], _T]) -> _T:
    if isinstance(func, staticmethod):
        func = func.__func__
    validate_no_required_arguments(func)

    unset = object()

    class Singleton:
        value = unset

        def __get__(self, instance, owner):
            if self.value is unset:
                value = self.value = func()
            else:
                value = self.value
            return value

    return Singleton()


def cached_import(module_path, class_name, package):
    # Check whether module is loaded and fully initialized.
    if not (
        (module := sys.modules.get(module_path))
        and (spec := getattr(module, "__spec__", None))
        and getattr(spec, "_initializing", False) is False
    ):
        module = import_module(module_path, package)
    return getattr(module, class_name)


def import_string(dotted_path, current_module=None):
    """
    Variant of `django.utils.module_loading.import_string` that allows relative imports (if `package` is specified).
    """
    try:
        module_path, class_name = dotted_path.rsplit(".", 1)
    except ValueError as err:
        raise ImportError(f"{dotted_path!r} doesn't look like a module path.") from err

    if current_module:
        try:
            package, _ = current_module.rsplit(".", 1)
        except ValueError as err:
            raise ImportError(
                f"{current_module!r} doesn't look like a module name. Using `__name__` in an __init__.py file is not supported."
            ) from err
    else:
        package = None
    try:
        return cached_import(module_path, class_name, package)
    except AttributeError as err:
        raise ImportError(f"Module {module_path}!r does not define a {class_name!r} attribute/class.") from err


class lazy_import_classproperty:
    """
    A variant of django.utils.functional.classproperty that just imports something.
    """

    def __init__(self, dotted_path, current_module=None):
        self.dotted_path = dotted_path
        self.current_module = current_module
        self.prop_name = None

    def __set_name__(self, owner, name):
        if self.prop_name is None:
            self.prop_name = name
        elif name != self.prop_name:
            raise TypeError(f"Cannot assign the same cached_property to two different names ({self.prop_name!r} and {name!r}).")

    def __get__(self, instance, cls=None):
        if self.prop_name is None:
            raise TypeError("Cannot use lazy_import_classproperty instance without calling __set_name__ on it.")
        value = import_string(self.dotted_path, self.current_module)
        setattr(cls, self.prop_name, value)
        return value
