from coded_flows.types import DirectoryPath



coded_flows_metadata = {
    "display_name": "Folder Selection",
    "description": "Select a folder from your device",
    "icon": "folder-filled",
    "type": "entry",
    "entry_type": "folder"

}

def folder_entry()-> DirectoryPath:
    folder_entry = ""
    return folder_entry