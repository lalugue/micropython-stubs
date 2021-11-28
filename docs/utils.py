LATEST = "Latest"


def clean_version(
    version: str,
    *,
    build: bool = False,
    patch: bool = False,
    commit: bool = False,
    drop_v: bool = False,
    flat: bool = False
):
    "Clean up and transform the many flavours of versions"
    # 'v1.13.0-103-gb137d064e' --> 'v1.13-103'

    if version in ["", "-"]:
        return version
    nibbles = version.split("-")
    if not patch:
        if nibbles[0] >= "1.10.0" and nibbles[0].endswith(".0"):
            # remove the last ".0"
            nibbles[0] = nibbles[0][0:-2]
    if len(nibbles) == 1:
        version = nibbles[0]
    elif build and build != "dirty":
        if not commit:
            version = "-".join(nibbles[0:-1])
        else:
            version = "-".join(nibbles)
    else:
        version = "-".join((nibbles[0], LATEST))
    if flat:
        version = version.strip().replace(".", "_")
    if drop_v:
        version = version.lstrip("v")
    else:
        if not version.startswith("v"):
            version = "v" + version
    return version


# def __test():
# print(clean_version("1.9.3"))
# print(clean_version("-"))
#     print(clean_version("1.9.3"))
#     print(clean_version("v1.9.3"))
#     print(clean_version("v1.10.0"))
#     print(clean_version("v1.13.0"))
#     print(clean_version("v1.13.0-103-gb137d064e"))
#     print(clean_version("v1.13.0-103-gb137d064e", patch=True))
#     print(clean_version("v1.13.0-103-gb137d064e", patch=True, build=True))
#     print(clean_version("v1.13.0-103-gb137d064e", patch=True, build=True, commit=True))
#     print(
#         clean_version(
#             "v1.13.0-103-gb137d064e", patch=True, build=True, commit=True, flat=True
#         )
#     )
#     print(
#         clean_version(
#             "v1.13.0-103-gb137d064e",
#             patch=True,
#             build=True,
#             commit=True,
#             flat=True,
#             drop_v=True,
#         )
#     )