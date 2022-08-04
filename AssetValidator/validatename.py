import bpy
import re
from bpy.types import Operator

class FTOOLS_OT_ValidateNames(Operator):

  bl_idname = "ftools.validatenames"
  bl_label = "Validate Object Names"
  bl_description = "Checks the names of the objects in specific collections as if they are matching a naming convention."
  message = " "

  def execute(self, context):
    LOWSUFFIX = context.scene.ftools.low_suffix
    HIGHSUFFIX = context.scene.ftools.high_suffix
    UNCATEGORIZED = context.scene.ftools.unc_coll
    CHECK_UNC = context.scene.ftools.check_unc
    NAMEPATTERN = re.compile(context.scene.ftools.regex_pat)
    #NAMEPATTERN = re.compile("^[A-Z]+[a-z]+_+[A-Z][a-z]+_+(Low|High)")

    sceneCollection = bpy.data.collections

    valid = []
    invalid = []

    if CHECK_UNC == True:
      for col in sceneCollection:
        for obj in col.objects:
          if re.match(NAMEPATTERN, obj.name):
            valid.append(obj.name)
          else:
            invalid.append(obj.name)
            messageBox(invalid)
    else:
      for col in sceneCollection:
        if col.name.endswith(LOWSUFFIX) or col.name.endswith(HIGHSUFFIX):
          for obj in col.objects:
            if re.match(NAMEPATTERN, obj.name):
              valid.append(obj.name)
            else:
              invalid.append(obj.name)
              messageBox(invalid)
            
    return {'FINISHED'}

def messageBox(message = "", title = "INVALID NAMING CONVENTION", icon = 'ERROR'):
    def draw(self, context):
      for n in message:
        self.layout.label(text=n)
        self.layout.separator()
    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)


          














