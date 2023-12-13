import os # For getting path and navigating
from collections import Counter

#[project name]/app/src/main/java/[com/example]/[.kt and packages]

def getFiles() -> tuple[list[str], str]:
    current_directory = os.getcwd()
    print("Project Directory:", current_directory)

    # Detect project extension used
    extension = primaryExtension(current_directory)
    print(f"Common extension: {extension}")

    # Define the path
    target_directory = getTargetDirectory(current_directory, extension)
    #print("Target Directory :", target_directory)

    navigateToFinalDir(target_directory)

    return listFiles(target_directory, extension), os.path.basename(current_directory)


def primaryExtension(path: str) -> str:
    extension_supported = [".kt", ".py"]
    file_extensions = []

    # Traverse the directory and its subdirectories
    for _, _, files in os.walk(path):
        for file in files:
            _, extension = os.path.splitext(file)
            # Check if the extension is in the allowed list
            if extension.lower() in extension_supported:
                file_extensions.append(extension.lower())

    # Count the occurrences of each file extension
    extension_counter = Counter(file_extensions)

    # Find the most common file extension
    most_common_extension = extension_counter.most_common(1)

    if most_common_extension:
        return most_common_extension[0][0]
    else:
        return ""
    
def getTargetDirectory(root_path: str, extension: str) -> str:
    target_directory = root_path
    # if .kt verify if its not a android project
    if extension == ".kt": # or extension == ".java":
        if isAndroidProject(root_path):
            target_directory = os.path.join(root_path, "app", "src", "main", "java")
    
    return target_directory

def isAndroidProject(root_path: str) -> bool:
    android_project_dir = ["app", "build", "gradle"]

    for directory in android_project_dir:
        directory_path = os.path.join(root_path, directory)
        if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
            return False

    return True
    
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
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extension):
                files.append(os.path.join(root, filename))
    return files



# ---- Saving ----

def createOutputDir(projectName: str):
    directoryName = "output_" + projectName.lower()
    directoryFileName = os.path.join(directoryName, "files")
    # Create the directory if it doesn't exist
    if not os.path.exists(directoryName):
        os.makedirs(directoryName)

    if not os.path.exists(directoryFileName):
        os.makedirs(directoryFileName)



def createFilesDir(projectName: str):
    directoryName = "output_" + projectName.lower() + "/sections"
    # Create the directory if it doesn't exist
    if not os.path.exists(directoryName):
        os.makedirs(directoryName)

def writeFile(projectName: str, fileName: str, content: str):
    # Create the file path by joining the directory and file names
    file_path = os.path.join("output_" + projectName.lower(), fileName)

    # Open the file in write mode and save the string
    with open(file_path, 'w') as file:
        file.write(content)