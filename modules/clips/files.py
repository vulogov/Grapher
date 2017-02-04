__author__  =  'Vladimir Ulogov'
__version__ = 'v0.1.0'

import clips

fs_check_file_read_clips="(deffunction fs_check_file_read (?str ) (python-call fs_check_file_read ?str ))"
fs_check_file_write_clips="(deffunction fs_check_file_write (?str ) (python-call fs_check_file_write ?str ))"
fs_check_directory_clips="(deffunction fs_check_directory (?str ) (python-call fs_check_directory ?str ))"


def fs_check_file_read(_str):
    if globals()["m_globals"]["check_file_read"](str(_str)) == True:
        return clips.Symbol('TRUE')
    return clips.Symbol('FALSE')

def fs_check_file_write(_str):
    if globals()["m_globals"]["check_file_write"](str(_str)) == True:
        return clips.Symbol('TRUE')
    return clips.Symbol('FALSE')

def fs_check_directory(_str):
    if globals()["m_globals"]["check_directory"](str(_str)) == True:
        return clips.Symbol('TRUE')
    return clips.Symbol('FALSE')