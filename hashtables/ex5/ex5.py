

def finder(files, queries):

    queriesDict = {query: None for query in queries}
    filesDict = {file: None for file in files}
    result = []

    for file in filesDict:
        if file.split("/")[-1] in queriesDict:
            result.append(file)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
