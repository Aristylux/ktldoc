def checkOptions(args: list[str]) -> int:
    if "-h" in args or "--help" in args:
        printHelp()
        return 1 # Quit
    
    if "-f" in args or "--file" in args:
        return 2
    

def printHelp():
    print("Usage: lxdoc [OPTION]...")

    print("if no option: kt by default")

    print("Options:")
    print("  -h,  --help  print this help")

    print("  -f,  --file  create the documentation for the file")

    # Not really needed because: detect extension
    # print("  -kt          latex documentation for Kotlin")
    # print("  -py          latex documentation from Python")