import re

from typing import Any, Generator, Self

class Dictoria(dict):
    """
    A dictionary extension that supports regex-based key search.

    This class extends the built-in `dict` type and allows recursive searching of nested dictionaries 
    using regex patterns. The input to the class must be a dictionary.

    Args:
        \\*args: Arguments passed to the base dictionary.
        \\*\\*kwargs: Keyword arguments passed to the base dictionary.

    Note:
        - When initializing this class, you must provide a dictionary as input.
        - Paths in the dictionary are represented in the format `/root/key/subkey` for nested structures.

    Example:
        >>> data = Dictoria({
        ...     "users": {
        ...         "user1": {"name": "Alice", "age": 25},
        ...         "user2": {"name": "Bob", "age": 30}
        ...     }
        ... })
        >>> name: str = data.get(r"/users/.+/name", target=r"A.+")
        >>> print(name)
        Alice
    """

    def __getitem__(self: Self, path: str) -> Generator[Any, None, None]:
        """
        Retrieves values matching the specified regular expression.

        Args:
            path (str): A regex pattern for searching keys.

        Yields:
            Generator[Any, None, None]: Values whose paths match the provided regex pattern.
        """
        for k, v in Dictoria.__generate_paths(dict(self)):
            m: re.Match | None = re.fullmatch(path, k)
            if m:
                yield v

    @staticmethod
    def __generate_paths(d: dict, parent_key: str = "/") -> Generator[tuple[str, Any], None, None]:
        """
        Recursively generates paths for all keys in the dictionary, including nested dictionaries.

        Args:
            d (dict): The source dictionary for path generation.
            parent_key (str): The prefix for the current nesting level. Defaults to '/'.

        Yields:
            Generator[tuple[str, Any], None, None]: Tuples `(path, value)` where `path` is the full key path and `value` is the corresponding value.
        """
        for k in d:
            if isinstance(d[k], dict):
                for i in Dictoria.__generate_paths(d[k], parent_key + str(k) + "/"):
                    yield i
            yield (parent_key + str(k), d[k])

    def get(
        self: Self,
        path: str,
        typeof: type | None = None,
        target: str | None = None,
        default: Any = None
    ) -> Any:
        """
        Retrieves a value based on the specified regex pattern with optional filtering.

        Args:
            path (str): A regex pattern for searching keys. The path format follows the structure `/root/key/subkey` for nested dictionaries.
            typeof (type, optional): Filters results by the specified type. Defaults to None.
            target (str, optional): A regex pattern for matching the value itself. Defaults to None.
            default (Any, optional): Default value to return if no matches are found. Defaults to None.

        Returns:
            Any: The first value that satisfies all conditions or the `default` value if no matches are found.

        Note:
            - The `path` parameter uses regex patterns to match dictionary keys.
            - Paths are structured as `/root/key/subkey` for nested dictionaries.
            - If no matches are found and `default` is not specified, the method will return `None`.

        Examples:
            >>> from dictoria import Dictoria
            >>> data = Dictoria({
            ...     "users": {
            ...         "user1": {"name": "Alice", "age": 25},
            ...         "user2": {"name": "Bob", "age": 30}
            ...     },
            ...     "settings": {
            ...         "timeout": 60,
            ...         "debug": False
            ...     }
            ... })

            # Example 1: Retrieve a specific age using regex
                >>> age: int = data.get(r"/users/.+/age", typeof=int)
                >>> print(age)
                25

            # Example 2: Retrieve a name matching a regex pattern
                >>> name: str = data.get(r"/users/.+/name", target=r"Alice")
                >>> print(name)
                Alice

            # Example 3: Handle non-existent keys with a default value
                >>> result: str = data.get(r"/nonexistent", default="Not found")
                >>> print(result)
                Not found

            # Example 4: Combine type filtering and value matching
                >>> value: int = data.get(r"/settings/.+", typeof=int, target=r".+0")
                >>> print(value)
                60
        """
        for v in self[path]:
            ok: bool = True
            if typeof:
                ok = ok and bool(type(v) == typeof)
            if target:
                ok = ok and bool(re.fullmatch(target, str(v)))
            if ok:
                return v
        return default
