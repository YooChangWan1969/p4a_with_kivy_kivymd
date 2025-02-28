[app]
title = sample
package.name = sampleApp
package.domain = org.kivy
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
source.include_patterns = assets/*,images/*.png
source.exclude_exts = spec,txt
source.exclude_dirs = tests, bin, venv, __pycache__
version = 0.1
requirements = python3==3.11.0,hostpython3==3.11.0,kivy==2.1.0,kivymd==1.0.1,cython==0.29.33,sdl2_ttf,pillow,liblzma,pyjnius==1.4.2
# requirements = python3,hostpython3,kivy,kivymd,cython,sdl2_ttf,pillow,liblzma,pyjnius,pycryptodome
# presplash.filename = %(source.dir)s/images/presplash.png
# icon.filename = %(source.dir)s/images/favicon.png
orientation = portrait
osx.python_version = 3.11.0
osx.kivy_version = 2.1.0
fullscreen = 0
android.permissions = android.permission.INTERNET, (name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18)
android.api = 33
android.enable_android_native_support = True
# android.add_compile_options = -DANDROID_UNIFIED_HEADERS -fomit-frame-pointer
# android.add_compile_options = -DANDROID_UNIFIED_HEADERS -fomit-frame-pointer -Wno-array-bounds
android.add_compile_options = -fomit-frame-pointer -Wno-array-bounds -I/path/to/ndk/sysroot/usr/include
android.extra_compile_args = -Wno-array-bounds, -Wno-deprecated-declarations, -fPIC, -D__GNUC_PREREQ(major,minor)=0
android.cppflags = -DANDROID -I/home/runner/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/linux-x86_64/sysroot/usr/include -I/home/runner/work/p4a_with_kivy_kivymd/p4a_with_kivy_kivymd/.buildozer/android/platform/build-arm64-v8a/build/python-installs/sampleApp/arm64-v8a/include/python3.11
android.ndk_api = 21
android.ndk = 25b
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b
android.min_sdk_version = 21
android.sdk_api = 33
# android.gradle_dependencies = 'androidx.multidex:multidex:2.0.1'
#android.add_dependencies = true
android.private_storage = True
android.cmake_args = -DANDROID_PLATFORM=21 -DCMAKE_ANDROID_API=21
build.cmake_options = -DCMAKE_POSITION_INDEPENDENT_CODE=1 -DENABLE_SHARED=0 -DENABLE_STATIC=1
android.enable_androidx = True
android.enable_numpy = False
android.copy_libs = True
android.add_src = True
android.setup_py_install = False
android.python_packages = grp:skip
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.host_python_ver = 3.11.0
p4a.host_python = /opt/hostedtoolcache/Python/3.11.0/x64/bin/python3
p4a.extra_args = --ignore-setup-py
p4a.branch = master
#p4a.branch = release-2022.12.20
p4a.bootstrap = sdl2
p4a.local_recipes = ./recipes
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false
[buildozer]
log_level = 2
warn_on_root = 1
