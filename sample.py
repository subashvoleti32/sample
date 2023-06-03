

gcloud spanner databases ddl update test-database --instance=test-instance --ddl "CREATE TABLE attribute_values (id STRING(36), attribute_id STRING(36), value STRING(250), label STRING(250), description STRING(500)) PRIMARY KEY (id)"

#update table 

gcloud spanner databases ddl update test-database --instance=test-instance --ddl="ALTER TABLE attribute_values ADD CONSTRAINT attribute_values_attribute_id_fk FOREIGN KEY (attribute_id) REFERENCES attributes (id)"
