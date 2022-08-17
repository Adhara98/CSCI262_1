from contextlib import contextmanager
import csv

@contextmanager
def salt_reader():
    with open('salt.txt', newline='') as salt_file:
        yield csv.DictReader(salt_file, delimiter=':')

@contextmanager
def salt_writer():
    with open('salt.txt', 'w+', newline='') as salt_file:
        yield csv.DictWriter(salt_file, delimiter=':', fieldnames=['Username', 'Salt'])

@contextmanager
def shadow_reader():
    with open('shadow.txt', newline='') as shadow_file:
        yield csv.DictReader(shadow_file, delimiter=':') 

@contextmanager
def shadow_writer():
    with open('shadow.txt', 'w+', newline='') as shadow_file:
        yield csv.DictWriter(shadow_file, delimiter=':', fieldnames=[
            'Username', 'PassSaltHash', 'SecurityClearance'
        ])
        
@contextmanager
def filestore_reader():
    with open('Files.store', newline='') as store_file:
        yield csv.DictReader(store_file, delimiter=':')

@contextmanager
def filestore_writer():
    with open('Files.store', 'w+', newline='') as store_file:
        yield csv.DictWriter(store_file, delimiter=':', fieldnames=[
            'Name', 'Owner', 'Classification'
        ])
