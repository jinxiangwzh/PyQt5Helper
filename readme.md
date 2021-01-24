# 开发笔记

## 1. 关于Pyinstaller版本显示
- 1.在PyQt5Helper实例化的时候开始Pyinstaller版本查询命令，读出返回后，信号通知再状态栏显示

## 2.测试项

### 2.1 命令测试项

- 1.General Options
  -[x] --distpath DIR <BR/>
  1.目录使能；2.目录保存；3.指定目录均测试OK
  -[x] --workpath WORKPATH <br/>
  1.目录使能；2.目录保存；3.指定目录均测试OK
  -[ ] --noconfirm
  -[ ] --upx-dir UPX_DIR
  -[ ] --ascii
  -[ ] --clean
  -[ ] --log-level LEVEL

- 2.What to generate
  -[ ] --onedir
  -[ ] --onefile
  -[ ] --specpath DIR
  -[ ] --name NAME
  
- 3.What to bundle, where to search
  -[ ] --add-data <SRC;DEST or SRC:DEST>
  -[ ] --add-binary <SRC;DEST or SRC:DEST>
  -[ ] --paths DIR
  -[ ] --hidden-import MODULENAME
  -[ ] --additional-hooks-dir HOOKSPATH
  -[ ] --runtime-hook RUNTIME_HOOKS
  -[ ] --exclude-module EXCLUDES
  -[ ] --key KEY
  -[ ] --debug <all,imports,bootloader,noarchive>
  
- 4.Windows and Mac OS X specific options
  -[ ] --console
  -[ ] --windowed
  -[ ] --icon <FILE.ico or FILE.exe,ID or FILE.icns>

- 5.Windows specific options
  -[ ] --version-file FILE
  -[ ] --manifest <FILE or XML>
  -[ ] --resource RESOURCE
  -[ ] --uac-admin
  -[ ] --uac-uiaccess
  
- 6.Windows Side-by-side Assembly searching options (advanced)
  -[ ] --win-private-assemblies
  -[ ] --win-no-prefer-redirects
  
- 7.Mac OS X specific options
  -[ ] --osx-bundle-identifier BUNDLE_IDENTIFIER
  
- 8.Rarely used special options
  -[ ] --runtime-tmpdir PATH
  -[ ] --bootloader-ignore-signals
  
## 3. TDDO

-[ ] 关闭主窗口,控制台信息显示窗口没有关闭
-[ ] 打包按键的背景色，反过来
  
 

