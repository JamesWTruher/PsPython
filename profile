set-location /root
[environment]::CurrentDirectory = "/root"

@'

To run demo 1, type:
./pspar.py '$a = 1;$b =' "$PSHOME/Modules/PowerShellGet/PSModule.psm1"

To run demo 2, type:
./psrun.py

'@
