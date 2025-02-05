# OARepo model builder tests
Plugin for oarepo-model-builder to generate 
test files and add test dependencies.
The record service and its rest api are covered for now. Tests read, write,
update, delete and search operations.The tests use automatically generated metadata in {model_name}/data/sample_data.yaml file to create records and upload them as fixtures.

Resource test:
* `test_get_item`: Tries to use the api to retrieve non existing and existing record. Should fail on the first task and success on second.
* `test_create`: Tries to use the api to create a list of records. Also tries to use unauthorized client to do so, which should fail with http code 403. Then the test tries to retrieve the records and checks whether they contain the same metadata that they were uploaded with.
* `test_listing`: Tries a get call on the base url to retrieve all saved records. Checks whether the correct number of records is retrieved.
* `test_update`: Tries to update non-existing record. Then updates an existing record and checks whether the metadata are correctly updated and revision_id incremented.
* `test_delete`: Tries to delete non-existing record. Then tries to delete an existing one and checks whether the get call return 410 error http code. Also checks that unauthorized client can't delete.
* `test_search`: Finds all metadata fields generated in the test data. Then tries search based on values in the fields and checks whether at least one record with the same field value is returned. Tries search based on created time, with correct time, wrong time and as a facet.

The service tests are analogous, they only bypass the api and use the expected service methods directly.

## Installation

### model.yaml

```yaml
model:
 plugins:
  packages:
   - oarepo-model-builder-tests
```
### command line
```bash
pip install oarepo-model-builder
pip install oarepo-model-builder-tests
```
