# PetHarbor

PetHarbor is a Python package designed for anonymizing datasets using either a pre-trained model or a hash-based approach. It provides two main classes for anonymization: `lite` and `advance`.

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```


## Lite Anonymization
The `lite` anonymization class uses a hash-based approach to anonymize text data. Here is an example of how to use it:

### Arguments


### Usage


```python
from petharbor.lite import annonymise

lite = petharbor_lite(
    dataset_path="testing/data/out/predictions.csv",
    hash_table="petharbor/data/pet_names_hashed.txt",
    salt="shared_salt",
    text_column="item_text",
    cache=True,
    output_dir="testing/data/out",
)
lite.annonymise()
```

### Advanced Anonymization
The `advance` anonymization class uses a pre-trained model to anonymize text data. Here is an example of how to use it:

### Arguments

### Usage


```python
from petharbor.advance import annonymise

    advance = petharbor_advanced(
        dataset_path="testing/data/out/predictions.csv",
        model_path="testing/models/best-model.pt",
        text_column="item_text",
        cache=True,
        logs="logs/",
        output_dir="testing/data/out/predictions.csv",
    )
    advance.annonymise()
```

## Configuration

### Device Configuration

The device (CPU or CUDA) can be configured by passing the `device` parameter to the anonymization classes. If not specified, the package will automatically configure the device.

### Caching

Both methods have a caching feature such that records already annonnymised will not be annonymised again. Therefore, after the initial application of the model downstream annonymisation should be quicker. We apply a 'annonymised' flag to the dataset, if a record is marked '1' in this field we skip it, and add it back to the complete dataset at the end.

## Logging

Logging is set up using the `logging` module. Logs will provide information about the progress and status of the anonymization process.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License.