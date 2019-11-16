from google.cloud import storage

##放置金鑰位置
storage_client = storage.Client.from_service_account_json(r'db103head.json')
##storage名稱
bucket_name = 'db103_head'


# 上傳資料(storage名稱,來源名稱,目標名稱,金鑰)
def upload_blob_gpx(source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    ##放置金鑰位置
    storage_client = storage.Client.from_service_account_json(r'db103head.json')
    ##storage名稱
    bucket_name = 'db103_head_gpx'
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


# 顯示資料項目(storage名稱,金鑰)
def list_blobs_gpx():
    blobs_list=[]
    """Lists all the blobs in the bucket."""
    ##放置金鑰位置
    storage_client = storage.Client.from_service_account_json(r'db103head.json')
    ##storage名稱
    bucket_name = 'db103_head_gpx'
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    print(type(blobs))
    for blob in blobs:
        print(blob.name)
        blobs_list.append(blob.name)
    return blobs_list


# 下載資料(storage名稱,storage上的檔案來源名稱,下載後的目標名稱,金鑰)
def download_blob_gpx(source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    ##放置金鑰位置
    storage_client = storage.Client.from_service_account_json(r'db103head.json')
    ##storage名稱
    bucket_name = 'db103_head_gpx'
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))


# 上傳資料(storage名稱,來源名稱,目標名稱,金鑰)
def upload_blob_html(source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    ##放置金鑰位置
    storage_client = storage.Client.from_service_account_json(r'db103head.json')
    ##storage名稱
    bucket_name = 'db103_head_html'
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


# 顯示資料項目(storage名稱,金鑰)
def list_blobs_html():
    blobs_list=[]
    """Lists all the blobs in the bucket."""
    ##放置金鑰位置
    storage_client = storage.Client.from_service_account_json(r'db103head.json')
    ##storage名稱
    bucket_name = 'db103_head_html'
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    print(type(blobs))
    for blob in blobs:
        print(blob.name)
        blobs_list.append(blob.name)
    return blobs_list


# 下載資料(storage名稱,storage上的檔案來源名稱,下載後的目標名稱,金鑰)
def download_blob_html(source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    ##放置金鑰位置
    storage_client = storage.Client.from_service_account_json(r'db103head.json')
    ##storage名稱
    bucket_name = 'db103_head_html'
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))


# 上傳資料(storage名稱,來源名稱,目標名稱,金鑰)
def upload_blob_png(source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    ##放置金鑰位置
    storage_client = storage.Client.from_service_account_json(r'db103head.json')
    ##storage名稱
    bucket_name = 'db103_head_png'
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


# 顯示資料項目(storage名稱,金鑰)
def list_blobs_png():
    blobs_list=[]
    """Lists all the blobs in the bucket."""
    ##放置金鑰位置
    storage_client = storage.Client.from_service_account_json(r'db103head.json')
    ##storage名稱
    bucket_name = 'db103_head_png'
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    print(type(blobs))
    for blob in blobs:
        print(blob.name)
        blobs_list.append(blob.name)
    return blobs_list


# 下載資料(storage名稱,storage上的檔案來源名稱,下載後的目標名稱,金鑰)
def download_blob_png(source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    ##放置金鑰位置
    storage_client = storage.Client.from_service_account_json(r'db103head.json')
    ##storage名稱
    bucket_name = 'db103_head_png'
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))