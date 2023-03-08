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


* Example, here we use prompt "Duke students portraits picture with face details and hair style" as input 
here is the outputs:
![picture1](https://replicate.delivery/pbxt/L82zn3RzAXqdD1s8OMLsl9DWzKalUlgw6NBpZ1yPUBG9KXJE/out-0.png)
![picture2](https://replicate.delivery/pbxt/jMFQO2HwSHqENlHdfvPEJXMQS0OtVXvG7MZheYOZHaeqX5KhA/out-1.png)
![picture3](https://replicate.delivery/pbxt/gDKBjAc0J7LHBlIffWXogPl9v30e06pf5r06h0fuoeMo9KXJE/out-2.png)
![picture4](https://replicate.delivery/pbxt/rolASmRRt8aZEpAdJW6LhR4rBYxom3a981f5ZtPCbcW7VuSIA/out-3.png)

those AI generate human face are really easy to tell the different with real human faces. 

2. pic to word 
import picture and find the elements in the pic and print it out.