import bpy
from bpy.types import Operator

class FTOOLS_OT_ChangeDataName(Operator):

  bl_idname = "ftools.changedataname"
  bl_label = "Fix Data Names"
  bl_description = "Renames all mesh data names to object names"

  def execute(self, context):
    
    LOWSUFFIX = context.scene.ftools.low_suffix
    HIGHSUFFIX = context.scene.ftools.high_suffix

    sceneCollection = bpy.data.collections

    for col in sceneCollection:
      if col.name.endswith(LOWSUFFIX) or col.name.endswith(HIGHSUFFIX):
        for obj in col.objects:
          obj.data.name = obj.name
          
    return {'FINISHED'}