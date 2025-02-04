import importlib
import inspect


def resolve_entrypoint_signature(entrypoint: str) -> inspect.Signature:
    module_path, func_name = entrypoint.split(':')

    # import the module dynamically
    module = importlib.import_module(module_path)

    func = getattr(module, func_name)
    signature = inspect.signature(func)

    return signature
