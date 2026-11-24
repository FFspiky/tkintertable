import unittest
import tkinter as tk

from tkintertable import TableCanvas


class KeyboardBindingsTest(unittest.TestCase):
    def test_table_keeps_application_bindings(self):
        try:
            root = tk.Tk()
        except tk.TclError as exc:
            self.skipTest(str(exc))
        self.addCleanup(root.destroy)
        root.withdraw()

        keys = ("<Right>", "<Delete>", "<Tab>", "<Control-v>")
        root.bind_all("<Right>", lambda event: None, add="+")
        original = [root.bind_all(key) for key in keys]
        frame = tk.Frame(root)
        table = TableCanvas(frame)
        table.do_bindings()

        self.assertEqual([root.bind_all(key) for key in keys], original)
        for key in keys:
            self.assertTrue(table.bind(key))
        table.destroy()
        self.assertEqual([root.bind_all(key) for key in keys], original)
