# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:/programs/accountancy/program2.py'],
             pathex=['D:\\programs\\accountancy'],
             binaries=[],
             datas=[('D:/programs/accountancy/addcustomer.py', '.'), ('D:/programs/accountancy/addproduct.png', '.'), ('D:/programs/accountancy/bill.png', '.'), ('D:/programs/accountancy/partyname.py', '.'), ('D:/programs/accountancy/pl.png', '.'), ('D:/programs/accountancy/profitnloss.py', '.'), ('D:/programs/accountancy/testpdf.py', '.'), ('D:/programs/accountancy/docimage', 'docimage/'), ('D:/programs/accountancy/ICON', 'ICON/'), ('D:/programs/accountancy/docimage/signature.png', '.'), ('D:/programs/accountancy/docimage/Tanet.png', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='program2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='D:\\programs\\accountancy\\ICON\\JS PETS AND PRODUCTS.ico')
