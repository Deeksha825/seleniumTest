from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl

location = "C:/Users/Deeksha/PycharmProjects/SeleniumPractice/Test/credentials.xlsx"

workbook = openpyxl.load_workbook(location)
sheet = workbook["write"]

for r in range(1,5):
    for c in range(1,4):
        sheet.cell(row = r,column = c).value("wel","come")

workbook.save(location)
