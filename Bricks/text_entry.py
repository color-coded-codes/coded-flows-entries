from coded_flows.types import Str



coded_flows_metadata = {
    "display_name": "Text",
    "description": "Textual input not exceeding 4096 characters",
    "icon": "keyboard",
    "type": "entry",
    "entry_type": "text"

}

def text_entry()-> Str:
    text_entry = ""
    return text_entry