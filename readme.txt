MagicSquarePkg MATLAB Python Package

1. Prerequisites for Deployment 

Verify that MATLAB Runtime(R2022b) is installed.
If not, you can run the MATLAB Runtime installer.
To find its location, enter
  
    >>mcrinstaller
      
at the MATLAB prompt.
NOTE: You will need administrator rights to run the MATLAB Runtime installer. 

Alternatively, download and install the Windows version of the MATLAB Runtime for R2022b 
from the following link on the MathWorks website:

    https://www.mathworks.com/products/compiler/mcr/index.html
   
For more information about the MATLAB Runtime and the MATLAB Runtime installer, see 
"Distribute Applications" in the MATLAB Compiler SDK documentation  
in the MathWorks Documentation Center.

Verify that a Windows version of Python 2.7, 3.8, 3.9, and/or 3.10 is installed.

2. Installing the MagicSquarePkg Package

A. Change to the directory that contains the file setup.py and the subdirectory 
MagicSquarePkg. If you do not have write permissions, copy all its contents to a 
temporary location and change to that directory.

B. Execute the command:

    python setup.py install [options]
    
If you have full administrator privileges, and install to the default location, you do 
not need to specify any options. Otherwise, use --user to install to your home folder, or 
--prefix="installdir" to install to "installdir". In the latter case, add "installdir" to 
the PYTHONPATH environment variable. For details, refer to:

    https://docs.python.org/2/install/index.html


3. Using the MagicSquarePkg Package

The MagicSquarePkg package is on your Python path. To import it into a Python script or 
session, execute:

    import MagicSquarePkg

If a namespace must be specified for the package, modify the import statement accordingly.
