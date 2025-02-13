import bpy

from .get_b_vars import get_context, get_active_object

def set_mode (mode):
  bpy.ops.object.mode_set(mode = mode)

def _get_object (name):
  return bpy.data.objects.get(name)

def select_all_objects (action = 'SELECT'):
  # TOGGLE – Toggle selection for all elements.
  # SELECT – Select all elements.
  # DESELECT – Deselect all elements.
  # INVERT – Invert selection of all elements.

  get_object().select_all(action = action)

def snap_cursor (location = (0, 0, 0)):
  context = get_context()
  prev_context = context.area.type
  context.area.type = 'VIEW_3D'
  # bpy.ops.view3d.snap_cursor_to_center()
  context.scene.cursor.location = location
  context.area.type = prev_context

def _active_object (object):
  get_context().view_layer.objects.active = object

def register_classes (classes):
  register, unregister = bpy.utils.register_classes_factory(classes)
  register()

def unregister_classes (classes):
  register, unregister = bpy.utils.register_classes_factory(classes)
  unregister()
