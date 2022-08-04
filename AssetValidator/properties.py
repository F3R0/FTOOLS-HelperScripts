import bpy

class CustomProperties(bpy.types.PropertyGroup):
    
    low_suffix : bpy.props.StringProperty(name="", default="_Low")
    high_suffix : bpy.props.StringProperty(name="", default="_High")
    unc_coll : bpy.props.StringProperty(name= "", default="Uncategorized")
    gather_unc : bpy.props.BoolProperty(name="", default=True)
    check_unc : bpy.props.BoolProperty(name="", default=False)
    regex_pat : bpy.props.StringProperty(name= "", default="[A-Z][a-z]")