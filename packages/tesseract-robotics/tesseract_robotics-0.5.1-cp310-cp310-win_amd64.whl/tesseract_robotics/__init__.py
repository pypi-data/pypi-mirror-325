"""""" # start delvewheel patch
def _delvewheel_patch_1_10_0():
    import os
    if os.path.isdir(libs_dir := os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'tesseract_robotics.libs'))):
        os.add_dll_directory(libs_dir)


_delvewheel_patch_1_10_0()
del _delvewheel_patch_1_10_0
# end delvewheel patch

def _tesseract_dll_path_():
    import sys
    import os
    if sys.platform == "win32" and sys.version_info[:2] >= (3, 8):
        tesseract_env_path = os.environ.get("TESSERACT_PYTHON_DLL_PATH",None)
        if tesseract_env_path:
            for p in tesseract_env_path.split(os.pathsep):
                os.add_dll_directory(p)

_tesseract_dll_path_()
del _tesseract_dll_path_
