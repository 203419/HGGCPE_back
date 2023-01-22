import os, datetime, time
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from PIL import Image


class PDF(FPDF):
    def __init__(self, usuario):
        super().__init__()
        self.add_page()
        self.set_author(usuario)
        self.set_top_margin(25)
        self.set_right_margin(20)
        self.set_left_margin(20)
        self.set_auto_page_break(True, 15)
        self.logo = False
        self.y = 20

    def reset_y(self):
        if self.y > 240:
            self.add_page()
            self.y = 20
        
    def add_title(self, title):
        self.set_font("Arial", 'B', size=18)
        if self.logo == True:
            self.set_x(40)
            self.cell(self.w-40, 5, txt=title, ln=1, align="L")
        else:
            self.cell(self.w , 5, txt=title, ln=1, align="L")
        self.y += 10

    def add_subtitle(self, title):
        self.set_font("Arial", 'B', size=14)
        self.set_x(20)
        self.cell(self.w , 5, txt=title, ln=1, align="L")
        self.y += 5

    def add_text(self, text):
        self.set_font("Arial", size=12)
        y = self.y

        for line in text.splitlines():
            self.set_xy(20, y)
            self.write(6, line)
            y += 7

        self.y = y + 16
        self.reset_y()

    def add_logo(self, file):
        self.image(file, 15, 15, 22, 22)
        self.logo = True

    def add_image(self, file):
        img = Image.open(file)
        
        if img.width >= img.height:
            size = 80/img.width
        else: 
            size = 60/img.height

        x = (self.w - (img.width * size))/2
        y = self.y

        self.image(file, x, y, (img.width * size), (img.height * size))
        self.y += (img.height * size) + 10

        self.reset_y()
        
    def add_table(self, data):
        self.set_font("Arial", size=11)
        col_width = self.get_string_width(data[1][1]) + 6
        row_height = 10

        x = (self.w - (col_width*len(data[0])))/2
        y = self.y
        
        for row in data:
            for item in row:
                self.set_xy(x,y)
                self.cell(col_width, row_height, txt=str(item), border=1)
                x+=col_width
            self.ln()
            x = (self.w - (col_width*len(data[0])))/2
            y +=row_height

        self.y = y + 11
        self.reset_y()
