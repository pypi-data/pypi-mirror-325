from setuptools import setup
from setuptools.command.install import install
import platform, sys, os, site
from os import path, environ

#------------------------------------
# Start menu item creation on Windows
#------------------------------------

def create_shortcut_under(root, exepath):
    profile = environ[root]
    linkpath = path.join(profile, "Microsoft", "Windows", "Start Menu", "Programs", "DWARF Explorer.lnk")
    try:
        from win32com.client import Dispatch
        from pywintypes import com_error
        try:
            sh = Dispatch('WScript.Shell')
            link = sh.CreateShortcut(linkpath)
            link.TargetPath = exepath
            link.Save()
            return True
        except com_error:
            return False
    except ImportError:
        import subprocess
        s = "$s=(New-Object -COM WScript.Shell).CreateShortcut('" + linkpath + "');$s.TargetPath='" + exepath + "';$s.Save()"
        return subprocess.call(['powershell', s], stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL) == 0

def create_shortcut(inst):
    try:
        exepath = path.join(path.dirname(sys.executable), "Scripts", "dwex.exe")
        if not path.exists(exepath):
            exepath = path.join(path.dirname(site.getusersitepackages()), "Scripts", "dwex.exe")

        if not create_shortcut_under('ALLUSERSPROFILE', exepath):
            create_shortcut_under('APPDATA', exepath)
    except:
        pass

#--------------------------------------    

def register_desktop_app():
    try:
        import base64, subprocess
        with open('/usr/share/applications/dwex.desktop', 'w') as f:
            f.write("[Desktop Entry]\nVersion=1.1\nType=Application\nName=DWARF Explorer\nComment=Debug information visualizer\nExec=dwex\nTerminal=false\nIcon=dwex\nCategories=Development;Debugger;\n")
        with open('/usr/share/icons/hicolor/48x48/apps/dwex.png', 'wb') as f:
            f.write(base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAADAAAAAwBAMAAAClLOS0AAAAKnRFWHRDcmVhdGlvbiBUaW1lANHhIDYg7e7/IDIwMjEgMTM6MDg6NDcgLTA1MDBuo0qzAAAAB3RJTUUH5QsGEQ8VL0d/PwAAAAlwSFlzAAALEgAACxIB0t1+/AAAAARnQU1BAACxjwv8YQUAAAAGUExURf///wAAAFXC034AAACkSURBVHjavdNREoUgCAXQyw5g/5sNxEoEpvc+yim0OcUoJvBRE2sAaeQRAkgB0NdBbJcPfgMNbglI8w9AAu1tDjXQv8DEUgH1gAwaDKQEu3kDWzBVIBNCReaG+Fc7oIAvGt1/g61cnsGnaM9nn0B89Rloq9UF4JDJd9VHsSILSIR7jiHTAm0qbiHNau7StlEXlCU5T0ALS65Zdh5lp+VwtvByOwCIiA5ALXz03AAAAABJRU5ErkJggg=="))
        subprocess.call('update-desktop-database')
    except:
        pass

#--------------------------------------

class my_install(install):
    def run(self):
        install.run(self)
        if platform.system() == 'Windows':
            create_shortcut(self)
        elif platform.system() == 'Linux':
            register_desktop_app()

# Pull the long desc from the readme
try:
    with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
        long_desc = f.read()          
except:
    long_desc = "GUI viewer for DWARF debug information"

setup(
    name='dwex',
    version='4.41',  # Sync with version in __main__
    packages=['dwex'],
    url="https://github.com/sevaa/dwex/",
    entry_points={"gui_scripts": ["dwex = dwex.__main__:main"]},
    cmdclass={'install': my_install},
    keywords = ['dwarf', 'debug', 'debugging', 'symbols', 'viewer', 'view', 'browser', 'browse', 'tree'],
    license="BSD",
    author="Seva Alekseyev",
    author_email="sevaa@sprynet.com",
    description="GUI viewer for DWARF debug information",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    python_requires=">=3.6.1",
    setup_requires=[],
    install_requires=['PyQt6', 'filebytes>=0.10.1', 'pyelftools>=0.30'] + (['pyobjc'] if platform.system() == 'Darwin' else []),
    platforms='any',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Environment :: MacOS X :: Cocoa",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications :: Qt",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Debuggers"
    ]
)

