from typing import TypeVar

T = TypeVar('T')


def singleton(original_class: T):
    original_class.instances = {}

    class SingletonClass:
        static = original_class

        def __new__(cls, *args, **kwargs):
            return cls._get_instance(*args, **kwargs)

        def _get_instance(*args, **kwargs) -> T:
            if original_class not in original_class.instances:
                original_class.instances[original_class] = original_class(*args, **kwargs)
            return original_class.instances[original_class]

    return SingletonClass
