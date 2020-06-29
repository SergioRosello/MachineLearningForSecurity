# Neural network to detect Botnet traffic

This body of work is a implementation of a Keras Neural Network used to detect Botnet traffic.

## Dataset used

* [ISOT HTTP Botnet Database](https://drive.google.com/open?id=1LW-FNhgqTZfYswHSLPUxtwccwM75O4J4)

## How to execute

* Install python dependencies (`pip install -r requirements.txt`)
* download and extract dataset
* copy the following 4 files into the dataset's directory.
    * `extraction.sh`
    * `sanitize.py`
    * `identifyAndsort.sh`
    * `prepareData.sh`
* Run prepareData.sh
* Go one directory above and run `modeloSecuencial.py`

This will generate the neural network model and save to disk.

## Example project structure

```
* practicaFinal                 (Root directory)
  * modeloSecuencial.py         (Keras model)
  * isot_app_and_botnet_dataset (Extracted dataset)
    * application_data          (Extracted directory)
    * botnet_data               (Extracted directory)
    * extraction.sh             (Copied file)
    * sanitize.py               (Copied file)
    * identifyAndsort.sh        (Copied file)
    * prepareData.sh            (Copied file)
```
