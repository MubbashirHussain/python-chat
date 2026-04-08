from app.config.cloudinary import cloudinary
import cloudinary.uploader
from fastapi import UploadFile
import uuid


async def uploadImages(
    file: UploadFile, folder: str = "chat-app/users/profiles"
) -> str:
    try:
        # Optional: validate file type
        if file.content_type not in ["image/jpeg", "image/png", "image/webp"]:
            raise Exception("Invalid file type")

        # Upload to Cloudinary
        result = cloudinary.uploader.upload(
            file.file,
            public_id=str(uuid.uuid4()),  # unique name
            folder=folder,  # optional folder
            resource_type="image",
        )

        # Return secure URL
        return result.get("secure_url")

    except Exception as e:
        print("Cloudinary Upload Error:", e)
        raise Exception("Image upload failed")
