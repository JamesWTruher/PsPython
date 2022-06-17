#!/usr/bin/python3

from pspython import *

# positional parameters
scriptDefinition = sys.argv[1]
scriptFile = sys.argv[2]

print(f"{bcolors.HEADER}Parse a script '{scriptDefinition}':{bcolors.RESET}")
parseResult = ParseScript(scriptDefinition)
print(f"{bcolors.HEADER}Tokens:{bcolors.RESET}")
parseResult.PrintTokens()
print(f"{bcolors.HEADER}Errors:{bcolors.RESET}")
parseResult.PrintErrors()
print(f"{bcolors.HEADER}Variables:{bcolors.RESET}")
varAst = parseResult.GetAst("VariableExpressionAst")
PrintResults(varAst)

print(f"{bcolors.HEADER}Press <ENTER> to continue{bcolors.RESET}")
input()
print(f"{bcolors.HEADER}parse a file '{scriptFile}'{bcolors.RESET}")
parseResult = ParseFile(scriptFile)
commandAst = parseResult.GetAst("CommandAst")
commands = set()
for c in commandAst:
    commandName = c.GetCommandName()
    # sometimes CommandName is null, don't include those
    if commandName != None:
       commands.add(c.GetCommandName().lower())
PrintResults(sorted(commands))
print(f"{bcolors.HEADER}How many unique commands?{bcolors.RESET}")
print(len(commands))

# exit nicely
Environment.ExitCode = 0

