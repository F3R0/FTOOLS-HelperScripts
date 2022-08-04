import bpy
from bpy.types import Operator

class FTOOLS_OT_Categorize(Operator):

  bl_idname = "ftools.categorize"
  bl_label = "Categorize Objects"
  bl_description = "Move the objects in the scene to a proper collection according to their suffixes."
  
  def execute(self, context):
    def messageBox(message = "", title = "Not found!", icon = 'ERROR'):
        def draw(self, context):
          self.layout.label(text=message)

        bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)    

    def checkUncatColl():
      if UNCATEGORIZED not in collections.keys():
        uncategorizedColl = collections.new(UNCATEGORIZED)
        bpy.context.scene.collection.children.link(uncategorizedColl)
        self.report({'INFO'}, "CREATED a collection for uncategorized objects.")
      else:
        uncategorizedColl = bpy.data.collections[UNCATEGORIZED]
        self.report({'INFO'}, "Collection for uncategorized objects FOUND")
      return uncategorizedColl

    def catObjectsToTemps():
      for col in collections:
        for obj in col.objects:
          if obj.name.endswith(LOWSUFFIX):
            temp_low.append(obj)
          elif obj.name.endswith(HIGHSUFFIX):
            temp_high.append(obj)
          else:
            temp_none.append(obj)

    def unlinkObjWithSuffix(suffix):
      for col in collections:
        for obj in col.objects:
          if obj.name.endswith(suffix):
            col.objects.unlink(obj)
          elif obj.name.endswith(suffix):
            col.objects.unlink(obj)
    
    def unlinkUncatObjects():
      for col in collections:
        for obj in col.objects:
          if obj.name.endswith(LOWSUFFIX) or obj.name.endswith(HIGHSUFFIX):
            pass
          else:
            col.objects.unlink(obj)

    def linkObjToTargetColl(temp, target):
      for obj in temp:
        target.objects.link(obj)
            
    def findTargetCollection(suffix): 
      temp = []
      for col in collections:
        if col.name.endswith(suffix):
          temp.append(col)
      if temp == []:
          messageBox(message="There is no COLLECTION with suffix: "+str(suffix))
          return None
      else:
        return temp[0]

    ## User inputs from the Panel
    UNCATEGORIZED = context.scene.ftools.unc_coll
    LOWSUFFIX = context.scene.ftools.low_suffix
    HIGHSUFFIX = context.scene.ftools.high_suffix
    GATHER_UNC = context.scene.ftools.gather_unc

    print(LOWSUFFIX)
    print(HIGHSUFFIX)

    # Temporary lists
    temp_low = []
    temp_high = []
    temp_none = []

    # Cache all collections
    collections = bpy.data.collections

    catObjectsToTemps()
    
    # Gather Categorized?
    if GATHER_UNC == True:
      unlinkUncatObjects()
      uncatCol = checkUncatColl()
      linkObjToTargetColl(temp_none, uncatCol)

    # Place Objects to the corresponding collections (LOW)
    target = findTargetCollection(LOWSUFFIX)
    if temp_low != []:
      if target is not None:
        unlinkObjWithSuffix(LOWSUFFIX)
        linkObjToTargetColl(temp_low, target)

    # Place Objects to the corresponding collections (HIGH)
    target = findTargetCollection(HIGHSUFFIX)
    if temp_high != []:
      if target is not None:
        unlinkObjWithSuffix(HIGHSUFFIX)
        linkObjToTargetColl(temp_high, target)

    return {'FINISHED'}