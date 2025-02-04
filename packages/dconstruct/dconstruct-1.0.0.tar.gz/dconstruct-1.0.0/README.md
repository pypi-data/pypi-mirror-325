
# dconstruct

Extremely simple way to build objects from a dictionary specification, recursively.

Contains one main function, ```construct```, which takes a type dispatch dictionary and a dictionary to construct an object from, and returns the object.

## Basic Example

```python
from dconstruct import construct

def create_model(spec):
    return construct(
        dict(Conv1d=torch.nn.Conv1d, Linear=torch.nn.Linear),
        spec,
        device='cpu'
    )
```

This function creates a model from a specification dictionary. For example, the following specification:

```python
spec = {
    'type': 'Conv1d',
    'in_channels': 1,
    'out_channels': 16,
    'kernel_size': 3
}
create_model(spec)
```

Will create a ```torch.nn.Conv1d``` object with the specified parameters. The ```device='cpu'``` argument is passed to the constructor, but the specification dictionary can override it.

## Recursive Example

If we want to support Sequential models, we can use the ```construct``` function recursively:

```python
def create_model(spec):
    return construct(
        dict(
            Conv1d=torch.nn.Conv1d,
            Linear=torch.nn.Linear,
            Sequential=lambda subspecs: torch.nn.Sequential(*[
                create_model(subspec) for subspec in subspecs
            ]),
        ),
        spec,
        device='cpu'
    )
```

Now we can create a model like this:

```python
spec = {
    'type': 'Sequential',
    'subspecs': [
        {
            'type': 'Conv1d',
            'in_channels': 1,
            'out_channels': 16,
            'kernel_size': 3
        },
        {
            'type': 'Linear',
            'in_features': 16,
            'out_features': 10
        }
    ]
}
create_model(spec)
```

This will create a ```torch.nn.Sequential``` object with the specified submodules.
