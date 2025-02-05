from abc import ABC
import os
import string
from typing import Iterable, TypeVar

from . import SingletonHubMeta

T = TypeVar("T")


class EnvironmentHubMeta(SingletonHubMeta[T], ABC):
    @staticmethod
    def _bake_basic_uri_formats(
        *keywords: str,
        formats: Iterable[str] = [
            "{keyword}",
            "{keyword}_URI",
            "{keyword}_URL",
            "{keyword}_CONNECTION_URI",
            "{keyword}_CONNECTION_URL",
            "{keyword}_CONNECTION_STRING",
            "{{name}}_{keyword}",
            "{{name}}_{keyword}_URI",
            "{{name}}_{keyword}_URL",
            "{{name}}_{keyword}_CONNECTION_URI",
            "{{name}}_{keyword}_CONNECTION_URL",
            "{{name}}_{keyword}_CONNECTION_STRING",
            "{keyword}_{{name}}",
            "{keyword}_URI_{{name}}",
            "{keyword}_URL_{{name}}",
            "{keyword}_CONNECTION_URI_{{name}}",
            "{keyword}_CONNECTION_URL_{{name}}",
            "{keyword}_CONNECTION_STRING_{{name}}",
        ],
    ):
        """
        Return a list of basic URI formats from given keywords.

        :param keywords: A collection of keywords used to generate
            the URI formats.
        :param formats: A collection of URI formats. The default formats
            are:
            "{keyword}",
            "{keyword}_URI",
            "{keyword}_URL",
            "{keyword}_CONNECTION_URI",
            "{keyword}_CONNECTION_URL",
            "{keyword}_CONNECTION_STRING",
            "{{name}}_{keyword}",
            "{{name}}_{keyword}_URI",
            "{{name}}_{keyword}_URL",
            "{{name}}_{keyword}_CONNECTION_URI",
            "{{name}}_{keyword}_CONNECTION_URL",
            "{{name}}_{keyword}_CONNECTION_STRING",
            "{keyword}_{{name}}",
            "{keyword}_URI_{{name}}",
            "{keyword}_URL_{{name}}",
            "{keyword}_CONNECTION_URI_{{name}}",
            "{keyword}_CONNECTION_URL_{{name}}",
            "{keyword}_CONNECTION_STRING_{{name}}".
        :return: A list of generated URI formats.
        """
        return [
            format.format(
                keyword=keyword,
            )
            for keyword in keywords
            for format in formats
        ]

    _formats: Iterable[str]

    def _name_selector(cls, name: str):
        """
        Selects the first environment variable name that matches the given name.

        If the given name is empty, it will search for the exact environment variable names
        without any substitutions. If the given name is not empty, it will search for the
        environment variable names with the given name as a replacement for the `{name}`
        placeholder in the format strings.

        The search is case-insensitive.

        The function will return the upper-case version of the environment variable name
        that is found.
        """
        empty = name == ""

        for format in cls._formats:
            dynamic = any(
                True
                for _, name, _, _ in string.Formatter().parse(format)
                if name == "name"
            )

            if not dynamic and not empty:
                continue

            if empty:
                if format in os.environ:
                    return format.upper()

                continue

            try:
                field_name = format.format(name=name).upper()

                if empty:
                    continue

                if field_name in os.environ:
                    return field_name

            except KeyError:
                continue

        return name.upper()
