from contexts import filestore_reader, filestore_writer

class FileManager(object):
    def __enter__(self):
        self.__instance__ = FileManager()
        return self.__instance__

    def __exit__(self, *args):
        pass

    def __init__(self) -> None:
        self._files = dict()
        try:
            self.__populate_files__()
        except:
            pass

    def __populate_files__(self) -> None:
        with filestore_reader() as files_reader:
            for file in files_reader:
                self._files[file['Name']] = {
                    'Name': file['Name'],
                    'Owner': file['Owner'],
                    'Classification': int(file['Classification'])
                }

    def get_files(self) -> dict:
        return self._files
    
    def exists(self, filename) -> bool:
        return filename in self._files

    def add_file(self, filename: str, owner: str, classification: int) -> None:
        assert not self.exists(filename), 'Error!!!: File already exists'

        self._files[filename] = {
            'Name': filename,
            'Owner': owner,
            'Classification': classification
        }

    def save(self) -> None:
        with filestore_writer() as files_writer:
            files_writer.writeheader()

            for data in self._files.values():
                files_writer.writerow(data)



    