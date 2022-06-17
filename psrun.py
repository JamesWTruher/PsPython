#!/usr/bin/python3

from pspython import *

# run demo 1
# return objects to python for printing
scriptDefinition = 'Get-ChildItem'
print(f"{bcolors.HEADER}run the script: {scriptDefinition}{bcolors.RESET}")
result = PsRunScript(scriptDefinition)
PrintResults(result)

# run demo 1
# return objects to python, filter them (in python), then format them with PowerShell
print(f"\n{bcolors.HEADER}input provided by python with formatting{bcolors.RESET}")
# part 1 - gather object
scriptDefinition = 'Get-ChildItem'
result = list(filter(lambda r: r.BaseObject.Name.startswith('ps'), PsRunScript(scriptDefinition)))
# part 2 - use those results as input for PowerShell
ps.Commands.Clear()
ps.Commands.AddCommand("Out-String").AddParameter("Stream",True).AddParameter("InputObject", result)
strResult = ps.Invoke()
# print results
PrintResults(strResult)

# exit nicely
Environment.ExitCode = 0
