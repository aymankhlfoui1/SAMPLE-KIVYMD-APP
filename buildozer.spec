[app]
# (str) Title of your application
title = SimpleVPN

# (str) Package name
package.name = Movistarvpn

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (str) Title of your application
package.name = simplevpn

# (str) Full name of your application
package.full_name = SimpleVPN

# (str) The domain name associated with the package
package.domain = org.test

# (str) Source code location
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (str) Presplash of the application
presplash.filename = %(source.dir)s/presplash.png

# (list) Permissions required by the app (add here any additional permissions required)
android.permissions = INTERNET, BIND_VPN_SERVICE

# (list) Features required by the app (add here any additional features required)
# android.features = android.hardware.touchscreen

# (str) The name of the service
android.service = org.kivy.android.PythonService

# (str) Path to the manifest template file
android.manifest_template = ./manifest_template.xml

# (str) Android API to use
android.api = 31

# (str) Minimum API for the app
android.minapi = 21

# (str) Path to Android NDK
android.ndk = 23b

# (list) Requirements needed for the app
requirements = python3,kivy,android,jnius

# (bool) Enable full layout rendering
fullscreen = 0

# (list) Orientation of the app
orientation = portrait

# (str) Path to icon file
icon.filename = %(source.dir)s/icon.png

# (str) Path to permissions file
permissions.filename = %(source.dir)s/permissions.xml

# (bool) Enable SSL verification
android.verify_ssl = 1

# (str) Path to the splash screen
splash.filename = %(source.dir)s/splash.png

# (bool) Use Java as your default build language
android.use_java = 1

# (list) Include additional gradle dependencies
android.gradle_dependencies = org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.3.50

# (str) Path to the private directory
android.private_storage = True

# (list) Include additional resources
android.add_resources = res/values/strings.xml

[buildozer]

# (int) Log level
log_level = 2

# (bool) Warn if root access is enabled
warn_on_root = 1

# (str) Additional arguments for the build command
build_args = --release

# (str) Additional arguments for the clean command
clean_args = --all

# (bool) Enable verbose output
verbose = 1
