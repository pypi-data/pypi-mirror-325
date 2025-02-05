import io
import zipfile
from os import PathLike
from pathlib import Path
from typing import Generator, List, Optional, Type, Union

from pipelet.exceptions.base import ProcessorStopIteration
from pipelet.exceptions.unzip_processor import UnzipError
from pipelet.log import logger_factory
from pipelet.processors.base import BaseProcessor
from pipelet.processors.file_system import (
    AbstractFileSystemManager,
    FileModeEnum,
)

logger = logger_factory()


class UnzipProcessor(
    BaseProcessor[
        Union[str, PathLike[str]], Union[str, PathLike[str]], None, None
    ],
):
    """
    A processor that handles unzipping of `.zip` files.

    This processor takes a `.zip` file as input, extracts its contents,
    and yields the paths of the extracted files. Optionally, the processor
    can delete the `.zip` file after extraction and can handle large files
    in batches.

    Attributes:
        _file_system_manager (AbstractFileSystemManager): The file system manager for file operations.
        _white_exceptions (List[Type[Exception]]): List of exceptions to bypass.
        _auto_delete (bool): Flag to delete the zip file after processing.
        _batch_size (Optional[int]): The batch size in bytes for extracting large files.
    """

    def __init__(
        self,
        file_system_manager: AbstractFileSystemManager[
            Union[str, PathLike[str]], Union[str, bytes]
        ],
        white_exceptions: Optional[List[Type[Exception]]] = None,
        auto_delete: bool = True,
        batch_size: Optional[int] = None,
    ) -> None:
        """
        Initializes the UnzipProcessor.

        Args:
            file_system_manager (AbstractFileSystemManager): The file system manager for file operations.
            white_exceptions (Optional[List[Type[Exception]]]): List of exceptions to bypass. Defaults to None.
            auto_delete (bool): Flag to delete the zip file after processing. Defaults to True.
            batch_size (Optional[int]): The batch size in megabytes for extracting large files. Defaults to None.
        """
        super().__init__(white_exceptions)
        self._file_system_manager = file_system_manager
        self._auto_delete = auto_delete
        self._batch_size = (
            batch_size * 1024 * 1024 if batch_size is not None else None
        )

    def process(
        self,
        input_data: Union[str, PathLike[str]],
    ) -> Generator[Union[str, PathLike[str]], None, None]:
        """
        Processes the given zip file and extracts its contents.

        Args:
            input_data (Union[str, PathLike[str]]): The path to the zip file to extract.

        Yields:
            Union[str, PathLike[str]]: The path to each extracted file.

        Raises:
            UnzipError: If the file is not a `.zip` file or cannot be processed.
        """
        suffix = Path(input_data).suffix
        if suffix != ".zip":
            raise UnzipError(
                input_data,
                f"File has an extension '{suffix}', expected .zip",
            )

        content = self._file_system_manager.read_file(input_data)

        if isinstance(content, (str, PathLike)):
            zip_source = content  # File path
        elif isinstance(content, (bytes, bytearray, memoryview)):
            zip_source = io.BytesIO(content)  # Flow of bytes
        else:
            raise TypeError(
                f"Unsupported content type: {type(content).__name__}. Expected str, bytes, or PathLike."
            )

        unzip_files: List[Union[str, PathLike[str]]] = []
        with zipfile.ZipFile(zip_source, FileModeEnum.READ) as zip_ref:
            for file_info in zip_ref.infolist():
                extracted_file_path = self._file_system_manager.get_path(
                    file_info.filename
                )

                with zip_ref.open(file_info, FileModeEnum.READ) as source_file:
                    if self._batch_size is not None:
                        while chunk := source_file.read(self._batch_size):
                            self._file_system_manager.append_to_file(
                                extracted_file_path, chunk
                            )
                    else:
                        self._file_system_manager.create_file(
                            extracted_file_path, source_file.read()
                        )

                unzip_files.append(extracted_file_path)

        if self.next is not None:
            for item in unzip_files:
                gen = self.next.process(item)
                try:
                    yield from gen
                except ProcessorStopIteration:
                    # Continue processing other files in the list even if one fails
                    pass
        else:
            yield from iter(unzip_files)

        # Optionally delete the zip file after extraction
        if self._auto_delete and not self.sub_next:
            self._file_system_manager.delete_file(input_data)

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(auto_delete={self._auto_delete}, "
            f"batch_size={self._batch_size})"
        )
