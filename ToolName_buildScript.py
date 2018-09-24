from cx_Freeze import setup, Executable
import sys

base = 'Win32GUI' if sys.platform=='win32' else None
buildOptions = dict(packages = [], excludes = [], includes = ["atexit"], include_files = ["icons/"])

executables = [
    Executable('ToolName.py', base=base, icon="icons/ToolName.ico")
]
setup(
    name='ToolName',
    version = '1.0',
    description = 'ToolName Show.',
    options = dict(build_exe = buildOptions),
    executables = executables
)