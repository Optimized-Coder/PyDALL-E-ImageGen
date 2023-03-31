# PyDALL-E ImageGen
PyDALL-E ImageGen is a Python-based web application that generates placeholder images using OpenAI's DALL-E model. It is built on top of the Flask web framework and allows users to easily generate unique placeholder images on-the-fly.  
---  
---
Usage
To generate a placeholder image, simply use an image tag with the src attribute pointing to the appropriate endpoint in the PyDALL-E ImageGen application. The image tag should include query parameters to specify the desired image properties.

Here is the format of the URL that you can use:

```url
http://localhost:5000/?noun=[NOUN]&action=[ACTION]&color=[COLOR]&height=[HEIGHT]
```

## Parameters
- noun - The noun or object that you want the image to depict. This can be any string value, such as "cat", "tree", "car", etc.

- action - The action or verb that you want the image to depict. This can be any string value, such as "running", "cooking", "flying", etc.

- color - The color of the image. This can be any string value, such as "red", "blue", "green", etc.

- height - The height of the image in pixels. If this parameter is omitted, the default height is set to 512 pixels.
---

## Example
Here is an example of how you can use PyDALL-E ImageGen to generate a placeholder image:

```code
<img src="http://localhost:5000/?noun=dog&action=cooking&color=green&height=512">
```

This will generate a unique image of a green dog cooking, with a height of 512 pixels and an aspect ratio of 1:1.
---
---

## Support
If you encounter any issues or bugs with PyDALL-E ImageGen, please feel free to open an issue on our GitHub repository.
---
---
## License
PyDALL-E ImageGen is licensed under the MIT License. See LICENSE for more information.
---
---
## Please star this repo!
If you find PyDALL-E ImageGen useful, please consider starring our repository on GitHub. Your support helps us to continue improving the application and adding new features. Thank you!