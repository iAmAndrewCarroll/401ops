# Function to display the menu
function Display-Menu {
  param([string]$SubMenu)
  Clear-Host
  Write-Host "SOC 2 Configuration Menu"
  Write-Host "-----------------------"
  if ($SubMenu) {
      Write-Host "$SubMenu"
  }
  Write-Host "1. Screen Lock"
  Write-Host "2. Antivirus"
  Write-Host "3. OS Updates"
  Write-Host "4. Exit"
}

# Main script loop
while ($true) {
  Display-Menu
  $choice = Read-Host "Enter your choice:"

  switch ($choice) {
      "1" {
          $subMenu = @"
1. Check Screen Lock Status
2. Modify Screen Lock Settings
"@
          Display-Menu -SubMenu $subMenu
          $screenLockChoice = Read-Host "Enter your screen lock choice (1 or 2):"
          switch ($screenLockChoice) {
              "1" {
                  # Check screen lock status
                  (Get-ItemProperty -Path Registry::HKEY_CURRENT_USER\Control Panel\Desktop).ScreenSaveTimeOut
                  (Get-ItemProperty -Path Registry::HKEY_CURRENT_USER\Control Panel\Desktop).ScreenSaverIsSecure
              }
              "2" {
                  # Modify screen lock settings
                  $timeout = Read-Host "Enter new screen timeout in seconds (e.g., 900 for 15 minutes):"
                  Powershell.exe (Add-Type '[DllImport("user32.dll")]public static extern int SystemParametersInfo(int uAction, int uParam, int lpvParam, int fuWinIni);' -Name SetScreenSaverTimeout -Pas)::SetScreenSaverTimeout(0, $timeout, 0, 0)
                  Powershell.exe (Add-Type '[DllImport("user32.dll")]public static extern int SystemParametersInfo(int uAction, int uParam, int lpvParam, int fuWinIni);' -Name SetPasswordProtector -Pas)::SetPasswordProtector(1, 1, 0)
                  Write-Host "Screen lock settings modified successfully." -ForegroundColor Green
              }
              default {
                  Write-Host "Invalid screen lock choice. Please try again."
              }
          }
      }
      "2" {
          $subMenu = @"
1. Check Antivirus Status
2. Modify Antivirus Settings
"@
          Display-Menu -SubMenu $subMenu
          $antivirusChoice = Read-Host "Enter your antivirus choice (1 or 2):"
          switch ($antivirusChoice) {
              "1" {
                  # Check antivirus status
                  Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled
              }
              "2" {
                  # Modify antivirus settings
                  # Enable real-time protection if disabled
                  If ($false -eq (Get-MpComputerStatus).RealTimeProtectionEnabled) {
                      Set-MpPreference -DisableRealtimeMonitoring $false
                      Write-Host "Real-time protection enabled."
                  } else {
                      Write-Host "Real-time protection is already enabled."
                  }
                  # Initiate a full scan
                  Start-MpScan -ScanType FullScan
                  Write-Host "Full scan initiated."
              }
              default {
                  Write-Host "Invalid antivirus choice. Please try again."
              }
          }
      }
      "3" {
          $subMenu = @"
1. Check OS Version
2. Check for Updates
3. Update OS
"@
          Display-Menu -SubMenu $subMenu
          $osUpdateChoice = Read-Host "Enter your OS update choice (1, 2, or 3):"
          switch ($osUpdateChoice) {
              "1" {
                  # Check OS version
                  Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion
              }
              "2" {
                  # Check for updates
                  Get-WUList | Where-Object {$_.IsInstalled -eq $false}
              }
              "3" {
                  # Update OS
                  Get-WUInstall -MicrosoftUpdate -AcceptAll -AutoReboot
                  Write-Host "OS updates initiated. The system may reboot automatically."
              }
              default {
                  Write-Host "Invalid OS update choice. Please try again."
              }
          }
      }
      "4" {
          # Exit the script
          exit
      }
      default {
          Write-Host "Invalid choice. Please select a valid option (1-4)."
      }
  }
}
