from mayavi import mlab
from mayavi.core.ui.api import MlabSceneModel, SceneEditor
from traits.api import HasTraits
from traitsui.api import View, Item, HSplit


class MultiView(HasTraits):

    def __init__(self, *args):
        """
        Use this class for plotting multiple 3D volumes in multiple windows.
        :param args (List): each element in the list is treated as a new mayavi subwindows which is dinamically generated.
        each element of the list can be either a numpy volume or a list of numpy volumes.
        if a list of volumes is specified, then that volumes will be plot on the same subwindow.
        example:
            MultiView([volume_1, volume_2, volume_3])
            -> 3 sub-windows with a single volume each
            MultiView([[vol_1, detail], [vol_2]])
            -> 2 sub-windows, one of them with two volumes overlapped

        you can also specify an opacity for a given volume by passing a tuple (volume, opacity) instead of a volume
        example:
            MultiView([[(volume_1, 0.2), volume_2], [volume_3]])
            -> 2 sub-windows: one window with two volumes, one of which with 20% opacity and another window with a single volume

        if not specified, opacity is set to 1.
        use show() method for plotting.
        """

        HasTraits.__init__(self)
        windows = [arg for arg in args if isinstance(arg, list)]  # filter not-list object

        self.num_views = len(windows)
        num_colors = max([len(w) for w in windows])  # which is the windows with highest number of volumes?
        self.colors = np.random.rand(num_colors, 3)

        istance_ids = []  # items will be attached to the mayavi scene by the name/ID of their attributes
        for i, w in enumerate(windows):
            istance_id = 'istance_{}'.format(str(i))
            setattr(self, istance_id, MlabSceneModel())
            istance_ids.append(istance_id)

        self.items = [Item(w, editor=SceneEditor(), height=500, width=600) for w in istance_ids]  # one Item per window
        self.view = View(HSplit(*self.items), resizable=True)  # fill all the windows in a view

        for w_id, w in enumerate(windows):
            for v_id, volume in enumerate(w):
                if isinstance(volume, tuple):
                    vol, opacity = volume[0], volume[1]
                else:
                    vol, opacity = volume, 1
                mlab.contour3d(vol, color=tuple(self.colors[v_id]), opacity=opacity, figure=getattr(self, istance_ids[w_id]).mayavi_scene)

    def show(self):
        self.configure_traits(view=self.view)