import struct

def type_check(B):
    partition_types = [
    ['00', 'Empty or Unused'],
    ['01', 'FAT12'],
    ['02', 'XENIX root'],
    ['03', 'XENIX usr'],
    ['04', 'FAT16 (Small)'],
    ['05', 'Extended Partition'],
    ['06', 'FAT16'],
    ['07', 'NTFS / HPFS / exFAT'],
    ['08', 'AIX bootable'],
    ['09', 'AIX data'],
    ['0A', 'OS/2 Boot Manager'],
    ['0B', 'FAT32 (CHS)'],
    ['0C', 'FAT32 (LBA)'],
    ['0E', 'FAT16 (LBA)'],
    ['0F', 'Extended Partition (LBA)'],
    ['10', 'OPUS'],
    ['11', 'Hidden FAT12'],
    ['12', 'Compaq diagnostcs'],
    ['14', 'FAT16 (LBA)'],
    ['16', 'Hidden FAT16'],
    ['17', 'Hidden NTFS'],
    ['1B', 'Hidden FAT32'],
    ['1C', 'Hidden FAT32 (LBA)'],
    ['1E', 'Hidden FAT16 (LBA)'],
    ['24', 'NEC DOS'],
    ['39', 'Plan 9'],
    ['3C', 'PartitionMagic recovery'],
    ['40', 'Venix 80286'],
    ['41', 'Linux/MINIX'],
    ['42', 'Linux Swap'],
    ['43', 'Linux Ext2/Ext3 (Old format)'],
    ['44', 'Linux Ext2/Ext3 (New format)'],
    ['83', 'Linux ext FS'],
    ['84', 'Linux swap / Solaris'],
    ['8E', 'Linux LVM'],
    ['93', 'Amoeba'],
    ['A0', 'IBM Thinkpad hidden'],
    ['A5', 'FreeBSD'],
    ['A6', 'OpenBSD'],
    ['A8', 'Mac OS X'],
    ['A9', 'NetBSD'],
    ['AF', 'Mac OS X HFS+'],
    ['B7', 'BSDI'],
    ['B8', 'Boot Manager'],
    ['BE', 'Solaris Boot Partition'],
    ['BF', 'Solaris / OpenIndiana'],
    ['C0', 'NTFS Boot Partition'],
    ['C1', 'FreeBSD boot'],
    ['C4', 'TrueCrypt volume'],
    ['C7', 'Windows 7 recovery'],
    ['D1', 'OpenBSD bootstrap'],
    ['D3', 'GParted'],
    ['D5', 'FreeBSD UFS2'],
    ['D6', 'Solaris (x86) partition'],
    ['D7', 'OpenBSD partition'],
    ['E1', 'Linux RAID'],
    ['E2', 'Linux LVM2'],
    ['E3', 'Linux EVMS'],
    ['E4', 'MS-DOS 6.0'],
    ['E5', 'OpenDOS'],
    ['E6', 'OS/2 Boot Manager'],
    ['E7', 'Non-OS/2 Boot Manager'],
    ['EB', 'FAT16 (LBA) (exFAT)'],
    ['EC', 'Windows 98 SE'],
    ['EE', 'GPT Protective'],
    ['EF', 'EFI System Partition'],
    ['F0', 'Microsoft Reserved'],
    ['F2', 'Linux Swap (used by newer Linux versions)'],
    ['F4', 'Microsoft Windows recovery partition'],
    ['F6', 'HPFS/NTFS'],
    ['F7', 'HPFS/NTFS (Boot)'],
    ['F8', 'OEM proprietary'],
    ['F9', 'BSD']
    ]
    for i in range(0, len(partition_types)):
        if B == partition_types[i][0]:
            return partition_types[i][1]
        else:
            return "Unknow"

def parse_partition(raw):
    if raw == "00000000000000000000000000000000":
        return "Empty"
    elif len(raw) != 32:
        raise ValueError("Unexpected Partition Table Length")

    boot_flag = raw[:2]
    if boot_flag not in ("80", "00"):
        raise ValueError(f"Unexpected Partition Table Header: {boot_flag}")
    
    return {
        "Bootable": boot_flag == "80",
        "Start Cylinder": raw[2:4],
        "Start Head": raw[4:6],
        "Start Sector": raw[6:8],
        "Partition Type Code": raw[8:10],
        "Partition Type": type_check(raw[8:10]),
        "End Cylinder": raw[10:12],
        "End Head": raw[12:14],
        "End Sector": raw[14:16],
        "First Sector": struct.unpack('<I', bytes.fromhex(raw[16:24]))[0],
        "Total Sectors": struct.unpack('<I', bytes.fromhex(raw[24:32]))[0]
    }

def read_raw_bytes(disk_path, size=512):
    with open(disk_path, 'rb') as disk:
        return disk.read(size)

def read_raw_hex(disk_path, size=512):
    return read_raw_bytes(disk_path, size).hex()

def parse_mbr(disk_path):
    raw_hex = read_raw_hex(disk_path)
    return {
        "Boot Code": raw_hex[:880],
        "Disk Signature": raw_hex[880:892],
        "Partition Table": raw_hex[892:1020],
        "MBR Signature": raw_hex[-4:],
        "Partitions": [
            parse_partition(raw_hex[892:924]),
            parse_partition(raw_hex[924:956]),
            parse_partition(raw_hex[956:988]),
            parse_partition(raw_hex[988:1020])
        ]
    }
