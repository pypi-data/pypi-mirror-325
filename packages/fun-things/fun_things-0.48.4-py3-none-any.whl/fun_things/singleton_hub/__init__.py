from abc import ABC, abstractmethod
from typing import Dict, Generic, TypeVar, final

T = TypeVar("T")


class SingletonHubMeta(ABC, type, Generic[T]):
    __key_cache: Dict[str, str] = {}
    __value_cache: Dict[str, T] = {}

    def _name_selector(cls, name: str):
        return name

    @abstractmethod
    def _value_selector(cls, name: str) -> T:
        pass

    def _on_clear(cls, key: str, value: T) -> None:
        pass

    @final
    def clear(cls, name: str):
        if name not in cls.__key_cache:
            return None, None

        key = cls.__key_cache[name]

        if key not in cls.__value_cache:
            return key, None

        value = cls.__value_cache[key]

        cls._on_clear(key, value)

        del cls.__value_cache[key]

        return key, value

    @final
    def clear_all(cls):
        result: Dict[str, T] = {}

        for key, value in cls.__value_cache.items():
            result[key] = value

            cls._on_clear(key, value)

        cls.__value_cache.clear()

        return result

    @final
    def get(
        cls,
        name: str = "",
    ):
        if name in cls.__key_cache:
            key = cls.__key_cache[name]
        else:
            key = cls.__key_cache[name] = cls._name_selector(name)

        if key in cls.__value_cache:
            return cls.__value_cache[key]

        value = cls.__value_cache[key] = cls._value_selector(key)

        return value

    def __getattr__(cls, name: str):
        return cls.get(name)
