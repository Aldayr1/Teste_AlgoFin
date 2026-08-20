[app]
# Configurações Básicas
title = AlgoFin Teste
package.name = algofin
package.domain = org.alberto
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Bibliotecas Blindadas (Kivy 2.3.0 e KivyMD 1.1.1)
requirements = python3,kivy==2.3.0,kivymd==1.1.1

# Configurações de Tela
orientation = portrait
fullscreen = 0

# Configurações do Android
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True

# Motor Python
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
