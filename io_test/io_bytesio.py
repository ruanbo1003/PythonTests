
import io
import hashlib


def io_bytesio_test():
    with io.BytesIO() as buff:
        body = buff.getvalue()

    file_name = "filename_1"
    file_bytes = bytes(file_name, 'utf8')

    print(f"{dir(file_bytes)}")

    print(f"type(body):{type(body)}")
    print(f"type(file_bytes):{type(file_bytes)}")

    body_hash = hashlib.md5(body).hexdigest()
    print(f"mdt:{body_hash}")

    new_body = body + file_bytes
    new_body_hash = hashlib.md5(new_body).hexdigest()
    print(f"mdt:{new_body_hash}")


if __name__ == "__main__":
    io_bytesio_test()
