from ssc_codegen import D, N, DictSchema, ItemSchema, ListSchema


class Foo(DictSchema):
    __SPLIT_DOC__ = D().css_all('b')
    __KEY__ = D().default("null").attr("a")
    __VALUE__ = D().default(None).attr("b")