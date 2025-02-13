def sizeof(num, suffix="B"):
    """
    credit: Fred Cirera
      - https://stackoverflow.com/questions/1094841/get-human-readable-version-of-file-size
      - https://web.archive.org/web/20111010015624/http://blogmag.net/blog/read/38/Print_human_readable_file_size
    """  # noqa: E501
    f = "{num:.1f}{unit}{suffix}"
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f.format(num=num, unit=unit, suffix=suffix)
        num /= 1024.0
    return f.format(num=num, unit="Yi", suffix=suffix)
