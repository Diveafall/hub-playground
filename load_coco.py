import hub
import tensorflow_datasets as tfds

# with tfds.testing.mock_data(num_examples=5):
ds = hub.Dataset.from_tfds("coco", split="test[0:5]", num=5)
res_ds = ds.store("./data/test_tfds/coco", length=5)
print(ds)
