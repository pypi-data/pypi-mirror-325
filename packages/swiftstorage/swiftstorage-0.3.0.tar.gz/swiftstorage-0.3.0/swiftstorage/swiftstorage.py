# Copyright (c) 2025 Sean Yeatts, Inc. All rights reserved.

from __future__ import annotations


# IMPORTS ( STANDARD )
import os
import pathlib
import shutil
from abc import ABC as Abstract
from abc import abstractmethod
from typing import Callable, List

# IMPORT ( PROJECT )
from .utilities import *


# CORE CLASS
class Storage:
    """
    Storage
    =======
    A conceptual container representing a datastore. Configurable to handle
    local or remote services ( ex. AWS S3 ).
    
    By default, Storage objects are configured as local datastores. Filepaths
    are always evaluated relative to the Storage root if a path argument is
    not specified for a given method.
    """

    # INTRINSIC METHODS
    def __init__(self, root: str, specification: StorageSpecification = None):
        self.stream = Stream()
        
        # Initialize specification
        self._specification = specification or LocalSpecification()
        self._specification.bind(self)

        # Clean up root directory
        self.root = self._delimit(root)
        self.specification.make(self.root)

    # SPECIFICATION PROPERTY
    @property
    def specification(self):
        return self._specification
    
    @specification.setter
    def specification(self, value: StorageSpecification):
        message = "A Storage object's specification is immutable. Instead, create a new Storage object."
        raise RuntimeError(message)

    # INTROSPECTIVE METHODS
    def contains(self, file: str) -> bool:
        """Checks whether a file exists within the datastore."""
        path = self.format_path(file)
        return self.specification.contains(path)
    
    def files(self, folder: str = None, subfolders: bool = False) -> list[str]:
        """Returns a list of all files contained within a folder."""
        path = self.format_path(folder) if (folder is not None) else self.root
        return self.specification.files(path, subfolders)

    def size(self, folder: str = None, subfolders: bool = False) -> tuple[float, str]:
        """Returns the total size of all files contained within a folder. Returns
        a tuple containing the result and its unit suffix."""
        path = self.format_path(folder) if (folder is not None) else self.root

        total: float = 0.0
        files = self.specification.files(path, subfolders)
        for file in files:
            total += self.specification.size(file)
        return pretty_print_bytes(total)

    # FILE MANIPULATION
    def move(self, file: str, destination: Storage, rename: str = None,
        overwrite: bool = True) -> bool:
        """Transfers a file to another datastore. The original file is NOT preserved."""
        if self.copy(file, destination, rename, overwrite):
            self.delete(file)

    def copy(self, file: str, destination: Storage, rename: str = None,
        overwrite: bool = True) -> bool:
        """Transfers a file to another datastore. The original file is preserved."""
        return self.specification.copy(file, destination, (rename or file), overwrite)

    def delete(self, file: str) -> bool:
        """Deletes a file from the datastore. Returns True if the file was removed."""
        path = self.format_path(file)
        if not self.contains(file):
            print(f"failed to locate file: {file}")
            return False
        self.specification.delete(path)
        return True
    
    # FOLDER MANIPULATION
    def make(self, folder: str) -> None:
        """Creates a new folder."""
        path = self.format_path(folder)
        self.specification.make(path)

    def purge(self, folder: str = None) -> None:
        """Deletes all files and subfolders from a folder."""
        path = self.format_path(folder) if (folder is not None) else self.root
        self.specification.purge(path)

    def remove(self, folder: str = None) -> None:
        """Removes a folder from the datastore."""
        path = self.format_path(folder) if (folder is not None) else self.root
        self.specification.remove(path)

    # DATA STREAMING METHODS
    def download(self, file: str) -> bytearray:
        """Streams a file from the datastore."""
        path = self.format_path(file)

        # [1] Check for invalid file
        if not self.contains(file):
            print(f"failed to locate file: {file}")
            return
        
        # [2] Check for invalid data
        if self.specification.size(path) == 0:
            print(f"cannot process empty file: {file}")
            return

        return self.specification.download(path)

    def upload(self, stream: bytearray, name: str, overwrite: bool = True) -> bool:
        """Streams a file to the datastore."""
        path = self.format_path(name)

        # [1] Check for invalid data
        if len(stream) <= 0:
            print("cannot process empty stream")
            return
        
        # [2] If necessary, create folder dependency
        parent = str(pathlib.Path(name).parent)
        if parent != ".":
            self.make(parent)
        
        return self.specification.upload(stream, path, overwrite)

    # HELPER METHODS
    def format_path(self, path: str) -> str:
        """Performs standard formatting operations for filepath arguments."""
        delimitted = self._delimit(path)
        return self._make_relative(delimitted)

    def _make_relative(self, path: str) -> str:
        """Formats a raw path to become relative to the Storage root."""
        return str(self.root + self.specification.delimiter + path)
    
    def _delimit(self, path: str) -> str:
        """Replaces delimiter symbols in the provided path using the correct
        symbol according to the StorageSpecification."""
        replacement: str = None
        match self.specification.delimiter:
            case '\\':
                replacement = '/'
            case '/':
                replacement = '\\'
        return path.replace(replacement, self.specification.delimiter)


# DATA STREAMING
class StreamListener:

    # INTRINSIC METHODS
    def __init__(self):
        self.callbacks: List[Callable[[float]]] = []
    
    # PUBLIC METHODS
    def connect(self, callback: Callable[[float]]) -> None:
        if not callback in self.callbacks:
            self.callbacks.append(callback)

    def disconnect(self, callback: Callable[[float]]) -> None:
        if callback in self.callbacks:
            self.callbacks.remove(callback)


class Stream:
    """The transmission channel through which a Storage object's data transfer
    operations are performed."""

    # INTRINSIC METHODS
    def __init__(self):
        self.progress:  StreamListener = StreamListener()
        self.download:  StreamListener = StreamListener()
        self.upload:    StreamListener = StreamListener()

    # PRIVATE METHODS
    def partition(self, file_size: float, increments: int = 5, limit: int = 10) -> bytes:
        """Computes the size ( bytes ) of a single streamable chunk based on
        a file's size and a specified number of divisions ( increments ). Returns
        the smaller value between the actual chunk size or the maximum allowable
        size ( limit )."""
        self.total = file_size * 2
        calculated  = file_size // increments
        allowable   = limit * 1000000   # convert megabytes --> bytes
        chunk       = min(calculated, allowable)
        return chunk
    
    def on_chunk_download(self, current: int, total: int) -> None:
        """Runs when a chunk is downloaded."""
        percent     = current / total * 100
        progress    = round(percent, 2)
        for callback in self.download.callbacks:
            callback(progress)

        # Total progress == half download progress
        for callback in self.progress.callbacks:
            callback(progress / 2)

    def on_chunk_upload(self, current: int, total: int) -> None:
        """Runs when a chunk is uploaded."""
        percent     = current / total * 100
        progress    = round(percent, 2)
        for callback in self.upload.callbacks:
            callback(progress)

    def link(self, stream: Stream) -> None:
        """Links this stream to another to track symmetrical ( download +
        upload ) operations."""
        stream.upload.connect(self._feedback)

    # PRIVATE METHODS
    def _feedback(self, percent: float) -> None:
        """Runs when a chunk from a linked Stream is uploaded. Used to report
        total progress of symmetrical ( download + upload ) operations."""

        # Normalize the range from 50-100 since we're only reporting the back
        # half of a total symmetrical operation

        normalized = (percent - 0) / (100 - 0) * (100 - 50) + 50
        for callback in self.progress.callbacks:
            callback(round(normalized, 2))


# SPECIFICATIONS
class StorageSpecification(Abstract):
    """A collection of properties and methods that define the behavior of a
    Storage object."""

    # CLASS ATTRIBUTES
    delimiter: str = "\\"   # some architectures use different delimiting characters

    # INTRINSIC METHODS
    def __init__(self):
        super().__init__()
        self.storage: Storage = None

    # SETUP METHODS
    def bind(self, storage: Storage) -> None:
        """Creates a link to the reference Storage object."""
        self.storage = storage

    # INTROSPECTIVE METHODS
    @abstractmethod
    def contains(self, file: str) -> bool: ...

    @abstractmethod
    def files(self, folder: str, subfolders: bool = False) -> list[str]: ...

    @abstractmethod
    def size(self, file: str) -> tuple[float, str]: ...

    # FILE MANIPULATION
    @abstractmethod
    def copy(self, file: str, destination: Storage, rename: str, overwrite: bool) -> bool: ...

    @abstractmethod
    def delete(self, file: str) -> None: ...

    # FOLDER MANIPULATION
    @abstractmethod
    def make(self, folder: str) -> None: ...

    @abstractmethod
    def purge(self, folder: str) -> None: ...

    @abstractmethod
    def remove(self, folder: str) -> None: ...

    # DATA STREAMING METHODS
    @abstractmethod
    def download(self, file: str) -> bytes: ...

    @abstractmethod
    def upload(self, stream: bytes, name: str, overwrite: bool) -> bool: ...


class LocalSpecification(StorageSpecification):
    """Represents a datastore that exists on the local machine."""
    
    # CLASS ATTRIBUTES
    delimiter: str = "\\"

    # INTROSPECTIVE METHODS
    def contains(self, file):
        super().contains(file)
        return os.path.exists(file)

    def files(self, folder, subfolders = False):
        super().files(folder, subfolders)
        results: list[str] = []
        if subfolders:  # we want to include subfolders
            for root, _, files in os.walk(folder):
                for file in files:
                    results.append(os.path.join(root, file))
        else:           # we don't want to include subfolders
            for file in os.listdir(folder):
                path = os.path.join(folder, file)
                if os.path.isfile(path):
                    results.append(path)
        return results

    def size(self, file):
        super().size(file)
        return os.path.getsize(file)

    # FILE MANIPULATION
    def copy(self, file, destination, rename, overwrite):
        super().copy(file, destination, rename, overwrite)

        # [1] Are we allowed to overwrite?
        if destination.contains(rename) and not overwrite:
            print(f"prevented overwrite: {rename}")
            return False

        # [2] Link to destination telemetry to report upload progress
        self.storage.stream.link(destination.stream)

        # [3] Perform transfer operation
        if (data := self.storage.download(file)):
            return destination.upload(data, rename, overwrite)
        return

    def delete(self, file):
        super().delete(file)
        print(f"deleting file: {file}")
        os.remove(file)

    # FOLDER MANIPULATION
    def make(self, folder):
        super().make(folder)
        if os.path.exists(folder):
            return
        print(f"creating folder: {folder}")
        os.makedirs(folder)
    
    def purge(self, folder):
        print(f"clearing folder: {folder}")
        super().purge(folder)
        for item in os.listdir(folder):
            path = os.path.join(folder, item)
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)

    def remove(self, folder):
        super().remove(folder)
        print(f"removing folder: {folder}")
        shutil.rmtree(folder)

    # DATA STREAMING METHODS
    def download(self, file):
        super().download(file)
        print(f"preparing file download: {file}")

        # [1] Calculate chunk size & print info
        size                    = self.size(file)
        chunk_size              = self.storage.stream.partition(size)
        formatted_file_size     = pretty_print_bytes(size)
        formatted_chunk_size    = pretty_print_bytes(chunk_size)
        print(f"file size ({formatted_file_size[1]}): {formatted_file_size[0]}")
        print(f"chunk size ({formatted_chunk_size[1]}): {formatted_chunk_size[0]}")

        # [2] Perform download operation
        try:
            print('downloading...')
            progress = 0
            datastream = bytearray()
            with open(file, 'rb') as target:
                while True:
                    if not (chunk := target.read(chunk_size)):
                        break
                    progress += len(chunk)
                    datastream.extend(chunk)
                    self.storage.stream.on_chunk_download(progress, size)
                print('download complete!')
                return datastream
        except Exception as exception:
            print(f"error downloading file: '{file}'")
            print(exception)
            return None
    
    def upload(self, stream, name, overwrite):
        super().upload(stream, name, overwrite)
        print(f"preparing file upload: {name}")
        
        # [1] Calculate chunk size & print info
        size                    = len(stream)
        chunk_size              = self.storage.stream.partition(size)
        formatted_file_size     = pretty_print_bytes(size)
        formatted_chunk_size    = pretty_print_bytes(chunk_size)
        print(f"file size ({formatted_file_size[1]}): {formatted_file_size[0]}")
        print(f"chunk size ({formatted_chunk_size[1]}): {formatted_chunk_size[0]}")

        # [2] Perform upload operation
        try:
            print('uploading...')
            progress = 0
            with open(name, 'wb') as target:
                while progress < size:
                    remaining = size - progress
                    current = min(chunk_size, remaining)
                    chunk = stream[progress:progress + current]
                    target.write(chunk)
                    progress += current
                    self.storage.stream.on_chunk_upload(progress, size)
                print('upload complete!')
                return True
        except Exception as exception:
            print(f"error uploading file: '{name}'")
            print(exception)
            return False
