"""example usage API interface"""
if __name__ == '__main__':
    # base ast builder
    from ssc_codegen.ast_builder import build_ast_module
    # build-in converter
    from ssc_codegen.converters.py_parsel import converter
    # runtime import module and parse
    # WARNING: DO NOT PASS UNKNOWN MODULES FOR SECURITY REASONS
    # IT COMPILE AND EXEC PYTHON CODE FROM FILE IN RUNTIME
    ast = build_ast_module(
        'a.py',
    )
    code = converter.convert_program(ast)
    print("\n".join(code))
