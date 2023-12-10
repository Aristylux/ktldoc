import os # For getting path and navigating

#[project name]/app/src/main/java/[com/example]/[.kt and packages]

def getFiles(extension: str) -> list[str]:

    current_directory = os.getcwd()
    print("Project Directory:", current_directory)

    # Define the path
    target_directory = os.path.join(current_directory, "app", "src", "main", "java")
    #print("Target Directory :", target_directory)

    navigateToFinalDir(target_directory)

    return listFiles(target_directory, extension)

    
def navigateToFinalDir(source_dir: str):
    while True:
        # List directories in the current directory
        items = 0
        subdirectory = ""
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isdir(item_path):
                subdirectory = item
            items += 1

        #print(f"Directory: {source_dir}")

        # If there is only one subdirectory, navigate into it
        if items == 1:
            source_dir = os.path.join(source_dir, subdirectory)
        else:
            # If there are no subdirectories or more than one, break out of the loop
            break
                
            
def listFiles(directory: str, extension: str) -> list[str]:
    items = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                items.append(os.path.join(root, file))
    return items