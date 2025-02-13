.. venco.py installation documentation file, created on February 11, 2020
    Licensed under CC BY 4.0: https://creativecommons.org/licenses/by/4.0/deed.en

.. _installation:

Installation and Setup
===================================


Requirements and boundary conditions
-------------------------------------

venco.py runs on Unix and Windows-based operating systems. It requires an
installed version of Python and the package, dependency and environment
management tool conda as well as internet access for setting up the
environment for downloading the required packages. Versioning is based on 
semantic versioning (X.Y.Z) changes versioning system via git-labels. You can 
use venco.py as a user (installation from PyPI) or contribute to the
codebase and documentation as developer (checking out the repository from 
gitlab). Depending on that choice the installation and setup differs.

.. image:: ../figures/application_context.drawio.png
	:width: 600
	:align: center

Installation for users
-------------------------------------
As a user, you will apply venco.py for answering analytical questions. Thus,
you're mainly interested in applying venco.py's built-in features and
functions. On this level, you will not change the codebase within the venco.py
core class objects - of course you can write your own data processing routines
around those functions.

Install using the environment management system conda (or mamba), open a
conda console, create a new environment and activate it by typing::

	conda create -n <your environment name> python
	conda activate <your environment name>

Install venco.py from the Python Package Index PyPI::

	pip install vencopy

Navigate to a parent directory where you want to create your venco.py user
folder in and type::

	python -m vencopy

You will be prompted for a userfolder name, type it and hit enter. Your
venco.py user folder will now be created. It will look like this:

::

    FOLDERNAME
    ├── config
    │   └── user_config.yaml.default
    ├── output
    │   ├── dataparser
    │   ├── gridmodeller
    │   ├── flexestimator
    │   ├── diarybuilder
    │   ├── profileaggregator
    │   └── postprocessor
    ├── input
    └── run.py

The user_config in the config folder is the main interface between the user and
the code. In order to learn more about them, check out our tutorials. For this
you will not need any additional data as an extract of a suitable database is provided at
https://gitlab.com/dlr-ve/esy/vencopy/vencopy/-/blob/joss/tutorials/data_sampling/MiD17.csv?ref_type=heads
This is an anonymised extract of the MiD B2 dataset. 

The dataset "Mobilität in
Deutschland" (German for mobility in Germany), can be requested here from the
clearingboard transport:
https://daten.clearingstelle-verkehr.de/order-form.html 
Alternatively, you can use the tool in 
conjunction with any other national travel survey data or output
of transport models which contains at least the following variables:

- Person ID: A unique identifier for each individual or vehicle or household.
- Trip ID: A distinct identifier for each trip.
- Timestamps: Precise hours of the day indicating the beginning and conclusion of a trip.
- Trip Purpose: The underlying motivation or intention for embarking on a particular journey.
- Distance: The total length in km covered during the trip.

To be able to run the following steps you need to have mobility data at hand.
If you have the "Mobilität in Deutschland" dataset or any other NTSs for which venco.py has been already adapted you can continue with the following instructions.
Alternatively, you can try out the tutorials (see :ref:`start`).

Now duplicate the user_config.yaml.default file and rename it to user_config.yaml.
Please navigate to your user_config.yaml and set the vencopy_root (user_config["global"]["absolute_path"]["vencopy_root"]) 
to the absolute path of the cloned vencopy repository.
Now enter the path to your local MiD STATA folder, it will end on .../B2/STATA/.
Now open your user folder in an IDE, configure your interpreter (environment) and type::

	python run.py

In the vencopy.log file which is generated for every run you will find detailed information about the execution of the model, serving as a diagnostic tool,
progress tracker, and audit trail. Its primary purpose is to record events, errors, and outputs during the execution of vencopy. 

Installation for developers
-------------------------------------

This part of the documentation holds a step-by-step installation guide for
venco.py if you want to contribute. You need git installed before installation.

1.  Navigate to a folder to which you want to clone venco.py. Clone the
    repository to your local machine using::

        git clone https://gitlab.com/dlr-ve/esy/vencopy/vencopy.git

2.  Set-up your environment. For this, open a conda console, navigate to the
    folder of your venco.py repository and enter the following command ::

	    conda create -n <your environment name> python
	    conda activate <your environment name>
        pip install -e .

3.  Now duplicate the user_config.yaml.default file and rename it to user_config.yaml.
    Navigate to your user_config.yaml and set the vencopy_root (user_config["global"]["absolute_path"]["vencopy_root"]) 
    to the absolute path of the vencopy folder in the cloned vencopy repository.
    Configure your config files if you want to use absolute links. This is only
    needed if you want to reference your own local data or want to post-process
    venco.py results and write them to a model input folder somewhere on your
    drive. You will find your config file in your repo under
    /config/dev_config.yaml and config/user_config.yaml. Input filenames are
    set to the example files which are provided with the repo.

4.  You're now ready to run venco.py for the first time by typing::

        python run.py

