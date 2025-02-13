import os
import re
import shutil
import math

# Function to append to a key in the dictionary
def append_to_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)

def is_numeric_1_to_9(value):
    return value.isdigit() and all('1' <= char <= '9' for char in value)

def remove_non_numeric(text):
    # Use a regular expression to remove all non-numeric characters
    return re.sub(r'\D', '', text)
    
def convert_string_to_int(text):
    value = remove_non_numeric(text)
    intvalue = 0
    error = 0
    try:
        intvalue = int(value)
    except:
        error = 1
    return intvalue
    
def roundupdiv(numerator, denominator):
    result = math.ceil(float(numerator) / float(denominator))
    return result

def append_to_file(file_path, content_to_append):
    try:
        with open(file_path, 'ab') as file:
            content_to_append = content_to_append + '\n'
            bytestowrite = content_to_append.encode(encoding="utf-8")
            file.write(bytestowrite)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except IOError:
        print(f"An I/O error occurred while writing to {file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"Successfully removed file: {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission denied: {file_path}")
    except Exception as e:
        print(f"Error removing file {file_path}: {e}")

class logger:
    def __init__(self, filepath):
        self.filepath = filepath
        remove_file(self.filepath)
    def add_to_log(self,content_to_append):
        append_to_file(self.filepath, content_to_append)

def move_and_rename_file(src, dst,logger = None):
    if os.path.exists(src):
        try:
            shutil.move(src, dst)
            if logger != None:
                logger.add_to_log(f"	File moved and renamed from {src} to {dst}")
        except FileNotFoundError:
            if logger != None:
                logger.add_to_log(f"	The file {src} does not exist.")
        except PermissionError:
            if logger != None:
                logger.add_to_log(f"	Permission denied: cannot move {src} to {dst}.")
        except Exception as e:
            if logger != None:
                logger.add_to_log(f"	An error occurred: {e}")
    else:
        if logger != None:
            logger.add_to_log(f"  File to be moved doesn't exist: {src}")