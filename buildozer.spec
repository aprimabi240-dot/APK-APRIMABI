[app]
title = Apk Apri
package.name = apkapri
package.domain = com.apri.apkapri
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0

[app:requirements]

[buildozer:state]
cache.buildozer = .buildozer
cache.platform = .platform

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreements = True
android.ant = False
