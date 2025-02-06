## <img src='https://abrain.one/img/lemur-nn-icon-64x64.png' width='32px'/> Neural Network Dataset 
<a href='https://pypi.python.org/pypi/nn-dataset'><img src='https://img.shields.io/pypi/v/nn-dataset.svg'/></a>
   
LEMUR - Learning, Evaluation, and Modeling for Unified Research

<img src='https://abrain.one/img/lemur-nn-whit.jpg' width='25%'/>

The original version of the <a href='https://github.com/ABrain-One/nn-dataset'>LEMUR dataset</a> was created by <strong>Arash Torabi Goodarzi, Roman Kochnev</strong> and <strong>Zofia Antonina Bentyn</strong> at the Computer Vision Laboratory, University of Würzburg, Germany.

<h3>Overview 📖</h3>
The primary goal of NN Dataset project is to provide flexibility for dynamically combining various deep learing tasks, datasets, metrics, and neural network models. It is designed to facilitate the verification of neural network performance under various combinations of training hyperparameters and data transformation algorithms, by automatically generating performance statistics. It is primarily developed to support the <a href="https://github.com/ABrain-One/nn-gen">NN Gen</a> project.

## Installation of the Latest Version of the NN Dataset
```bash
pip install nn-dataset --upgrade
rm -rf db
```
From GitHub:
```bash
pip uninstall nn-dataset -y
rm -rf db
pip install git+https://github.com/ABrain-One/nn-dataset --upgrade --force --extra-index-url https://download.pytorch.org/whl/cu124
```

## Environment for NN Dataset Contributors
### Pip package manager
Create a virtual environment, activate it, and run the following command to install all the project dependencies:
```bash
pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu124
```

### Docker
All versions of this project are compatible with <a href='https://hub.docker.com/r/abrainone/ai-linux' target='_blank'>AI Linux</a> and can be run inside a Docker image:
```bash
docker run -v /a/mm:. abrainone/ai-linux bash -c "PYTHONPATH=/a/mm python -m ab.nn.train"
```

## Usage

Standard use cases:
1. Add a new neural network model into the `ab/nn/nn` directory.
2. Run the automated training process for this model (e.g., a new ComplexNet training pipeline configuration):
```bash
python -m ab.nn.train -c img-classification_cifar-10_acc_ComplexNet
```
or for all image segmentation models using a fixed range of training parameters and transformer:
```bash
python run.py -c img-segmentation -f echo --min_learning_rate 1e-4 -l 1e-2 --min_momentum 0.8 -m 0.99 --min_batch_binary_power 2 -b 6
```
To reproduce the previous result, set the minimum and maximum to the same desired values:
```bash
python run.py -c img-classification_cifar-10_acc_AlexNet --min_learning_rate 0.0061 -l 0.0061 --min_momentum 0.7549 -m 0.7549 --min_batch_binary_power 2 -b 2 -f norm_299
```
To view supported flags:
```bash
python run.py -h
```

## Contribution

To contribute a new neural network (NN) model to the NN Dataset, please ensure the following criteria are met:

1. The code for each model is provided in a respective ".py" file within the <strong>/ab/nn/nn</strong> directory, and the file is named after the name of the model's structure.
2. The main class for each model is named <strong>Net</strong>.
3. The constructor of the <strong>Net</strong> class takes the following parameters:
   - <strong>in_shape</strong> (tuple): The shape of the first tensor from the dataset iterator. For images it is structured as `(batch, channel, height, width)`.
   - <strong>out_shape</strong> (tuple): Provided by the dataset loader, it describes the shape of the output tensor. For a classification task, this could be `(number of classes,)`.
   - <strong>prm</strong> (dict): A dictionary of hyperparameters, e.g., `{'lr': 0.24, 'momentum': 0.93, 'dropout': 0.51}`.
   - <strong>device</strong> (torch.device): PyTorch device used for the model training 
4. All external information required for the correct building and training of the NN model for a specific dataset/transformer, as well as the list of hyperparameters, is extracted from <strong>in_shape</strong>, <strong>out_shape</strong> or <strong>prm</strong>, e.g.: </br>`batch = in_shape[0]` </br>`channel_number = in_shape[1]` </br>`image_size = in_shape[2]` </br>`class_number = out_shape[0]` </br>`learning_rate = prm['lr']` </br>`momentum = prm['momentum']` </br>`dropout = prm['dropout']`.
5. Every model script has function returning set of supported hyperparameters, e.g.: </br>`def supported_hyperparameters(): return {'lr', 'momentum', 'dropout'}`</br> The value of each hyperparameter lies within the range of 0.0 to 1.0.
6. Every class <strong>Net</strong> implements two functions: </br>`train_setup(self, prm)`</br> and </br>`learn(self, train_data)`</br> The first function initializes the `criteria` and `optimizer`, while the second implements the training pipeline. See a simple implementation in the <a href="https://github.com/ABrain-One/nn-dataset/blob/main/ab/nn/nn/AlexNet.py">AlexNet model</a>.
7. For each pull request involving a new NN model, please generate and submit training statistics for 100 Optuna trials (or at least 3 trials for very large models) in the <strong>ab/nn/stat</strong> directory. The trials should cover 5 epochs of training. Ensure that this statistics is included along with the model in your pull request. For example, the statistics for the ComplexNet model are stored in files <strong>&#x003C;epoch number&#x003E;.json</strong> inside folder <strong>img-classification_cifar-10_acc_ComplexNet</strong>, and can be generated by:<br/>
```bash
python run.py -c img-classification_cifar-10_acc_ComplexNet -t 100 -e 5
```
<p>See more examples of models in <code>/ab/nn/nn</code> and generated statistics in <code>/ab/nn/stat</code>.</p>

### Available Modules

The `nn-dataset` package includes the following key modules:

1. **Dataset**:
   - Predefined neural network architectures such as `AlexNet`, `ResNet`, `VGG`, and more.
   - Located in `ab.nn.nn`.

2. **Loaders**:
   - Data loaders for datasets such as CIFAR-10 and COCO.
   - Located in `ab.nn.loader`.

3. **Metrics**:
   - Common evaluation metrics like accuracy and IoU.
   - Located in `ab.nn.metric`.

4. **Utilities**:
   - Helper functions for training and statistical analysis.
   - Located in `ab.nn.util`.


## Citation

If you find the LEMUR Neural Network Dataset to be useful for your research, please consider citing:
```bibtex
@misc{ABrain-One.NN-Dataset,
  author       = {Goodarzi, Arash Torabi and Kochnev, Roman and Khalid, Waleed and Qin, Furui and Kathiriya, Yash Kanubhai and Dhameliya, Yashkumar Sanjaybhai and Ignatov, Dmitry and Timofte, Radu},
  title        = {Neural Network Dataset: Towards Seamless AutoML},
  howpublished = {\url{https://github.com/ABrain-One/nn-dataset}},
  year         = {2024},
}
```

## Licenses

This project is distributed under the following licensing terms:
<ul><li>for neural network models adopted from other projects
  <ul>
    <li> Python code under the legacy <a href="Doc/Licenses/LICENSE-MIT-NNs.md">MIT</a> or <a href="Doc/Licenses/LICENSE-BSD-NNs.md">BSD 3-Clause</a> license</li>
    <li> models with pretrained weights under the legacy <a href="Doc/Licenses/LICENSE-DEEPSEEK-LLM-V2.md">DeepSeek LLM V2</a> license</li>
  </ul></li>
<li> all neural network models and their weights not covered by the above licenses, as well as all other files and assets in this project, are subject to the <a href="LICENSE.md">MIT license</a></li> 
</ul>

#### The idea of Dr. Dmitry Ignatov
