import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
workbook = Workbook("processed/text_detected/text_detected.txt")
workbook.save("processed/load_json/output.json")
jpype.shutdownJVM()

with open('processed/text_detected/text_detected.txt') as f:
    contents = f.read

