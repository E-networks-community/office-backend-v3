import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
    cloud_name="dagw7pro6",
    api_key="761564937985964",
    api_secret="4GsZPO7aW5TvNNrkIAD4AgC_TTI"
)


def upload_image_to_cloudinary(image):
    result = cloudinary.uploader.upload(
        image,
        quality='auto:low',
    )
    image_url = result['url']
    return image_url
