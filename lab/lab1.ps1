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

# Function to handle errors
function Handle-Error {
  param([string]$ErrorMessage)
  Write-Host "Error: $ErrorMessage" -ForegroundColor Red
  Write-Host "Please check the script and try again."
}

# Main script loop
do {
  Display-Menu
  $choice = Read-Host "Enter your choice:"

  try {
      switch ($choice) {
          "1" {
              Display-Menu -SubMenu "Screen Lock"
              $screenLockChoice = Read-Host "Enter your screen lock choice (a or b):"
              switch ($screenLockChoice) {
                  "a" {
                      # Check screen lock status
                      (Get-ItemProperty -Path Registry::HKEY_CURRENT_USER\Control Panel\Desktop).ScreenSaveTimeOut
                      (Get-ItemProperty -Path Registry::HKEY_CURRENT_USER\Control Panel\Desktop).ScreenSaverIsSecure
                  }
                  "b" {
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
              Display-Menu -SubMenu "Antivirus"
              $antivirusChoice = Read-Host "Enter your antivirus choice (a or b):"
              switch ($antivirusChoice) {
                  "a" {
                      # Check antivirus status
                      Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled
                  }
                  "b" {
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
              Display-Menu -SubMenu "OS Updates"
              $osUpdateChoice = Read-Host "Enter your OS update choice (a, b, or c):"
              switch ($osUpdateChoice) {
                  "a" {
                      # Check OS version
                      Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion
                  }
                  "b" {
                      # Check for updates
                      Get-WUList | Where-Object {$_.IsInstalled -eq $false}
                  }
                  "c" {
                      # Update OS
                      Get-WUInstall -MicrosoftUpdate -AcceptAll -AutoReboot
                      Write-Host "OS updates initiated. The system may reboot automatically."
                  }
                  default
