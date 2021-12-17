import sys
import clang.cindex
from devana.syntax_abstraction.typeexpression import BasicType, TypeModification
from devana.syntax_abstraction.functioninfo import FunctionInfo, FunctionModification
from devana.syntax_abstraction.organizers.sourcefile import SourceFile
from devana.utility.errors import CodeError
from devana.syntax_abstraction.organizers.lexicon import Lexicon

# def find_by_name(node, text):
#     if node.spelling == text:
#         return node
#     for n in node.get_children():
#         r = find_by_name(n, text)
#         if r is not None:
#             return r
#     return None

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

# class TestFunctionsSimple(unittest.TestCase):
#     def setUp(self):
#         index = clang.cindex.Index.create()
#         self.cursor = index.parse(os.path.dirname(__file__) + r"/source_files/simple_functions.hpp").cursor

#     def test_function_procedure(self):
#         node = find_by_name(self.cursor, "procedure_forward")
#         result = FunctionInfo(node)
#         stub_lexicon(result)
#         self.assertEqual(result.name, "procedure_forward")
#         self.assertEqual(result.return_type.modification, TypeModification.NONE)
#         self.assertEqual(result.return_type.details, BasicType.VOID)
#         self.assertEqual(len(result.arguments), 0)
#         self.assertEqual(result.modification, FunctionModification.NONE)
#         self.assertEqual(result.body, None)
#         self.assertEqual(len(result.overloading), 0)
#         self.assertEqual(result.template, None)
#         self.assertTrue(result.is_declaration)
#         self.assertFalse(result.is_definition)

#     def test_function_arguments(self):
#         node = find_by_name(self.cursor, "num_forward")
#         result = FunctionInfo(node)
#         stub_lexicon(result)
#         self.assertEqual(result.name, "num_forward")
#         self.assertTrue(result.return_type.modification.is_pointer)
#         self.assertEqual(result.return_type.details, BasicType.FLOAT)
#         self.assertEqual(len(result.arguments), 2)
#         self.assertEqual(result.arguments[0].name, "x")
#         self.assertEqual(result.arguments[0].type.modification, TypeModification.NONE)
#         self.assertEqual(result.arguments[0].type.details, BasicType.DOUBLE)
#         self.assertEqual(result.arguments[0].default_value, None)
#         self.assertEqual(result.arguments[1].name, "b")
#         self.assertTrue(result.arguments[1].type.modification.is_pointer)
#         self.assertEqual(result.arguments[1].type.details, BasicType.SHORT)
#         self.assertEqual(result.arguments[1].default_value, None)
#         self.assertEqual(result.modification, FunctionModification.NONE)
#         self.assertEqual(result.body, None)
#         self.assertEqual(len(result.overloading), 0)
#         self.assertEqual(result.template, None)
#         self.assertTrue(result.is_declaration)
#         self.assertFalse(result.is_definition)

#     def test_function_default_values(self):
#         node = find_by_name(self.cursor, "num_default_forward")
#         result = FunctionInfo(node)
#         stub_lexicon(result)
#         self.assertEqual(result.name, "num_default_forward")
#         self.assertTrue(result.return_type.modification.is_reference)
#         self.assertEqual(result.return_type.details, BasicType.FLOAT)
#         self.assertEqual(len(result.arguments), 2)
#         self.assertEqual(result.arguments[0].name, "test_var")
#         self.assertEqual(result.arguments[0].type.modification, TypeModification.NONE)
#         self.assertEqual(result.arguments[0].type.details, BasicType.DOUBLE)
#         self.assertEqual(result.arguments[0].default_value, "76.0")
#         self.assertEqual(result.arguments[1].name, "a")
#         self.assertTrue(result.arguments[1].type.modification.is_pointer)
#         self.assertEqual(result.arguments[1].type.details, BasicType.DOUBLE)
#         self.assertEqual(result.arguments[1].default_value, "nullptr")
#         self.assertEqual(result.modification, FunctionModification.NONE)
#         self.assertEqual(result.body, None)
#         self.assertEqual(len(result.overloading), 0)
#         self.assertEqual(result.template, None)
#         self.assertTrue(result.is_declaration)
#         self.assertFalse(result.is_definition)

#     def test_function_body(self):
#         node = find_by_name(self.cursor, "procedure_def")
#         result = FunctionInfo(node)
#         stub_lexicon(result)
#         self.assertEqual(result.name, "procedure_def")
#         self.assertEqual(result.return_type.modification, TypeModification.NONE)
#         self.assertEqual(result.return_type.details, BasicType.VOID)
#         self.assertEqual(len(result.arguments), 0)
#         self.assertEqual(result.modification, FunctionModification.NONE)
#         self.assertEqual(len(result.overloading), 0)

#         self.assertEqual(result.template, None)
#         self.assertTrue(result.is_definition)
#         self.assertFalse(result.is_declaration)
#         # to compare platform independent
#         self.assertEqual(result.body.replace("\r\n", "\n"),
# """{
#     int a = 6*8;
#     int b = 2*a;
#     for(int i = 0; i < 5; i++)
#     {
#         a += b*i;
#     }
# }""")

#     def test_function_modification(self):
#         with self.subTest("mod_constexpt_func"):
#             node = find_by_name(self.cursor, "mod_constexpt_func")
#             result = FunctionInfo(node)
#             stub_lexicon(result)
#             self.assertEqual(result.name, "mod_constexpt_func")
#             self.assertEqual(result.return_type.modification, TypeModification.NONE)
#             self.assertEqual(result.return_type.details, BasicType.INT)
#             self.assertEqual(len(result.arguments), 1)
#             self.assertEqual(result.arguments[0].name, "a")
#             self.assertEqual(result.arguments[0].type.details, BasicType.INT)
#             self.assertEqual(len(result.overloading), 0)
#             self.assertEqual(result.template, None)
#             self.assertFalse(result.is_definition)
#             self.assertTrue(result.is_declaration)
#             self.assertTrue(result.modification.is_constexpr)

#         with self.subTest("mod_static_func"):
#             node = find_by_name(self.cursor, "mod_static_func")
#             result = FunctionInfo(node)
#             stub_lexicon(result)
#             self.assertEqual(result.name, "mod_static_func")
#             self.assertEqual(result.return_type.modification, TypeModification.NONE)
#             self.assertEqual(result.return_type.details, BasicType.INT)
#             self.assertEqual(len(result.arguments), 1)
#             self.assertEqual(result.arguments[0].name, "a")
#             self.assertEqual(result.arguments[0].type.details, BasicType.INT)
#             self.assertEqual(len(result.overloading), 0)
#             self.assertEqual(result.template, None)
#             self.assertFalse(result.is_definition)
#             self.assertTrue(result.is_declaration)
#             self.assertTrue(result.modification.is_static)

#         with self.subTest("mod_inline_func"):
#             node = find_by_name(self.cursor, "mod_inline_func")
#             result = FunctionInfo(node)
#             stub_lexicon(result)
#             self.assertEqual(result.name, "mod_inline_func")
#             self.assertEqual(result.return_type.modification, TypeModification.NONE)
#             self.assertEqual(result.return_type.details, BasicType.INT)
#             self.assertEqual(len(result.arguments), 1)
#             self.assertEqual(result.arguments[0].name, "a")
#             self.assertEqual(result.arguments[0].type.details, BasicType.INT)
#             self.assertEqual(len(result.overloading), 0)
#             self.assertEqual(result.template, None)
#             self.assertFalse(result.is_definition)
#             self.assertTrue(result.is_declaration)
#             self.assertTrue(result.modification.is_inline)

#     def test_function_namespace_return(self):
#         node = find_by_name(self.cursor, "namespace_return_func")
#         result = FunctionInfo(node)
#         stub_lexicon(result)
#         self.assertEqual(result.name, "namespace_return_func")
#         self.assertEqual(result.return_type.modification, TypeModification.NONE)
#         self.assertEqual(len(result.arguments), 1)
#         self.assertEqual(result.arguments[0].name, "a")
#         self.assertEqual(result.arguments[0].type.details, BasicType.INT)
#         self.assertEqual(len(result.overloading), 0)
#         self.assertEqual(result.template, None)
#         self.assertFalse(result.is_definition)
#         self.assertTrue(result.is_declaration)
#         self.assertEqual(result.modification, FunctionModification.NONE)
#         self.assertEqual(result.return_type.name, "typereal")
#         self.assertEqual(result.return_type.namespaces, ("test_namespace",))

#     def test_function_modification(self):
        # node = find_by_name(self.cursor, "attribute_func_1")
        # result = FunctionInfo(node)
        # self.assertTrue(result.modification.is_static)
        # self.assertEqual(result.modification, FunctionModification.NONE | FunctionModification.STATIC)

        # node = find_by_name(self.cursor, "attribute_func_2")
        # result = FunctionInfo(node)
        # self.assertTrue(result.modification.is_inline)
        # self.assertEqual(result.modification, FunctionModification.NONE | FunctionModification.INLINE)

        # node = find_by_name(self.cursor, "attribute_func_3")
        # result = FunctionInfo(node)
        # self.assertTrue(result.modification.is_constexpr)
        # self.assertEqual(result.modification, FunctionModification.NONE | FunctionModification.CONSTEXPR)

        # node = find_by_name(self.cursor, "attribute_func_4")
        # result = FunctionInfo(node)
        # self.assertTrue(result.modification.is_static)
        # self.assertTrue(result.modification.is_inline)
        # self.assertEqual(result.modification, FunctionModification.NONE
        #                  | FunctionModification.STATIC
        #                  | FunctionModification.INLINE)

