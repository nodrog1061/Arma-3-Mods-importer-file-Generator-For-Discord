#!/usr/bin/python
import jinja2
import getWorkshop
from datetime import date
from decouple import config

def generateHtml(colectionId):

    colection= getWorkshop.getColection(colectionId)
    try:
        del colection['itemcount']
    except:
        print("no item count key")

    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "templates/modlist.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(parent_list=colection, name=config('MOD-LIST-TITLE')+str(date.today()).replace('-', ' '))  # this is where to put args to the template renderer
    
    # to save the results
    with open("results/"+config('MOD-COLLECTION-FILENAME')+".html", "w") as fh:
        fh.write(outputText)
    
    return(outputText)