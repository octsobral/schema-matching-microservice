class FileUploadResponse:

    def __init__(self, id, metadata):

        self.id = id
        self.metadata = metadata

    def to_json(self):
        return self.__dict__
