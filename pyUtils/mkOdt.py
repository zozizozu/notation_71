#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   https://github.com/eea/odfpy/blob/master/examples/
#

from odf.opendocument import OpenDocumentSpreadsheet, OpenDocumentText, load
from odf.text import P, LineBreak
from odf.table import Table, TableColumn, TableRow, TableCell


from odf.opendocument import OpenDocumentSpreadsheet
from odf.style import Style, TextProperties, TableColumnProperties, TableRowProperties, Map, TableCellProperties, ParagraphProperties
from odf.number import NumberStyle, CurrencyStyle, CurrencySymbol,  Number,  Text
from odf.text import P
from odf.table import Table, TableColumn, TableRow, TableCell


from odf.draw import Frame, Image
from odf import teletype

def mkRow(cellsContent):
	row = TableRow( stylename='ro1'  )
	for txt in cellsContent: 
		cell = TableCell( stylename='justified' )
		cLines = content.split('\n')
		for l in cLines:
			p = P(text=u""+l+"", )
			cell.addElement(p) 
	
def mkTab(tab, fileName='Notation_71'):
	textdoc = OpenDocumentSpreadsheet()
	
	s = textdoc.styles
	
	photostyle = Style(name="photostyle", family="presentation")
	photostyle.addElement(ParagraphProperties(textalign="center"))
	s.addElement(photostyle)
    
	justifystyle = Style(name="justified", family="table-cell")
	justifystyle.addElement(ParagraphProperties(textalign="center"))
	justifystyle.addElement(TableCellProperties(verticalalign="middle"))
	justifystyle.addElement(TextProperties(attributes={'fontsize':"12pt",'fontweight':"bold", 'color':"#000000" }))
	s.addElement(justifystyle)
	
	widewidth = Style(name="co1", family="table-column")
	widewidth.addElement(TableColumnProperties(columnwidth="40pt"))
	s.addElement(widewidth)
	
	widerow = Style(name="ro1", family="table-row")
	widerow.addElement(TableRowProperties(rowheight="40pt"))
	s.addElement(widerow)

	table = Table(name="Notation_71")
	
	nbCol = len(tab[0])
	for i in range(nbCol):
		table.addElement(TableColumn())
		
	dec = 0
	for iRow in range(len(tab)):
		row = TableRow( stylename='ro1'  )
		for c in tab[iRow]:
			cell = TableCell( stylename='justified' )
			content = str(c)
			if '.png' == content[-4:] :
				photoframe = Frame(width="20pt", height="20pt", x="10pt", y="10pt")
				href = textdoc.addPicture(content)
				photoframe.addElement(Image(href=href))
				cell.addElement(photoframe) 
			else:
				cLines = content.split('\n')
				for l in cLines:
					p = P(text=u""+l+"", )
					cell.addElement(p) 

			row.addElement(cell)

		table.addElement(row)

	textdoc.spreadsheet.addElement(table)
	textdoc.save(fileName+".ods")
	
	print('\nFichier '+fileName+'.ods writen\n')
	
	
	
	
