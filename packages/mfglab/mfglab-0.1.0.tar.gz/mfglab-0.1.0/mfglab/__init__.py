# mfglab/__init__.py
__version__ = "0.1.0"

__all__ = [
    "com",
    "config",
    "dshm",
    "llm",
    "rdbms",
    "tabular",
    "utils",
    "vision",
    "__version__",
]

from importlib import import_module
for mod in __all__[:-1]:
    globals()[mod] = import_module(f".{mod}", __name__)

