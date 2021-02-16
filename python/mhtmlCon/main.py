import base64
import sys
from bs4 import BeautifulSoup


if __name__ == "__main__":

    with open(sys.argv[1], "r") as rf:

        data = rf.read()

        fields = data.split("--=_NextPart")

        i = 1
        for f in fields:
            # extract the images
            if "Content-Type: image/jpeg" in f:
                img_data = f.split("\n\n")[1]
                filename = "img"+str(i)+".png"
                i += 1
                with open(filename, "wb") as fh:
                    fh.write(base64.decodebytes(bytes(img_data, 'utf-8')))

            # store the content a plain html
            if "Content-Location: main.htm" in f:
                html_data = f.split("<!DOCTYPE html>")[1]
                with open("index.html", "w") as fh:
                    fh.write(html_data)

                # extract the text for the single steps and add the image
                # write the whole stuff to a markdown
                with open("readme.md", "w") as fh:
                    soup = BeautifulSoup(html_data, 'html.parser')
                    j = 1
                    for step in soup.find_all('p'):
                        if len(step.contents) == 2:
                            stepdesc = step.contents[1].strip()
                            fh.write(
                                "![{}](img{}.png)\n\n".format(stepdesc, j))
                            fh.write("{}\n\n".format(stepdesc))
                            j += 1
