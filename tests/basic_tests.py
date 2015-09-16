from unittest import TestCase, main as unittest_main
from textwrap import dedent

from amdfix.fixer import fixit, mod2name


def aeq(src, dst):
    src = dedent(src)
    dst = dedent(dst)
    if src != dst:
        assert src == dst, "expected:\n%s\n----\ngot:\n%s\n" % (src, dst)


class TestTests(TestCase):
    def test_mod2name(self):
        self.assertEqual(mod2name("dojo/on"), "on")
        self.assertEqual(mod2name("dojo/dom-class"), "domClass")
        self.assertEqual(mod2name("./Foo"), "Foo")

    def test_fixit(self):
        src = """
            import dojo/on

            on(window, "resize", function(){

            })

            export function() {
                // this is foo
            }
        """
        aeq(
            """
                define(
                    ["dojo/on"],
                    function(on){


                        on(window, "resize", function(){

                        })

                        return function() {
                            // this is foo
                        }
                    }
                )
            """, fixit(src)
        )


if __name__ == '__main__':
    unittest_main()
