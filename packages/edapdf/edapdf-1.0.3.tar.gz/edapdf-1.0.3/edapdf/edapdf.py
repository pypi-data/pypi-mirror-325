"""
Defines EDAPresentation class.
"""

from tempfile import NamedTemporaryFile

from fpdf import FPDF, Align
from matplotlib.figure import Figure
from matplotlib.pyplot import savefig
import pandas as pd
import polars as pl
from great_tables import GT


class EDAPDF(FPDF):
    """
    PDF class that inherits from FPDF and automatically
    sets certain options.
    """

    _title: str
    _header_flag: bool

    def __init__(self, title: str = ""):
        self._title = title  # Initialize _title properly
        super().__init__(orientation="landscape", unit="mm", format="A4")
        self._header_flag = False
        self._add_title_page()
        self._header_flag = True

    def _add_title_page(self):
        # Calculate center position
        self.set_font(
            "helvetica", style="B", size=30
        )  # Calculate size of cell containing title
        text_width = self.get_string_width(self._title)
        x = (self.w - text_width) / 2  # Center horizontally
        y = self.h / 2  # Center vertically

        # Set position and add text
        self.add_page()
        self.set_xy(x, y)
        self.cell(text_width, 10, self._title, align="C")
        self._reset_font()

    def _reset_font(self):
        self.set_font("helvetica", size=12)

    def header(self):
        if self._header_flag:
            # Setting font: helvetica bold 15
            self.set_font("helvetica", style="B", size=12)
            # Printing title:
            self.cell(w=None, h=None, text=self._title)
            # Performing a line break:
            self.ln(20)
            self.set_font("helvetica", size=12)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", size=8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def add_figure(self, figure: Figure, title: str = "Figure"):
        self.add_page()
        self.set_font("helvetica", size=20, style="B")
        text_width = self.get_string_width(title)
        x = (self.w - text_width) / 2  # Center horizontally
        y = 20  # Center vertically
        self.set_xy(x, y)
        self.cell(w=text_width + 4, h=10, text=title, align="C")
        self.ln(17)
        self._reset_font()

        with NamedTemporaryFile(suffix=".png") as tempfile:
            figure.set_size_inches(6, 4)
            figure.savefig(tempfile)
            self.image(tempfile.name, x=Align.C)
        self._reset_font()

    def add_table(self, table: pd.DataFrame | pl.DataFrame, title: str = "Table"):
        self.add_page()
        self.set_font("helvetica", size=20, style="B")
        text_width = self.get_string_width(title)
        x = (self.w - text_width) / 2  # Center horizontally
        y = 20  # Center vertically
        self.set_xy(x, y)
        self.cell(w=text_width + 4, h=10, text=title, align="C")
        self.ln(17)
        self._reset_font()
        with NamedTemporaryFile(suffix=".png") as tempfile:
            gt = GT(table)
            gt.save(tempfile.name, scale=5)
            self.image(tempfile.name, x=Align.C, h=101.6, keep_aspect_ratio=True)
        self.set_font("helvetica", size=12)
