try:
    from mkdocs.commands.babel import (
        compile_catalog,
        extract_messages,
        init_catalog,
        update_catalog,
    )

    babel_cmdclass = {
        "compile_catalog": compile_catalog,
        "extract_messages": extract_messages,
        "init_catalog": init_catalog,
        "update_catalog": update_catalog,
    }
except ImportError:
    babel_cmdclass = {}
