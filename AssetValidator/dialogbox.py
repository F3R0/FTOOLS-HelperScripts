import bpy
from bpy.types import Operator

class FTOOLS_OT_DialogBox(Operator):

  bl_label = "Open a Dialog Box"
  bl_idname = "ftools.dialogbox"

  textInput : bpy.props.StringProperty(
    name = "testfield",
    default = " "
  )
  
  def execute(self, context):
    
    return {'FINISHED'}

  def invoke(self, context, event):
    
    return {'FINISHED'}