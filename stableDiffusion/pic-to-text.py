import replicate

url = "/workspaces/StableDiffusion/stableDiffusion/1 (1043).jpg"

def pic_to_text(url_address):
    model = replicate.models.get("methexis-inc/img2prompt")
    version = model.versions.get("50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5")
    inputs = {
        "image": open(url_address, "rb"),
    }
    output = version.predict(**inputs)
    return output
 
# model = replicate.models.get("methexis-inc/img2prompt")
# version = model.versions.get("50adaf2d3ad20a6f911a8a9e3ccf777b263b8596fbd2c8fc26e8888f8a0edbb5")
# inputs = {
#     "image": open("/workspaces/StableDiffusion/stableDiffusion/1 (1043).jpg", "rb"),
# }
# output = version.predict(**inputs)
# print(output)

if __name__ == "__main__":
    print(pic_to_text(url))