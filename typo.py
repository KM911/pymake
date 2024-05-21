

TYPE_ERROR = {
    "docker": [
        "dockre", "dokcer"],
    "rust": ["rst"]
}
ERROR_DICT = {

}


for k, v in TYPE_ERROR.items():
    for i in v:
        ERROR_DICT[i] = k
