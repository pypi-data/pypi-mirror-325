==================
LitexCNC - Modules
==================

This folder and its sub-folders contains the drivers for boards. In the root folder 
the default modules are placed. Any user-specific module should be placed in a 
sub-folder, which will be automatically detected by the compiler when a user uses:

.. code:: python
    
    litexcnc install_driver

.. warning::
    
    All drivers should be preprended with ``litexcnc_`` to indicate it is part of the
    LitexCNC eco-system. Drivers without this prefix will not be automatically detected
    by the compiler and cannot be loaded by LitexCNC.
