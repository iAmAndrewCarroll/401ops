# PowerShell Script to Configure Password Complexity, Minimum Password Length, and SMB v1 Client Driver Status

# Function to get the current status of SMB v1 client driver
Function Get-SMBv1ClientStatus {
  $path = "HKLM:\SYSTEM\CurrentControlSet\Services\mrxsmb10"
  $name = "Start"

  # Check if the registry path exists
  If (Test-Path $path) {
      $currentStatus = (Get-ItemProperty -Path $path).$name
      Return $currentStatus
  } Else {
      Write-Warning "Registry path not found: $path"
      Return $null
  }
}

# Function to set the SMB v1 client driver configuration
Function Set-SMBv1ClientConfiguration {
  param (
      [bool]$disable
  )
  $path = "HKLM:\SYSTEM\CurrentControlSet\Services\mrxsmb10"
  $name = "Start"
  
  if ($disable) {
      $value = 4 # 4 corresponds to Disabled
      $statusMessage = "Enabled: Disable driver (recommended)"
  } else {
      $value = 2 # 2 corresponds to Automatic
      $statusMessage = "Automatic (default)"
  }

  # Check if the registry path exists
  If (Test-Path $path) {
      # Set the registry value
      Set-ItemProperty -Path $path -Name $name -Value $value
      Write-Host "SMB v1 client driver has been configured to: $statusMessage"
  } Else {
      Write-Warning "Registry path not found: $path"
  }
}

# Function to get the current status of Password Complexity
Function Get-PasswordComplexityStatus {
  $seceditOutput = secedit /export /cfg "$env:temp\secpol.cfg"
  $complexityStatus = $seceditOutput | Select-String -Pattern "PasswordComplexity\s*=\s*\d"

  if ($complexityStatus -match "PasswordComplexity\s*=\s*1") {
      return "Enabled"
  } else {
      return "Disabled"
  }
}

# Function to set Password Complexity
Function Set-PasswordComplexity {
  param (
      [bool]$Enable
  )
  $value = if ($Enable) { 1 } else { 0 }
  $seceditOutput = secedit /export /cfg "$env:temp\secpol.cfg"
  $seceditOutput | ForEach-Object { $_ -replace "PasswordComplexity\s*=\s*\d", "PasswordComplexity = $value" } | Out-File "$env:temp\secpol.cfg"

  $seceditImport = secedit /configure /db "$env:windir\security\local.sdb" /cfg "$env:temp\secpol.cfg" /areas SECURITYPOLICY > $null

  if ($Enable) {
      Write-Host "Password Complexity has been Enabled"
  } else {
      Write-Host "Password Complexity has been Disabled"
  }
}

# Function to get the current Minimum Password Length
Function Get-MinimumPasswordLength {
  $seceditOutput = secedit /export /cfg "$env:temp\secpol.cfg"
  $minLengthStatus = $seceditOutput | Select-String -Pattern "MinimumPasswordLength\s*=\s*\d"

  if ($minLengthStatus -match "MinimumPasswordLength\s*=\s*(\d+)") {
      return $matches[1]
  } else {
      return "Not Set"
  }
}

# Function to set Minimum Password Length
Function Set-MinimumPasswordLength {
  param (
      [int]$Length
  )
  $seceditOutput = secedit /export /cfg "$env:temp\secpol.cfg"
  $seceditOutput | ForEach-Object { $_ -replace "MinimumPasswordLength\s*=\s*\d", "MinimumPasswordLength = $Length" } | Out-File "$env:temp\secpol.cfg"

  $seceditImport = secedit /configure /db "$env:windir\security\local.sdb" /cfg "$env:temp\secpol.cfg" /areas SECURITYPOLICY > $null

  Write-Host "Minimum Password Length has been set to: $Length characters"
}

# Display current settings
Write-Host "Password Complexity Settings:"
$complexityStatus = Get-PasswordComplexityStatus
Write-Host "Current Password Complexity Status: $complexityStatus"

Write-Host "Minimum Password Length Settings:"
$minLength = Get-MinimumPasswordLength
Write-Host "Current Minimum Password Length: $minLength characters"

# User interaction for Password Complexity
$complexitySelection = Read-Host "Do you want to (E)nable or (D)isable Password Complexity? (E/D)"
Switch ($complexitySelection.ToUpper()) {
  'E' { Set-PasswordComplexity -Enable $true }
  'D' { Set-PasswordComplexity -Enable $false }
  Default { Write-Host "Invalid selection. No changes were made to Password Complexity." }
}

# User interaction for Minimum Password Length
$newLength = Read-Host "Enter the new minimum password length"
if ($newLength -match "^\d+$") {
  Set-MinimumPasswordLength -Length $newLength
} else {
  Write-Host "Invalid input. Please enter a numeric value for Minimum Password Length."
}

# Get and display the current status of SMB v1 client driver
$currentStatus = Get-SMBv1ClientStatus
If ($currentStatus -eq 4) {
  Write-Host "Current status of SMB v1 client driver: Disabled"
} Else {
  Write-Host "Current status of SMB v1 client driver: Enabled"
}

# User interaction for SMB v1 client driver
$choice = Read-Host "Do you want to (E)nable or (D)isable SMB v1 client? (E/D)"
If ($choice -eq "E" -or $choice -eq "e") {
  # Call the function to set SMB v1 client configuration to Enabled
  Set-SMBv1ClientConfiguration -disable $false
  Write-Host "SMB v1 client driver has been enabled."
} elseif ($choice -eq "D" -or $choice -eq "d") {
  # Call the function to set SMB v1 client configuration to Disabled
  Set-SMBv1ClientConfiguration -disable $true
  Write-Host "SMB v1 client driver has been disabled."
} else {
  Write-Host "Invalid choice. No changes were made to SMB v1 client driver."
}

# Get and display the updated status of SMB v1 client driver
$updatedStatus = Get-SMBv1ClientStatus
If ($updatedStatus -eq 4) {
  Write-Host "Updated status of SMB v1 client driver: Disabled"
} Else {
  Write-Host "Updated status of SMB v1 client driver: Enabled"
}
