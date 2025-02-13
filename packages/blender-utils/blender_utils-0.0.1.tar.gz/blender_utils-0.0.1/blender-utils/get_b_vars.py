import bpy

def get_ops ():
  return bpy.ops

def get_mesh ():
  return get_ops().mesh

def get_context ():
  return bpy.context

def get_object ():
  return get_ops().object

def get_armature ():
  return get_ops().armature

def get_active_object ():
  return get_context().active_object

def get_operator ():
  return bpy.types.Operator

def get_panel ():
  return bpy.types.Panel

def get_collections ():
  return bpy.data.collections

def get_bone_widget ():
  return get_ops().bonewidget
