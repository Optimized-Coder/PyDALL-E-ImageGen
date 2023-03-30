'''

DALL-E image placeholder generator based on templated user prompt

DALL-E is an artificial intelligence language model developed by OpenAI that can generate images from textual descriptions. 
It uses a combination of deep learning techniques such as Generative Adversarial Networks (GANs) and Transformers to 
understand natural language input and produce corresponding images.

===== A NOTE ON COPYRIGHT =====
As with most AI language models and associated outputs, the copyright status of DALL-E generated images is a subject of debate and uncertainty. While OpenAI, the 
developer of DALL-E, has claimed ownership of the model and the training data used to create it, the generated images themselves may not be subject to copyright 
protection, as they are not created by humans and do not meet the originality requirement for copyright protection.

However, the use of DALL-E-generated images may still be subject to legal restrictions or licensing requirements depending on how they are used and by whom. For 
example, if the images are used for commercial purposes, they may be subject to trademark or intellectual property laws.

It is important to note that the legal and ethical implications of AI-generated content are still being explored and debated by legal and policy experts, and the 
copyright status of DALL-E-generated images may evolve as these discussions continue.



The MIT License (MIT)
Copyright © 2023 Joshua Shepherd

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the 
Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


'''

from core import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)