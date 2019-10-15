{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "helper.py",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Joycechidi/Deep-Learning-/blob/master/PyTorch-Practice/helper.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "FKEUXEGI9p0j",
        "colab_type": "text"
      },
      "source": [
        "This helper file will help in keeping the testing, classifier and visualization functions separate from the neural network I want to train.This will help keep my code clean and reuseable."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Qlgl5zhq87iT",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "from torch import nn, optim\n",
        "from torch.autograd import Variable"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "U6PZ4ibj-kPA",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def test_network(net, trainloader):\n",
        "    criterion = nn.MSELoss()\n",
        "    ptimizer = optim.Adam(net.parameter(), lr=0.0001)\n",
        "    \n",
        "    dataiter = iter(trainloader)\n",
        "    images, labels = dataiter.next()\n",
        "    \n",
        "    #Create Variables for the inputs and targets\n",
        "    inputs = Variable(images)\n",
        "    targets = Varaible(images)\n",
        "    \n",
        "    #Clear the gradients from all Variable\n",
        "    optimizer.zero_grad()\n",
        "    \n",
        "    #Forward pass, then backward pass, then update weights\n",
        "    output = net.forward(inputs)\n",
        "    loss = criterion(output, targets)\n",
        "    loss.backwards()\n",
        "    optimizer.step()\n",
        "    \n",
        "    return True\n",
        "    \n",
        "    \n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wglgl6qh-kN2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def imshow(image, ax=None, title=None, normalize=True):\n",
        "    \"\"\" Imshow for Tensor.\"\"\"\n",
        "    if ax is None:\n",
        "        fig, ax = plt.subplots()\n",
        "        \n",
        "    image = image.numpy().transpose((1, 2, 0))\n",
        "    \n",
        "    \n",
        "    if normalize:\n",
        "        mean = np.array([0.485, 0.456, 0.406])\n",
        "        std = np.array([0.229, 0.224, 0.225])\n",
        "        image = std * image + mean\n",
        "        image = np.clip(image, 0, 1)\n",
        "        \n",
        "    ax.imshow(image)\n",
        "    ax.spines['top'].set_visible(False)\n",
        "    ax.spines['right'].set_visible(False)\n",
        "    ax.spines['left'].set_visible(False)\n",
        "    ax.spines['bottom'].set_visible(False)\n",
        "    ax.tick_params(axis='both', length=0)\n",
        "    ax.set_xticklabels('')\n",
        "    ax.set_yticklabels('')\n",
        "    \n",
        "    return ax"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nPsNBCir-kKL",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def view_recon(img, recon):\n",
        "    \"\"\" Function for displaying an image as a PyTorch tensr and its\n",
        "    reconstruction also a PyTorch Tensor\n",
        "    \n",
        "    \n",
        "    \"\"\"\n",
        "    fig, axes = plt.subplots(ncols=2, sharex=True, sharey=True)\n",
        "    axes[0].imshow(img.numpy().squeeze())\n",
        "    axes[1].imshow(recon.data.numpy().squeeze())\n",
        "    for ax in axes:\n",
        "        ax.axis('off')\n",
        "        ax.set_adjustable('box-forced')"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5AHgVBnv-kHb",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "def view_classify(img, ps, version=\"MNIST\"):\n",
        "    ''' Function for viewing an image and it's predicted classes.\n",
        "    '''\n",
        "    ps = ps.data.numpy().squeeze()\n",
        "\n",
        "    fig, (ax1, ax2) = plt.subplots(figsize=(6,9), ncols=2)\n",
        "    ax1.imshow(img.resize_(1, 28, 28).numpy().squeeze())\n",
        "    ax1.axis('off')\n",
        "    ax2.barh(np.arange(10), ps)\n",
        "    ax2.set_aspect(0.1)\n",
        "    ax2.set_yticks(np.arange(10))\n",
        "    if version == \"MNIST\":\n",
        "        ax2.set_yticklabels(np.arange(10))\n",
        "    elif version == \"Fashion\":\n",
        "        ax2.set_yticklabels(['T-shirt/top',\n",
        "                            'Trouser',\n",
        "                            'Pullover',\n",
        "                            'Dress',\n",
        "                            'Coat',\n",
        "                            'Sandal',\n",
        "                            'Shirt',\n",
        "                            'Sneaker',\n",
        "                            'Bag',\n",
        "                            'Ankle Boot'], size='small');\n",
        "    ax2.set_title('Class Probability')\n",
        "    ax2.set_xlim(0, 1.1)\n",
        "\n",
        "    plt.tight_layout()\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "so4cZ960-jh2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}