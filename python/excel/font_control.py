# excel worksheet font control

import os

from xlwt import Workbook
import xlwt


filepath = r'C:\Codes\Snippets\sample data\output.xlsx'

book = Workbook()
sheet1 = book.add_sheet('fonr')
# book.add_sheet('Sheet 2')

xlwt.add_palette_colour("custom_colour", 0x21)
book.set_colour_RGB(0x21, 255, 255, 0)

style = xlwt.easyxf('pattern: pattern solid, fore_colour custom_colour')
sheet1.write(0, 0, 'Some text', style)

book.save(filepath)

os.startfile(filepath)
