import os
# DOTNET_ROOT is set in the docker image
# If you're not using docker, set the value correctly and uncomment the next line
# os.environ["DOTNET_ROOT"] = r'/pathto/.dotnet'
# set this to the location of your PowerShell installation
# this is the location in the container
psHome = r'/opt/microsoft/powershell/7-lts/'

# load up the clr
from clr_loader import get_coreclr
from pythonnet import set_runtime

# this is set in the container
runtimeConfig = r'/root/pspython.runtimeconfig.json'
rt = get_coreclr(runtimeConfig)
set_runtime(rt)
import clr
import sys
import System
from System import Environment

# we need to load MMI before we get started otherwise we get a
# strong name validation error
mmi = psHome + r'Microsoft.Management.Infrastructure.dll'
clr.AddReference(mmi)
from Microsoft.Management.Infrastructure import *

# load up the worker assembly
sma = psHome + r'System.Management.Automation.dll'
clr.AddReference(sma)
from System.Management.Automation import *
from System.Management.Automation.Language import Parser

ps = PowerShell.Create()
def PsRunScript(script):
    ps.Commands.Clear()
    ps.Commands.AddScript(script)
    result = ps.Invoke()
    rlist = []
    for r in result:
        rlist.append(r)
    return rlist

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class ParseResult:
    def __init__(self, scriptDefinition, tupleResult):
        self.ScriptDefinition = scriptDefinition
        self.Ast = tupleResult[0]
        self.Tokens = tupleResult[1]
        self.Errors = tupleResult[2]

    def PrintAst(self):
        print(self.ast.Extent.Text)

    def PrintErrors(self):
        for e in self.Errors:
            print(str(e))

    def PrintTokens(self):
        for t in self.Tokens:
            print(str(t))

    def GetAst(self, astname):
        Func = getattr(System, "Func`2")
        func = Func[System.Management.Automation.Language.Ast, bool](lambda a : type(a).__name__ == astname)
        asts = self.Ast.FindAll(func, True)
        return asts

def ParseScript(scriptDefinition):
    token = None
    error = None
    ast = Parser.ParseInput(scriptDefinition, token, error)
    pr = ParseResult(scriptDefinition, ast)
    return pr

def ParseFile(filePath):
    token = None
    error = None
    ast = Parser.ParseFile(filePath, token, error)
    pr = ParseResult(filePath, ast)
    return pr

def PrintResults(result):
    for r in result:
        print(r)
