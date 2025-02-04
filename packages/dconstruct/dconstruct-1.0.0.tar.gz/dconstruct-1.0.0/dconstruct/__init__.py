def construct(type_map, spec, **default_kwargs):
    """
    Construct an object from a dictionary specification.
    The specification must have a "type" key that maps to a type in the type_map.

    :param type_map: A dictionary mapping type names to types.
    :param spec: A dictionary specification of the object.
    :param default_kwargs: Default keyword arguments to pass to the constructor. These can be overridden by the spec.

    :return: An object of the type specified in the specification.
    """
    spec = dict(spec.items())
    if "type" not in spec:
        raise ValueError("Specification must have a 'type' key.")
    type_name = spec.pop("type")
    if type_name not in type_map:
        raise ValueError(
            f"Unknown type '{type_name}'. Must be one of {sorted(type_map.keys())}."
        )
    default_kwargs.update(spec)
    return type_map[type_name](**default_kwargs)
