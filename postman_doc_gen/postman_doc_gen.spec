# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['postman_doc_gen.py'],
    pathex=['/Users/kelishrestha/terminal-spaces/work-space/postman-doc-gen'],
    binaries=[],
    datas=[('./schemas/schema_2_1_0.json', 'schemas'),
                    ('./templates/index.html', 'templates'),
                    ('./templates/css/*.css', 'templates/css'),
                    ('./templates/js/*.js', 'templates/js')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='postman_doc_gen',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
