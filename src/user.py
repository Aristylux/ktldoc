def checkOptions(args: list[str]) -> int:
    if "-h" in args or "--help" in args:
        printHelp()
        return 1 # Quit
    

def printHelp():
    print("Usage: lxdoc [OPTION]...")

    print("if no option: kt by default")

    print("Options:")
    print("  -h,  --help  print this help")
    print("  -kt          latex documentation for Kotlin")
    print("  -py          latex documentation from Python")