# Computer Vision - Texture Synthesis
This is the first part of the project where the goal is to implement and evaluate the idea of Texture Synthesis by Non-Parametric Sampling as proposed by Efros and Leung, ICCV99.  
<br/>
The paper can be found at this link : http://graphics.cs.cmu.edu/people/efros/research/NPS/efros-iccv99.pdf

## Getting Started
We are given a pseudo code of the implementation of Non-Parametric Sampling algorithm which we need to run on the sample gif images to synthesize a 200x200 pixel image.  
<br/>
Example image : <br/> <img src="https://github.com/Shishir94/CV-TextureAnalysis/blob/master/textures/T1.gif" alt="Texture" width="160"><br/>
<br/>
We repeat this for various WindowSize parameters and evaluate the performance and quality of the synthesized image.  
<br/>
The pseudocode for the algorithm : http://graphics.cs.cmu.edu/people/efros/research/NPS/alg.html

We plot synthesize images for various window sizes hence resulting in synthesised images becoming better qualitatively however taking a longer time to be synthesized. The results for synthesized images for different seed images are as follows:

<br/>
Texture 1 : <br/> <img src="https://github.com/shishir-umesh/CV-TextureAnalysis/blob/master/result/T1-res.png" alt="Texture" width="160"><br/>

<br/>
Texture 2 : <br/> <img src="https://github.com/shishir-umesh/CV-TextureAnalysis/blob/master/result/T2-res.png" alt="Texture" width="160"><br/>

<br/>
Texture 3 : <br/> <img src="https://github.com/shishir-umesh/CV-TextureAnalysis/blob/master/result/T3-res.png" alt="Texture" width="160"><br/>

<br/>
Texture 4 : <br/> <img src="https://github.com/shishir-umesh/CV-TextureAnalysis/blob/master/result/T4-res.png" alt="Texture" width="160"><br/>

<br/>
Texture 5 : <br/> <img src="https://github.com/shishir-umesh/CV-TextureAnalysis/blob/master/result/T5-res.png" alt="Texture" width="160"><br/>
