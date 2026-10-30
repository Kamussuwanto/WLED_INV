This note describe how to clone this project (einv_leddrawer) from 
Github into local a local computer repository and flash ESP32S3 firmware.

*copy dot ino file into arduino IDE. Press boot button while 
plug-in usb into computer then release the boot button, and click
upload from Arduino IDE. Wait until finish

*from WSL: 
…or create a new repository on the command line
echo "# einv_leddrawer1" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Kamussuwanto/einv_leddrawer.git
git push -u origin main
alt: ---

…or push an existing repository from the command line
git remote add origin https://github.com/Kamussuwanto/einv_leddrawer.git
git branch -M main
git push -u origin main
alt:---

...or


*Set up a virtual environment:
python3 -m venv myenv
source myenv/bin/activate