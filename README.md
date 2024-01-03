# nsfw-sf-ai-classifier

An AI that use machine learning to detect NSFW images

## Installation

```bash
python3 -m pip install -r requirements.txt
```

## Usage

To execute the AI :

1. Place the images you want to classify in the `execute` folder
2. Execute the `execute.py` file with this command :

    ```bash
    python3 execute.py
    ```

3. The result will appear in the console

## Training

To train the AI :

1. Place the images you want to train with in the `train` folder, you have to create a folder for nsfw and one for sfw
2. Execute the `train.py` file with this command :

    ```bash
    python3 train.py
    ```

3. The AI will be trained and the result will be saved as `modele_nsfw_sfw.h5`

RENAME THE PREVIOUS MODEL BEFORE TRAINING A NEW ONE TO AVOID LOSING IT !

---

## License : [MIT](https://choosealicense.com/licenses/mit/)

## Author : [@Tarkhubal](https://www.github.com/Tarkhubal)

You MUST credit me if you use this project in your own project !

---

## Contributing

You can contribute to this project by creating a zip file with the images you want to train with and send it to me on Discord (@thomas0535) or [by email](mailto:thb5309@gmail.com). You can also create a zip file dans make a pull request with a link to your file in the description !

All images are welcome !

## Acknowledgements

Thanks to:

- [r/datasets](https://www.reddit.com/r/datasets/)
- [r/nsfw](https://www.reddit.com/r/nsfw/)
- [EBazarov/nsfw_data_source_urls](https://github.com/EBazarov/nsfw_data_source_urls)
- [Standford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/)
- [Indoor Scene Recognition](http://web.mit.edu/torralba/www/indoor.html)
- [Cifar 10](https://www.cs.toronto.edu/~kriz/cifar.html)
- [Celebfaces](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)

## Some numbers

- 271 299 : number of training images for the v2 (~269 000 more images than the v1)
  - 20 311 NSFW images
  - 250 988 SFW images
- 28 495 908 864 (28.5Go) : Total size of all images

---

## Versions

### AI versions

| Version        | Release date | Number of images | Is available |
| :---           |    :----:    |      :----:      |    :----:    |
| v3 (Neogix)    | xx/01/2024   | ~400 000         | No           |
| v2 (Oxynax)    | 20/05/2023   | 271 299          | Yes          |
| v1 (The first) | 15/05/2023   | ~2 400           | No (deleted) |

---

### Code versions (implemented functionnalities)

**Version 1.0 (current)** :

Image classification :

  1. The result of the classification will appear only in the console
  2. Added a program to check files from the `train/dataset/*` folder to delete non-usables images (not images, corrupted images, too small etc.). THIS SCRIPT **DELETE** THE NOT-COMPATIBLE FILES, BE CAREFUL !

**Version 1.1 (in coming)** :

Image classification :

  1. The classified images will be copied in the `result/nsfw` and `result/sfw` folders
