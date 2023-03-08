[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)
## Stable Diffusion

1. Words to pic
key:
* Input prompt

* pixel dimensions of output image "256x256" or "768x768",

    > 'image_dimensions': "768x768",

* Specify things to not see in the output
    * 'negative_prompt': ...,

*  Number of images to output.
    *  Range: 1 to 4

    > 'num_outputs': x,

* Number of denoising steps
    * Range: 1 to 500
    > 'num_inference_steps': 50,

* Scale for classifier-free guidance
    * Range: 1 to 20
    > 'guidance_scale': 7.5,

* Choose a scheduler.
    > 'scheduler': "DPMSolverMultistep",

*  Random seed. Leave blank to randomize the seed
    > 'seed': ...,


2. pic to word 
import picture and find the elements in the pic and print it out.