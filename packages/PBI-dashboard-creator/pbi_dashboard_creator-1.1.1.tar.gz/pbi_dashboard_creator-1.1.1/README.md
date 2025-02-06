# Power Bpy
Do you wish you could build dashboard with python or R, but can't because the client specifically asked for Power BI or your employer only supports publishing Power BI? Do you love love love Power BI, but wish there was a way to automatically generate parts of your dashboard to speed up your development process?          

Introducing Power Bpy, a python package that lets you create Power BI dashboards using functions 💪 instead of the point-and-click interface 🥹. Dashboards created using these functions can be opened, edited and saved normally in Power BI desktop.       

This package uses the new .pbip/.pbir format with TMDL enabled. This stores dashboards as directories of text files instead of binary files letting you version control your dashboards! 🥳 These features are still preview features, so use this with caution until there's more clarity from microsoft about what they're going to do with .pbir and tmdl.       

[![pypi Version](https://img.shields.io/pypi/v/PBI-dashboard-creator.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/PBI-dashboard-creator/)
[![PyPI Downloads](https://static.pepy.tech/badge/pbi-dashboard-creator)](https://pepy.tech/projects/pbi-dashboard-creator)
[![Codecov test coverage](https://codecov.io/gh/Russell-Shean/PBI-dashboard-creator/branch/master/graph/badge.svg)](https://app.codecov.io/gh/Russell-Shean/PBI-dashboard-creator?branch=master)

           
# Features      
Currently the package has functions that let you *automatically* 🥳 do the following:     
- Create a new dashboard
- Import data from
  - csv file stored locally 
  - csv file stored in Azure Data Lake Storage (ADLS)
  - Power BI table stored as a Tabular Model Definition Language (TMDL) file
- Add a page
- Add background images to a page
- Add visuals to a page
  - charts
  - slicers
  - cards
  - maps
  - text boxes
  - buttons

## Dependencies    
Before you can start to build power BI dashboards using this package's functions you'll need the following: 
1. python and pip installed and on path
2. git installed and on path
3. Power BI Desktop (You can create the dashboards without this, but not view them).

Power BI settings:      
You'll need to enable some preview features in Power BI Desktop. Navigate to `File` > `Options and Settings` > `Options` > `Preview features` and enable the following options:
1. Shape map visual
2. Power BI Project (.pbip) save option
3. Store Semantic Model using TMDL format
4. Store reports using enhanced metadata format (PBIR)


# Run the example
This example assumes you are on windows. All the code below should be entered in command prompt or put in a batch script.      

1. Create a new folder to store all the files you'll need.    
```batchfile
:: create a new folder
mkdir automatic_PBI_dashboards_example

:: move into the new folder
cd automatic_PBI_dashboards_example
```
2. Clone the files from github.    
```batchfile
git clone https://github.com/Russell-Shean/PBI_dashboard_creator
```
3. Activate venv.    
The following is taken from this <a href="https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/">tutorial</a>. We'll use venv to install the python package in an isolated environemnt.   
```batchfile
:: create a virtual environment
py -m venv .venv

:: activate the virtual environment
.venv\Scripts\activate

:: For extra credit, verify that venv is working
where python

```

4. Make sure pip is installed and up-to-date.    
Pip is the tool we'll use to install the package.  
```batchfile
:: install and/or upgrade pip
py -m pip install --upgrade pip

:: check version number (and confirm it's working)
py -m pip --version

```   
   
5. Install the package.
Install the package from pypi.     
```batchfile
py -m pip install PBI_dashboard_creator

```     

6. Create the example dashboard.
Run an example script to generate an example dashboard.
```batchfile

py PBI_dashboard_creator/examples/create_example_dashboard.py

```     
    
7. Open the dashboard.      
Open the dashboard to confirm everything worked. 
```
start test_dashboard/test_dashboard.pbip
```

8. Refresh data models

After Power BI opens, you'll see a banner that looks like this:
![image](https://github.com/user-attachments/assets/e71b04b0-7402-4544-9fda-ff9d898df614)      

Click `Refresh now`      

If everything worked you should have a dashboard that looks like this:     
![image](https://github.com/user-attachments/assets/70cb3771-410d-44c0-850a-dfb5d13949f2)     
![image](https://github.com/user-attachments/assets/1dd0c4ee-469d-40b2-ab20-ef3da3fcdb66)        

![image](https://github.com/user-attachments/assets/3bdab36e-5fdc-47fc-9ddf-64a69e3fbd21)       

# Next steps
The code used to generate the dashboard is stored <a href= "https://github.com/Russell-Shean/PBI-dashboard-creator/blob/main/examples/create_example_dashboard.py">here</a>      
The function documentation is stored <a href="https://pbi-dashboard-creator.readthedocs.io/en/latest/PBI_dashboard_creator.html">here</a>       

Try building your own dashboards with these functions and let me know what happens!   

# Feedback    
I welcome the following feedback:    
1. Pull requests to add features, add tests, fix bugs, or improve documentation. If the change is a major change create an issue first.
2. Issues to suggest new features, report bugs, or tell me that the documentation is confusing 😅
3. Power BI feature requests. I need help from Power BI developers who don't neccesarily have experience with python or github. I don't rely know Power BI 😅, so please feel free to suggest new features. It would be really helpful if you could include a .pbix file that has the feature or even better a git diff of the dashboard before and after the change.(Use the .pbip format)
4. Tests. I need some way to test DAX, M and TMDL for validity without using Power BI desktop. If you know of a tool I could use in Github Actions let me know! 

# Big changes coming up:    
1. This package will be renamed as powerbpy and migrated to a different github and pypi location. The version will be reset to 0.1.0
2. I will add a step-by-step explanation/tutorial for the example dashboard
3. I will deploy to conda
4. I plan to convert the functions to classes and methods
5. I will add tests and input validation. I doubt this will do anything except prevent malformed dashboard files, but stricter input validation may break some edge case uses. 
6. I will add functions to do the following:
   - Create a map with a dynamic legend
   - Add cards and slicers
   - list pages




