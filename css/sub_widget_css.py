
version_file_css = """
QLineEdit{
    border-width: 0px;
    border-style: none;
    border-radius: 0px;
    background-color: transparent;
}

QLineEdit:focus:!read-only{
    border-width: 1px;
    border-style: solid;
    border-radius: 0px;
    background-color: white;
}

QLineEdit:read-only{
    border-width: 0px;
    border-style: none;
    border-radius: 0px;
    background-color: lightGray;
}
"""