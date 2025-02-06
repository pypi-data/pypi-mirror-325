import pathlib
import pprint

from python.booksToScrapeExtend import CataloguePage

if __name__ == "__main__":
    resp = pathlib.Path("booksToScrapePage.html").read_text(encoding="utf-8")

    # mod = Compiler.from_file("schemas/booksToScrapeExtend.py", converter=converter)
    # pprint.pprint(
    #     mod.run_parse("CataloguePage", resp),
    #     compact=True
    # )
    result = CataloguePage(resp).parse()
    pprint.pprint(result, compact=True)
