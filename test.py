import hub
import tensorflow_datasets as tfds
from PIL import Image

ds = hub.Dataset("./data/test_tfds/coco")
# print(ds)

# img = ds["image"][0].compute()

# print(type(ds))
# print(ds)
# print("--------------------------------------")
# print(type(ds["objects"]))
# print(ds["objects"])
# print("--------------------------------------")  # print(img)
# print(type(ds["objects"][0]))
# print("--------------------------------------")
# print(type(ds["objects"][0].compute()["bbox"]))  # TODO: add to list
# print(ds["objects"][0].compute()["bbox"])  # TODO: add to list

# print(ds["objects"][0].compute()["is_crowd"])

img = Image.fromarray(ds["image", 0].compute())
img.save("./lmao.jpeg", "jpeg")
