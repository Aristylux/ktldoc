def checkOptions(args: list[str]) -> int:
    if "-h" in args or "--help" in args:
        printHelp()
        return 1 # Quit
    

def printHelp():
    print("USAGE: ")

    print("OPTIONS:")
    print("-h,\t--help, print this help")
    print("-kt\t, latex documentation for Kotlin")
    print("-py\t, latex documentation from Python")