from dataclasses import dataclass

@dataclass

class DataIngestionArtifact:
    data_zip_file_path:str #these two are return types of my components
    feature_store_path:str