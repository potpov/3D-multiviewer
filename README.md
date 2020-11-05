# Multiviewer for 3D volumes

This is a Python class for plotting one or more numpy volumes in multiple windows wrapped into a single view (based on mayavi).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mayavi and its dependencies, that's all we need.

```bash
pip install mayavi
pip install PyQt5
```

## Usage
You can plot numpy volumes by passing several list of volumes to the class; each list corresponds to an independent subwindow in the view.
The following example will plot volume_1 and volume_2 in two separate windows as shown below.

```python
MultiView([volume_1], [volume_2]).show()
```


![alt text](https://ibin.co/w800/5gI1F9e7G8Ar.png)

you can create as many windows as you want by adding more and more lists:

```python
MultiView([volume_1], [volume_2], [volume_n]).show()
```

![alt text](https://ibin.co/w800/5gI1HxrbymVV.png)


you can plot more volumes in a window by simply adding them to a list.
The following example plots two volumes in the first windows but you could provide with how many you want, they'll just overlap each other.

```python
MultiView([volume_1, sphere], [volume_2]).show()
```

![alt text](https://ibin.co/w800/5gI1OWN6KIsr.png)

## dealing with opacity

when plotting more than one volume in a window the overlapped volumes can result in a fuzzy view.
it is possible to specify the opacity of a volume by just passing a tuple (volume, opacity) instead of the volume directly as show below.

```python
MultiView([(big_one, 0.4), sphere], [volume_2]]).show()
```

![alt text](https://ibin.co/w800/5gI1Z8WkbR7R.png)
