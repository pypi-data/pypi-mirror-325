import pathlib

from ssc_codegen.converters.tools import go_unimport_naive

if __name__ == '__main__':
    code = pathlib.Path("examples/go/booksToScrape.go").read_text(encoding="utf-8")

    print(go_unimport_naive(code))