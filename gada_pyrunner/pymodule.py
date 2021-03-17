"""Can run a python module directly from code.
"""
from typing import List, Optional


def load_module(name: str):
    try:
        import importlib

        return importlib.import_module(name)
    except Exception as e:
        raise Exception(f"failed to import module {name}") from e


def run(
    comp, *, gada_config: dict, node_config: dict, argv: Optional[List] = None
):    
    if "entrypoint" not in node_config:
        raise Exception("missing entrypoint in configuration")

    if "module" in node_config:
        comp = load_module(node_config["module"])

    fun = getattr(comp, node_config["entrypoint"])
    fun(argv=argv)
