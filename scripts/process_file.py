import argparse
from google.cloud import storage

def process_file(bucket_name, object_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(object_name)

    # Download the file's contents
    #contents = blob.download_as_text()
    print(f'Processing file {object_name} from bucket {bucket_name}')
    print(f'Contents: {contents}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process a file from Cloud Storage.')
    parser.add_argument('--bucket', required=True, help='The name of the GCS bucket.')
    parser.add_argument('--object', required=True, help='The GCS object name.')
    args = parser.parse_args()
    
    process_file(args.bucket, args.object)
