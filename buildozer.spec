[app]

# (str) Title of your application
title = SampleApp

# (str) Package name
package.name = nfsApk

# (str) Package domain (needed for android/ios packaging)
package.domain = org.novfensec

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.0,kivymd==1.1.1,pillow==10.3.0,openssl

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements = 

# (str) Presplash of the application
presplash.filename = %(source.dir)s/images/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/images/favicon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

# 
# author = 

# change the major version of python used by the app
#osx.python_version = 3

# Kivy version to use
#osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = android.permission.INTERNET, android.permission.BIND_VPN_SERVICE, android.permission.WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 19b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path = 

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path = 

# (bool) enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin source.
android.enable_androidx = True

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (int) autoconnect native environment
#android.autoconnect = 0

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) android architecture that will be installed in the device
#android.install_arch = arm64-v8a

# (str) Python-for-Android branch to use, defaults to master
p4a.branch = master

# (str) Extra command line arguments to pass when invoking python-for-android
p4a.extra_args = --requirements=openssl

# 
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios

# (str) Xcode version to use
#ios.xcode = /Applications/Xcode.app/Contents/Developer

# (str) Xcode build type
#ios.xcode_build_type = Debug

# (str) ios arch to build
#ios.archs = arm64

#
# Buildozer specific
#

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = 

# (str) Path to buildozer storage, absolute or relative to spec file
#bin_dir = 

# (list) Directory to exclude (default is .svn,.git,.hg,dist,build,__pycache__)
#exclude_dirs = 

# (list) Directory to exclude in the final archive for the App
#exclude_dirs_sdist = 

# (list) Include specific files into the distribution
#include_files = 

# (str) Change the build type to manual (to overwrite specific build commands)
# build_type = manual

# (str) Where to unpack (temp) files used for build
# temp_dir =
