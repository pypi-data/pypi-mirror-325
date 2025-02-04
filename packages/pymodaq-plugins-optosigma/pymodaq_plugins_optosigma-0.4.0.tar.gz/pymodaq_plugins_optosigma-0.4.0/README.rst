pymodaq_plugins_optosigma
#########################

.. the following must be adapted to your developed package, links to pypi, github  description...

.. image:: https://img.shields.io/pypi/v/pymodaq_plugins_optosigma.svg
   :target: https://pypi.org/project/pymodaq_plugins_optosigma/
   :alt: Latest Version

.. image:: https://readthedocs.org/projects/pymodaq/badge/?version=latest
   :target: https://pymodaq.readthedocs.io/en/stable/?badge=latest
   :alt: Documentation Status

.. image:: https://github.com/NanoQM/pymodaq_plugins_optosigma/workflows/Upload%20Python%20Package/badge.svg
   :target: https://github.com/NanoQM/pymodaq_plugins_optosigma
   :alt: Publication Status

.. image:: https://github.com/NanoQM/pymodaq_plugins_optosigma/actions/workflows/Test.yml/badge.svg
    :target: https://github.com/NanoQM/pymodaq_plugins_optosigma/actions/workflows/Test.yml


Set of OptoSigma controllers for PyMoDAQ that includes the following controllers: {GSC-02C, RMC-102, SHRC203, SBIS26}. 
Each controller is in a seperate module and can be used independently.


Authors
=======

* Amelie Deshazer
* Daichi Kozawa


Instruments
===========

Below is the list of instruments included in this plugin

Actuators
+++++++++

* **GSC-02C**: controller of GSC 2 Axis Stage Controller
* **RMC-102**: controller of RMC-102 Remote Micrometer Controller
* **SHRC203**: controller of SHRC203 3 Axis Stage Controller   
* **SBIS26**: controller of SBIS26 Driver Integrated Motorized Stage


Installation instructions
=========================

* Tested with PyMoDAQ’s version: 4.4.7
* **RMC-102 USB Driver(for Windows 7/8.1/10)32/64bit *for Remote Acutuator**
      Install through OptoSigma’s website: 
      https://jp.optosigma.com/en_jp/software__usb
