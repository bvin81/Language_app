$WshShell = New-Object -ComObject WScript.Shell
$Desktop = [Environment]::GetFolderPath('Desktop')
$Shortcut = $WshShell.CreateShortcut("$Desktop\AI Language Tutor.lnk")
$Shortcut.TargetPath = "C:\Users\birov\Documents\Karrier\AI_language_tutor\start_app.bat"
$Shortcut.WorkingDirectory = "C:\Users\birov\Documents\Karrier\AI_language_tutor"
$Shortcut.Save()
Write-Host "Parancsikon letrehozva az Asztalon!"
