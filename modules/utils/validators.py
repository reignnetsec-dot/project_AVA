

def normalize_filename(filename: str, extension: str) -> str:
    filename = filename.strip()
    if not filename:
        raise ValueError("Filename cannot be empty.")
    return filename if filename.lower().endswith(extension) else f"{filename}{extension}"


def prompt_non_empty(prompt: str) -> str:
    value = input(prompt).strip()
    if not value:
        raise ValueError("Input cannot be empty")
    return value