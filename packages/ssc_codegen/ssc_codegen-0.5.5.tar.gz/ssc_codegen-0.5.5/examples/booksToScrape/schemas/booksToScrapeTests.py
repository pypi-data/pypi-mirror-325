from ssc_codegen import D, N, ItemSchema, ListSchema, FlatListSchema, DictSchema

FMT_CATALOGUE = "https://books.toscrape.com/catalogue/{{}}"
FMT_BOOK = "https://books.toscrape.com/{{}}"


class Books(ListSchema):
    """Schema for extracting a list of books."""
    __SPLIT_DOC__ = D().css_all(".product_pod")

    name = D().css("h3 > a").attr("title")
    image_url = D().css(".thumbnail").attr("src").ltrim('../').fmt(FMT_BOOK)
    url = D().css("h3 > a").attr("href").fmt(FMT_CATALOGUE)
    # TODO: simple pattern-matching replace expr?
    rating = (D().css(".star-rating").attr("class").re(r"star-rating (\w+)")
              .re_sub(r"\bOne\b", "1")
              .re_sub(r"\bTwo\b", "2")
              .re_sub(r"\bThree\b", "3")
              .re_sub(r"\bFour\b", "4")
              .re_sub(r"\bFive\b", "5")
              ).to_int()
    price = D().css(".price_color").text().re(r"(\d+\.\d+)").to_float()


class Pagination(ItemSchema):
    """Schema for extracting pagination details."""
    showing_start=D().css(".form-horizontal").text().re(r'results \- showing (\d+) to \d+').to_int()
    showing_end=D().css(".form-horizontal").text().re(r'results \- showing \d+ to (\d+)').to_int()
    current_page = D().css('.current').text().re(r"Page (\d+) of \d+").to_int()
    total_page = D().css('.current').text().re(r"Page \d+ of (\d+)").to_int()

    next_page_url = D().default(None).css(".next > a").attr("href").fmt(FMT_CATALOGUE)
    previous_page_url = D().default(None).css(".previous > a").attr("href").fmt(FMT_CATALOGUE)


class BooksAll(ItemSchema):
    all_urls = D().is_css(".product_pod").css_all(".product_pod > h3 > a").attr("href").fmt(FMT_BOOK)
    all_names = D().is_css(".product_pod").css_all(".product_pod > h3 > a").text()


class BooksFlatNames(FlatListSchema):
    __SPLIT_DOC__ = D().css_all(".product_pod > h3 > a")
    __ITEM__ = D().text()

class BooksDict(DictSchema):
    __SPLIT_DOC__ = D().css_all(".product_pod")
    __KEY__ = D().css("h3 > a").text()
    __VALUE__ = N().sub_parser(Books)


class CataloguePage(ItemSchema):
    """Schema for extracting the entire catalogue page with nested schemas."""
    __PRE_VALIDATE__ = D().is_css('title').css("title").text().is_regex(r"Books to Scrape")
    # TODO: add shortcut remove whitespaces
    title = D().css("title").text().re_sub('^\s*').re_sub('\s*$')
    pagination = N().sub_parser(Pagination)
    books = N().sub_parser(Books)
    books_all = N().sub_parser(BooksAll)
    books_all_names = N().sub_parser(BooksFlatNames)
    books_dict = N().sub_parser(BooksDict)
    books_list = N().sub_parser(BooksFlatNames)