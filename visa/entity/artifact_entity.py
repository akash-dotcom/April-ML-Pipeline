from collections import namedtuple



DataIngestionArtifact=namedtuple("Data_Ingestion_Artifact",
                                   ["train_file_path","test_file_path",
                                   "is_ingested","message"])

DataValidationArtifact=namedtuple("DataValidationArtifact",
                                  ["schema_file_path","is_validated","message"])