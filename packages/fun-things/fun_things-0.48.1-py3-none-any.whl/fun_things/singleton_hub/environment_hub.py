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
        Select the environment variable name based on the given name.

        This function supports two kinds of formats.
        The first one is a simple string, which is used as the name of
            the environment variable.
        The second one is a format string, which is used to generate
            the name of the environment variable by replacing the
            placeholder "{name}" with the given name.

        The function will check all the formats in the order they are
            given, and return the first name that exists in the
            environment variables.

        If no environment variable is found, the function will return
            the given name in upper case.

        :param name: The given name.
        :return: The selected environment variable name.
        """
        empty = name == ""

        for format in cls._formats:
            dynamic = any(
                True
                for _, name, _, _ in string.Formatter().parse(format)
                if name == "name"
            )

            if dynamic == empty:
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
