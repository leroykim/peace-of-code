import pyperclip

"""
What is does: build scp command based on given information and copies the result command to clipboard for ctrl+v.
Purpose: to exchange data between local drive and a remote server.
Usage:
file_location = "my-file-location"
source_host = None
source_user = None

file_destination = "file-destination-in-a-remote-server"
dest_host = "remote-server-endpoint"
dest_user = "remote-server-user-name"

build_scp(
    file_location=file_location,
    source_host=source_host,
    source_user=source_user,
    file_destination=file_destination,
    dest_host=dest_host,
    dest_user=dest_user,
)
# scp my-file-location remote-server-user-name@remote-server-endpoint:file-destination-in-a-remote-server
"""


def build_path_info(*, location: str, host: str = None, user: str = None):
    path_string = location
    if host:
        path_string = (
            f"{user}@{host}:{path_string}" if user else f"{host}:{path_string}"
        )

    return path_string


def build_scp(
    *,
    file_location,
    source_host,
    source_user,
    file_destination,
    dest_host=None,
    dest_user=None,
    public_key=False,
    recursive=False,
):
    command = ["scp"]
    source_path = build_path_info(
        location=file_location, host=source_host, user=source_user
    )
    dest_path = build_path_info(
        location=file_destination, host=dest_host, user=dest_user
    )
    if public_key:
        command.append("-i")
        command.append(public_key)
    if recursive:
        command.append("-r")
    command.append(source_path)
    command.append(dest_path)
    command_str = " ".join(command)
    print(command_str)
    pyperclip.copy(command_str)
