PyPartitionSchemesParse
*****************************************************************
This program is under development to read most partitioning schemes, such as MBR, GPT, etc.

Usage-----------------
import PyPSP.py

then you use use PyPSP.parse_partition(your_rawHEX_32digit_partition_table) to analyse the data from a single partition table

Or PyPSP.parse_mbr(r'your_disk_path') to get a list of all the data from the mbr