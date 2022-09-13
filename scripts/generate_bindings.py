import sys
import clang.cindex
# from devana.syntax_abstraction.typeexpression import BasicType, TypeModification
# from devana.syntax_abstraction.functioninfo import FunctionInfo, FunctionModification
# from devana.syntax_abstraction.organizers.sourcefile import SourceFile
# from devana.utility.errors import CodeError
# from devana.syntax_abstraction.organizers.lexicon import Lexicon

# EMSCRIPTEN_BINDINGS(my_module) {
#     function("lerp", &lerp);
# }

def generateBindingString(path):
    binding = "/* Generated */\nEMSCRIPTEN_BINDINGS(my_module) {\n"
    index = clang.cindex.Index.create()
    globalNamespaceNode = index.parse(path).cursor
    for n in globalNamespaceNode.get_children():
        if n.kind == clang.cindex.CursorKind.FUNCTION_DECL:
            binding += f'    function("{n.spelling}", &{n.spelling});\n'
        # print(n.kind == clang.cindex.CursorKind.FUNCTION_DECL, n.spelling)
        # result = FunctionInfo(n)
        # result.lexicon = Lexicon()
        # print(result.return_type)
    binding += '}\n/* Generated */\n'
    return binding

def main():
    path = sys.argv[1]
    print(generateBindingString(path))

if __name__ == "__main__":
    main()
