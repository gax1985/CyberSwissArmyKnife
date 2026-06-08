
from pathlib import Path
import sys
import json
class TheFileIngester():
    def __init__(self): # This class is responsible for ingesting files from the local filesystem.
        pass

    def the_reader(self,file_path):
        print(f" ... As we speak , I am extracting knowledge from the target payload [*]...")

        ## Let us now define the folder location, according to the operating system where this application is ran :
        target_file = Path(file_path)

        ## ... an IF statement is added here to address the possibility of the file location being empty, by informing
        ## the user :

        if not target_file.exists():
            print(f"[-] FATAL !!! ALARM !!! This location is ... nada !")
            ### ... here, we issue a call to the system to exit the application :
            sys.exit(1)

        ## ... the previous line would have ended things really, but it is a form of habit for me, since it was an IF
        ## statement. The .read_text() function opens the file, and its contents gets assigned to the variable, with
        ## 'UTF-8' encoding :
        else:
            file_content = target_file.read_text(encoding="utf-8")

        ## ... finally, the following line returns the contents of the file :
        return file_content

# Next, let us create TheFileIngester Class :
# Ingester = TheFileIngester()
# precious_contents = Ingester.the_reader(path_found)


