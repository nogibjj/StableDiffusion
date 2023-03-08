import replicate

model = replicate.models.get("methexis-inc/img2prompt")
version = model.versions.get("50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5")
inputs = {
    "image": open("/workspaces/StableDiffusion/IMG_3925.JPG", "rb"),
}
output = version.predict(**inputs)
print(output)