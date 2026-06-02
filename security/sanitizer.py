import gc


def sanitize_memory(data):
    data.clear()

    del data

    gc.collect()
