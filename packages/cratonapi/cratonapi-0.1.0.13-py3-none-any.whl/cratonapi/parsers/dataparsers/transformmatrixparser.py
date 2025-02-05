import struct

from cratonapi.datacontainers import TransformMatrix


def parse(message: bytes) -> TransformMatrix:
    if len(message) < 16:
        raise RuntimeError("Incomplete message!")
    signature = message[0:4].decode("utf-8")
    if signature != "WSPM":
        raise RuntimeError("Incorrect signature!")
    size, operation, request, uid = struct.unpack("<IHHI", message[4:16])
    if uid == 0 or (operation == 2 and request == 27 and size == 12):
        raise RuntimeError("Desmana is not open!")
    if operation != 3 or request != 27:
        raise RuntimeError("Incorrect operation or request codes!")
    if len(message) - 8 != size:
        raise RuntimeError("Incomplete message!")

    a, b, c, d, e, f, g, h = struct.unpack("<8d", message[16: 80])
    return TransformMatrix(
        a,
        b,
        c,
        d,
        e,
        f,
        g,
        h
    )
