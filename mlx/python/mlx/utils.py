# Copyright © 2023 Apple Inc.
from collections import defaultdict


def tree_map(fn, tree, *rest, is_leaf=None):
    """Applies ``fn`` to the leaves of the Python tree ``tree`` and
    returns a new collection with the results.

    If ``rest`` is provided, every item is assumed to be a superset of ``tree``
    and the corresponding leaves are provided as extra positional arguments to
    ``fn``. In that respect, :meth:`tree_map` is closer to :func:`itertools.starmap`
    than to :func:`map`.

    The keyword argument ``is_leaf`` decides what constitutes a leaf from
    ``tree`` similar to :func:`tree_flatten`.

    .. code-block:: python

        import mlx.nn as nn
        from mlx.utils import tree_map

        model = nn.Linear(10, 10)
        print(model.parameters().keys())
        # dict_keys(['weight', 'bias'])

        # square the parameters
        model.update(tree_map(lambda x: x*x, model.parameters()))

    Args:
        fn (callable): The function that processes the leaves of the tree.
        tree (Any): The main Python tree that will be iterated upon.
        rest (tuple[Any]): Extra trees to be iterated together with ``tree``.
        is_leaf (callable, optional): An optional callable that returns ``True``
           if the passed object is considered a leaf or ``False`` otherwise.

    Returns:
        A Python tree with the new values returned by ``fn``.
    """
    if is_leaf is not None and is_leaf(tree):
        return fn(tree, *rest)
    elif isinstance(tree, (list, tuple)):
        TreeType = type(tree)
        return TreeType(
            tree_map(fn, child, *(r[i] for r in rest), is_leaf=is_leaf)
            for i, child in enumerate(tree)
        )
    elif isinstance(tree, dict):
        return {
            k: tree_map(fn, child, *(r[k] for r in rest), is_leaf=is_leaf)
            for k, child in tree.items()
        }
    else:
        return fn(tree, *rest)


def tree_map_with_path(fn, tree, *rest, is_leaf=None, path=None):
    """Applies ``fn`` to the path and leaves of the Python tree ``tree`` and
    returns a new collection with the results.

    This function is the same :func:`tree_map` but the ``fn`` takes the path as
    the first argument followed by the remaining tree nodes.

    Args:
        fn (callable): The function that processes the leaves of the tree.
        tree (Any): The main Python tree that will be iterated upon.
        rest (tuple[Any]): Extra trees to be iterated together with ``tree``.
        is_leaf (callable, optional): An optional callable that returns ``True``
           if the passed object is considered a leaf or ``False`` otherwise.

    Returns:
        A Python tree with the new values returned by ``fn``.

    Example:
        >>> from mlx.utils import tree_map_with_path
        >>> tree = {"model": [{"w": 0, "b": 1}, {"w": 0, "b": 1}]}
        >>> new_tree = tree_map_with_path(lambda path, _: print(path), tree)
        model.0.w
        model.0.b
        model.1.w
        model.1.b
    """
    if is_leaf is not None and is_leaf(tree):
        return fn(path, tree, *rest)
    elif isinstance(tree, (list, tuple)):
        prefix = f"{path}." if path else ""
        TreeType = type(tree)
        return TreeType(
            tree_map_with_path(
                fn, child, *(r[i] for r in rest), is_leaf=is_leaf, path=f"{prefix}{i}"
            )
            for i, child in enumerate(tree)
        )
    elif isinstance(tree, dict):
        prefix = f"{path}." if path else ""
        return {
            k: tree_map_with_path(
                fn, child, *(r[k] for r in rest), is_leaf=is_leaf, path=f"{prefix}{k}"
            )
            for k, child in tree.items()
        }
    else:
        return fn(path, tree, *rest)


def tree_flatten(tree, prefix="", is_leaf=None):
    """Flattens a Python tree to a list of key, value tuples.

    The keys are using the dot notation to define trees of arbitrary depth and
    complexity.

    .. code-block:: python

        from mlx.utils import tree_flatten

        print(tree_flatten([[[0]]]))
        # [("0.0.0", 0)]

        print(tree_flatten([[[0]]], ".hello"))
        # [("hello.0.0.0", 0)]

    .. note::
       Dictionaries should have keys that are valid Python identifiers.

    Args:
        tree (Any): The Python tree to be flattened.
        prefix (str): A prefix to use for the keys. The first character is
            always discarded.
        is_leaf (callable): An optional callable that returns True if the
            passed object is considered a leaf or False otherwise.

    Returns:
        List[Tuple[str, Any]]: The flat representation of the Python tree.
    """
    flat_tree = []

    if is_leaf is None or not is_leaf(tree):
        if isinstance(tree, (list, tuple)):
            for i, t in enumerate(tree):
                flat_tree.extend(tree_flatten(t, f"{prefix}.{i}", is_leaf))
            return flat_tree
        if isinstance(tree, dict):
            for k, t in tree.items():
                flat_tree.extend(tree_flatten(t, f"{prefix}.{k}", is_leaf))
            return flat_tree

    return [(prefix[1:], tree)]


def tree_unflatten(tree):
    """Recreate a Python tree from its flat representation.

    .. code-block:: python

        from mlx.utils import tree_unflatten

        d = tree_unflatten([("hello.world", 42)])
        print(d)
        # {"hello": {"world": 42}}

    Args:
        tree (list[tuple[str, Any]]): The flat representation of a Python tree.
           For instance as returned by :meth:`tree_flatten`.

    Returns:
        A Python tree.
    """
    if len(tree) == 1 and tree[0][0] == "":
        return tree[0][1]

    try:
        int(tree[0][0].split(".", maxsplit=1)[0])
        is_list = True
    except ValueError:
        is_list = False

    # collect children
    children = defaultdict(list)
    for key, value in tree:
        current_idx, *next_idx = key.split(".", maxsplit=1)
        next_idx = "" if not next_idx else next_idx[0]
        children[current_idx].append((next_idx, value))

    # recursively map them to the original container
    if is_list:
        keys = sorted((int(idx), idx) for idx in children.keys())
        l = []
        for i, k in keys:
            # if i <= len(l), no {} will be appended.
            l.extend([{} for _ in range(i - len(l))])
            l.append(tree_unflatten(children[k]))
        return l
    else:
        return {k: tree_unflatten(v) for k, v in children.items()}


def tree_reduce(fn, tree, initializer=None, is_leaf=None):
    """Applies a reduction to the leaves of a Python tree.

    This function reduces Python trees into an accumulated result by applying
    the provided function ``fn`` to the leaves of the tree.

    Example:
        >>> from mlx.utils import tree_reduce
        >>> tree = {"a": [1, 2, 3], "b": [4, 5]}
        >>> tree_reduce(lambda acc, x: acc + x, tree, 0)
        15

    Args:
        fn (callable): The reducer function that takes two arguments (accumulator,
            current value) and returns the updated accumulator.
        tree (Any): The Python tree to reduce. It can be any nested combination of
            lists, tuples, or dictionaries.
        initializer (Any, optional): The initial value to start the reduction. If
            not provided, the first leaf value is used.
        is_leaf (callable, optional): A function to determine if an object is a
            leaf, returning ``True`` for leaf nodes and ``False`` otherwise.

    Returns:
        Any: The accumulated value.
    """
    if is_leaf is not None and is_leaf(tree):
        return tree if initializer is None else fn(initializer, tree)

    accumulator = initializer

    if isinstance(tree, (list, tuple)):
        for item in tree:
            accumulator = tree_reduce(fn, item, accumulator, is_leaf)
    elif isinstance(tree, dict):
        for item in tree.values():
            accumulator = tree_reduce(fn, item, accumulator, is_leaf)
    else:
        return tree if accumulator is None else fn(accumulator, tree)

    return accumulator
