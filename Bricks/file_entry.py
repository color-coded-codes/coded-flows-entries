from coded_flows.types import FilePath



coded_flows_metadata = {
    "display_name": "File Selection",
    "description": "Select a file from your device",
    "icon": "file-filled",
    "type": "entry",
    "entry_type": "file"

}

def file_entry()-> FilePath:
    file_entry = ""
    return file_entry