import glob
import importlib
from os.path import dirname, isfile


def __list_all_modules():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(work_dir + "/*/*.py")

    all_modules = [
        (((f.replace(work_dir, "")).replace("/", "."))[:-3])
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return sorted(all_modules)


ALL_MODULES = __list_all_modules()


def load_plugins():
    for module in ALL_MODULES:
        try:
            importlib.import_module("BrandrdXMusic.plugins" + module)
            print(f"[PLUGIN LOADED] {module}")
        except Exception as e:
            print(f"[PLUGIN FAILED] {module} -> {e}")


__all__ = ALL_MODULES + ["ALL_MODULES", "load_plugins"]
