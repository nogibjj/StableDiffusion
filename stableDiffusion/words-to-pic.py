import replicate

model = replicate.models.get("stability-ai/stable-diffusion")
version = model.versions.get("db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf")

# https://replicate.com/stability-ai/stable-diffusion/versions/db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf#input
inputs = {
    # Input prompt
    'prompt': "Selecting Hyperparameters 1. Start with default values: Many deep learning frameworks provide default values for hyperparameters. These values have been chosen to work well in a wide range of situations, and can be a good starting point.",

    # pixel dimensions of output image
    'image_dimensions': "768x768",

    # Specify things to not see in the output
    # 'negative_prompt': ...,

    # Number of images to output.
    # Range: 1 to 4
    'num_outputs': 4,

    # Number of denoising steps
    # Range: 1 to 500
    'num_inference_steps': 50,

    # Scale for classifier-free guidance
    # Range: 1 to 20
    'guidance_scale': 7.5,

    # Choose a scheduler.
    'scheduler': "DPMSolverMultistep",

    # Random seed. Leave blank to randomize the seed
    # 'seed': ...,
}

# https://replicate.com/stability-ai/stable-diffusion/versions/db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf#output-schema
output = version.predict(**inputs)
print(output)