========
ADwin.py
========

This is the python wrapper module for the ADwin API to communicate with ADwin-systems.

Requirements, downloadable at `ADwin.de <https://www.adwin.de/de/download/download.html>`_:

*    Linux / Mac: libadwin.so
*    Windows: adwin32.dll / adwin64.dll

**Changelog**

+-----------+----------------------------------------------------------------+
| Version   | Changes                                                        |
+===========+================================================================+
| 0.20.0    | new function: Get_Lost_Events()                                |
+-----------+----------------------------------------------------------------+
| 0.19.0    | new function: Get_Known_Deviceno()                             |
+-----------+----------------------------------------------------------------+
| 0.18.1    | setup: distutils -> setuptools, egg -> wheel                   |
+-----------+----------------------------------------------------------------+
| 0.18.0    | new mode: useNumpyArrays                                       |
+-----------+----------------------------------------------------------------+
| 0.17.2    | minor enhancements                                             |
+-----------+----------------------------------------------------------------+
| 0.17.1    | bugfix File2Data()                                             |
+-----------+----------------------------------------------------------------+
| 0.17.0    | new function: SanitizeFloatingPointValues()                    |
+-----------+----------------------------------------------------------------+
| 0.16.4    | bugfix Data_Type() T12/ADwinX                                  |
+-----------+----------------------------------------------------------------+
| 0.16.3    | ctypes.WinDLL() needs full path;                               |
|           | additional functions for ADwinX                                |
+-----------+----------------------------------------------------------------+
| 0.16.2    | bugfix                                                         |
+-----------+----------------------------------------------------------------+
| 0.16.1    | bugfix                                                         |
+-----------+----------------------------------------------------------------+
| 0.16.0    | Changed license to Apache V2;                                  |
|           | CODING cp1252 added in example[_python3].py;                   |
|           | changed bas_demos to python3 and Qt5                           |
+-----------+----------------------------------------------------------------+
| 0.15      | bugfixes;                                                      |
|           | new functions for datatype double;                             |
|           | Data_Type(), Data2File(), File2Data();                         |
|           | renamed Get_Last_Error_Text() to Get_Error_Text();             |
|           | changed returnvalue from Processor_Type to str (1010 -> "T10");|
|           | div pep8-style changes, several improvements, winreg-key;      |
|           | examples reworked                                              |
+-----------+----------------------------------------------------------------+
| 0.14      | bugfix GetData_String()                                        |
+-----------+----------------------------------------------------------------+
| 0.13      | new function: GD_Transsize()                                   |
+-----------+----------------------------------------------------------------+
| 0.12      | bugfixes                                                       |
+-----------+----------------------------------------------------------------+
| 0.11      | bugfixes                                                       |
+-----------+----------------------------------------------------------------+
| 0.10      | bas_demo7: float() instead of QString.toDouble();              |
|           | examples: c_int32 instead of c_long;                           |
|           | new functions: Clear_Data(), Retry_Counter()                   |
+-----------+----------------------------------------------------------------+
| 0.9       | adwin32.dll / adwin64.dll depending on the python-version;     |
|           | bas_demos: str() instead of QtCore.QString.number();           |
|           | bas_dmo3: bugfix div/0                                         |
+-----------+----------------------------------------------------------------+
| 0.8       | ctypes.c_int32 instead of ctypes.c_long                        |
+-----------+----------------------------------------------------------------+
| 0.7       | bugfix Windows-registry;                                       |
|           | python3-support for Windows                                    |
+-----------+----------------------------------------------------------------+
| 0.6       | bugfix GetData_String()                                        |
+-----------+----------------------------------------------------------------+
| 0.5       | removed Get- and Set_Globaldelay();                            |
|           | bugfixes Fifo_Count() and Fifo_Empty()                         |
+-----------+----------------------------------------------------------------+
| 0.4       | new class-attribute ADwindir;                                  |
|           | bas_demos (1, 2, 3, 7) created;                                |
|           | indenting fixed                                                |
+-----------+----------------------------------------------------------------+
| 0.3       | one file for booth python-versions (2/3);                      |
|           | no exception if Test_Version() fails                           |
+-----------+----------------------------------------------------------------+
| 0.2       | usage of the module ctypes;                                    |
|           | class ADwin;                                                   |
|           | python3-support for linux                                      |
+-----------+----------------------------------------------------------------+
| 0.1       | first issue                                                    |
+-----------+----------------------------------------------------------------+
