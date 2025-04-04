
# glsurface
**glsurface** is a python class to show show 2d data with wxpython and pyopengl.

## Installation
```shell
$ pip install glsurface
```

## Usage
1. Derived a class from `TrackingSurface`
    ```python
    class Surface(TrackingSurface):
        def __init__(self, *args, **kwargs):
        TrackingSurface.__init__(self, *args, **kwargs)
        ...
    ```
2. Create an instance, and set data (optional)
    ```python
    class SurfacePanel(wx.Panel):

        def __init__(self, parent):
            wx.Panel.__init__(self, parent, -1)
            ...
            self.x = np.linspace(0, 2 * np.pi, 30).reshape((1, 30))
            z = np.cos(self.x).T * np.sin(self.x)
            self.canvas = Surface(self, {'z': z})
            ...

    ```
3. Update the data
    1. Add the new frame data to the current frame buffer
        ```python
        self.canvas.NewFrameArrive(z, silent=False)
        ```
    2. Or reset the frame buffer with new data
        ```python
        self.canvas.SetFrames(points, reset_buf_len=True, silent=False)
        ```
Check `gltest.py` for details.

<img src="https://github.com/tianzhuqiao/glsurface/blob/master/images/demo.gif?raw=true"></img>