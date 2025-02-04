"""""" # start delvewheel patch
def _delvewheel_patch_1_10_0():
    import os
    if os.path.isdir(libs_dir := os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'bfiocpp.libs'))):
        os.add_dll_directory(libs_dir)


_delvewheel_patch_1_10_0()
del _delvewheel_patch_1_10_0
# end delvewheel patch

from .tsreader import TSReader, Seq, FileType, get_ome_xml  # NOQA: F401
from .tswriter import TSWriter  # NOQA: F401
from . import _version

__version__ = _version.get_versions()["version"]
