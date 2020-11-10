import pandas as pd
import mongoengine as mongo

from database.model.form import Form
from model.metadata_update.metadata_update_request import MetadataUpdateRequest

class MetadataUpdateService:

    def metadata_update(self, metadata_update_request):

        form = Form.objects.get(id=metadata_update_request.id)
        excel_file = pd.ExcelFile(form.file)
        modified_excel_document = excel_file.parse(excel_file.sheet_names[0], names=metadata_update_request.new_metadata)

        new_indece=[]
        for index in metadata_update_request.new_metadata:
            new_indece.append(index +': 1')

        #Form.create_index(new_indece)
        Form.objects.insert(modified_excel_document)


        #User.objects.first() == None

