import os
import io
import boto3
from PIL import Image

s3 = boto3.client('s3')

def lambda_handler(event, context):
    print(event)
    for record in event['Records']:
        source_bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        destination_bucket_name = '42sp-lkenji-o-bucket-converted'
        
        try:
            response = s3.get_object(Bucket=source_bucket_name, Key=object_key)
            image_content = response['Body'].read()

            with Image.open(io.BytesIO(image_content)) as img:
                img.thumbnail((500, 500)) 
                img = img.convert("L")
                buffer = io.BytesIO()
              
                image_format = img.format
                
                if image_format and image_format.upper() == 'JPG':
                    image_format = 'JPEG'
                elif not image_format or image_format.upper() not in ['JPEG', 'PNG', 'WEBP', 'GIF', 'BMP', 'TIFF']:
                    image_format = 'JPEG'
                
                print(f"Saving image as format: {image_format}")
                img.save(buffer, format=image_format)
                buffer.seek(0) 
                
                s3.put_object(
                    Bucket=destination_bucket_name,
                    Key=object_key,
                    Body=buffer,
                    ContentType='image/jpg'
                )
                print(f"Successfully processed and uploaded {object_key} to {destination_bucket_name}")

        except Exception as e:
            print(f"Error processing {object_key}: {e}")
            raise # Re-raise the exception to indicate a failure
