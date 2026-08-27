; AEGIS Capture Windows Installer
; Compiled with Inno Setup 6

#define MyAppName "AEGIS Capture"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "LeverageFx / Honeydewnuts"
#define MyAppURL "https://aegis-api-0z1p.onrender.com"

[Setup]
AppId={{AEGIS-CAPTURE-WIN-2026}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=Output
OutputBaseFilename=AEGIS_Capture_Setup
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; Main EXE from PyInstaller
Source: "dist\AEGIS_Capture\AEGIS_Capture.exe"; DestDir: "{app}"; Flags: ignoreversion

; All supporting files from PyInstaller folder
Source: "dist\AEGIS_Capture\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

; MT5 EA - THIS IS THE NEW LINE
Source: "mq5\AEGIS_Executor.mq5"; DestDir: "{app}\mq5"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\AEGIS_Capture.exe"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\AEGIS_Capture.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\AEGIS_Capture.exe"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
