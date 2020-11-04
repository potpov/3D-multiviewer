# Multiviewer for 3D volumes

This is a simple Python class for plotting one or more numpy volumes in multiple windows wrapped in a single view using mayavi.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mayavi and its dependencies, that's all we need.

```bash
pip install mayavi
pip install PyQt5
```

## Usage
you can plot numpy volumes by passing several list of volumes to the class and then use the show method.
each list is treated as a new sub-window. the following example will plot volume_1 and volume_2 in two separate windows as shown below.

```python
MultiView([volume_1], [volume_2]).show()
```


![alt text](https://ibin.co/w800/5gD6BbsA6DdV.png)

you can plot as many volumes as you want by adding more and more lists.
View will be just splittend in more sub-windows:

```python
MultiView([volume_1], [volume_2], [volume_n]).show()
```

![alt text](https://ibin.co/w800/5gD6OPWyUVm9.png)


you can also put more than a volume in a list and all those volumes will be plotted in the same window.
The following example plots three volumes in the first windows.

```python
MultiView([volume_1a, volume_1b, volume_1c]]).show()
```

![alt text](https://ibin.co/5gDALoXa3Pqo.png)

## dealing with opacity

furthermore, it is possible to specify the opacity of a volume. this is useful when overlapped volumes result in a fuzzy view. just pass a tuple (volume, opacity) instead of a volume directly.

```python
MultiView([(big_one, 0.4), detail, detail_2], [volume_2]]).show()
```

![alt text](https://ibin.co/w800/5gD6ULK8EYWT.png)
