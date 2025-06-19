import io
import zipfile


def unzip_to_csv(data: bytes, path: str) -> bool:
    try:
        with zipfile.ZipFile(io.BytesIO(data.content)) as zf:
            with zf.open(zf.namelist()[0]) as f:
                with open(path, 'wb') as of:
                    of.write(f.read())
    except Exception as e:
        print(e)
        return False
    finally:
        return True
