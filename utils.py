def process_file_by_chunk(file_path, proc = lambda chunk: chunk, chunksize = 4096)
    result = None
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(chunksize), b''):
            result = proc(chunk)
    return result