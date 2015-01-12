DNACloud README
========================================================

-This software take any computer file as input and provides you its corresponding DNA string as well as small chunks of DNA String of length 117 which can be easily synthesized.

-It also decodes the original file from the DNA string or DNA list. Since this conversion process is quiet heavy it comes with a build in estimator which approximates the physical memory used by the software when converting a particular file.

-This software is developed by [`Shalin Shah`](www.guptalab.org/shalinshah) at Laboratory of Natural Information Processing, DA-IICT (Gupta Lab). It has been presented as a poster at [FNANO'14](http://www.cs.duke.edu/FNANO/). 

You could report bugs and feedback at :- `dnacloud@guptalab.org`                     
To know more you can also visit our website :- `www.guptalab.org/dnacloud`                        
You can also find our extended paper on [Cornell's archive](arxiv.org) :- `http://arxiv.org/pdf/1310.6992v2.pdf`        

**(C) - 2013 Gupta Lab**


Build Instructions
---------------------------------------------------------

**a) For MAC/Linux :-** 

- Download the source code(as .zip) from git or clone it using following command :-

        git clone https://github.com/shalinshah1993/DNACloud.git

- Open terminal and move to DNACloud directory containing `dnacloud.sh` file. Try to run this shell file using following command :-

        sh dnacloud.sh

- If it doesn't work showing error that barcode module or wx module not found then you will have to first download python distribution of those modules.

- You can either install them using pip or by downloading their .zip distributions(containing setup.py file) available.

- To install pip type following command or download its distribution folder from internet and run `python setup.py instal`. Note that pip is payloaded with python if you install python using brew:- 

        sudo apt-get install python-pip (Linux)
        sudo easy_install pip or brew install python (MAC OSX)

- After installing pip you should install wxpython 32 bit v2.8 using following command. Make sure you are using python of 32bit or force 64bit python interpreter to run in 32 bit mode.

	sudo pip install wxpython==2.8 or sudo apt-get install python-wxgtk3.0-dev

- Lastly, you need to install Whitie's pyBarcode module which is available [here](https://bitbucket.org/whitie/python-barcode/get/dd1a7c7ddf05.zip "here") or [here](https://bitbucket.org/whitie/python-barcode "here") .
To install it simply download it as .zip and run `sudo apt-get install python-setuptools` and `sudo python setup.py install` in this directory.

**b) For Windows :-**

- Download the command line tools for git hub and setup file for pip. Install them and set their path as environment variable. Once this is done you can follow the same process as above using CMD.

- Hope that helps you to install DNACloud. In case any doubt please mail @ `dnacloud@guptalab.org`


Folder Info:-
---------------------------------------------------------

 .temp - Contains temporary files which can be cleaned from the software.
 
 database - This folder contains all the encoded DNA Lists and your preferences. Please do not change or delete these files.
 
 source - All the python files. `MainFrame.py` is the main GUI file.
 
 scripts - Contains scripts to convert software to `.exe` and `.app` file.
 
 help - Contains PDF files for `CREDITS` and `USER MANUAL`. You may refer the last document to understand the software.
 
 icons - Contains all the icons used in the software.
 
 Create exe:-
 ---------------------------------------------------------
 1) Copy barcode and PIL folder into source folder
 
 2) Copy DNAicon.ico file from icon folder to source folder
 
 3) Change directory to scripts
  
 4) Copy exe_app_converterScript.py into source folder
 
 5) run "python exe_app_converterScript.py install" command in command promt run as administrator
 
 6) change directory to newly created directory called build
 
 7) change the name of the folder (present there) to source 
 
 8) copy all the folders and files except source folder from main source code to this directory
 
