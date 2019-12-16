import os
from PyPDF2 import PdfFileReader, PdfFileWriter
# wp = 'E://Paper/RDF-All/'
# targetPath = "E://Paper/target"

def show_files(path, all_files):
    file_list = os.listdir(path)
    
    for file in file_list:
        cur_path = os.path.join(path, file)
        if os.path.isdir(cur_path):
            show_files(cur_path, all_files)
        else:
            all_files.append(cur_path.replace("\\", "/"))

    return all_files

# allFiles = show_files(wp, [])


def outputToFile(fileName, allFiles):
    with open(fileName, "wb+") as outputFile:
        out_pdf = PdfFileWriter()
        for file in allFiles:
            if not (file.__contains__("FrontMatter")):
                sc_pdf = PdfFileReader(open(file, 'rb'))
                out_pdf.addPage(sc_pdf.getPage(0))
                print(file)
        out_pdf.write(outputFile)

if __name__ == '__main__':
    list = ['./vldbPapers/pvldb7','./vldbPapers/pvldb8','./vldbPapers/pvldb9','./vldbPapers/pvldb10','./vldbPapers/pvldb11','./vldbPapers/pvldb12']
    i = 7
    for dir in list:
        volFiles = show_files(dir, [])
        fileName = "vldbAbstract/pvldb" + str(i) + ".pdf"
        outputToFile(fileName, volFiles)
        print(i)
        i = i +1