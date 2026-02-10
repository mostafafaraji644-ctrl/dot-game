[app]
title = DotGame
package.name = dotgame
package.domain = org.example

source.dir = .
source.include_exts = py

entrypoint = main.py

version = 0.1

requirements = python3,kivy==2.3.1

orientation = portrait
fullscreen = 1

android.accept_sdk_license = True
android.api = 33
android.ndk = 25b
android.archs = arm64-v8a
