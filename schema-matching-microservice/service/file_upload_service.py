import datetime
import pandas as pd
from database.model.form import Form
from model.file_upload.file_upload_response import FileUploadResponse

class FileUploadService:

    def __init__(self):
        self.file_upload_response = FileUploadResponse

    def file_upload(self, file_uploaded):

        database_registry = Form()
        database_registry.file = file_uploaded.file
        database_registry.name = file_uploaded.name
        database_registry.uploaded_timestamp = datetime.datetime.now()
        database_registry.save()

        file_id = str(database_registry.id)
        metadata = self._metadata_extraction(file_uploaded.file)

        return self.file_upload_response(file_id, metadata)

    def _metadata_extraction(self, file):

        metadata = []
        excel_document = pd.read_excel(file)

        for column in excel_document.columns:
            metadata.append(column)

        return metadata



