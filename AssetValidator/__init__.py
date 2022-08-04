bl_info = {
    "name": "Asset Validator",
    "author": "F3R0",
    "description": "Asset validation tool",
    "version": (0, 3, 2),
    "blender": (2,93,5),
    "location": "View3D",
    "warning": "",
    "doc_url": "",
    "category": "FTools",
}

import bpy

from .panel import FTOOLS_PT_Panel
from .categorize import FTOOLS_OT_Categorize
from .validatename import FTOOLS_OT_ValidateNames
from .datanames import FTOOLS_OT_ChangeDataName
from .dialogbox import FTOOLS_OT_DialogBox
from .properties import CustomProperties

toRegister = (
            FTOOLS_PT_Panel,
            FTOOLS_OT_Categorize,
            FTOOLS_OT_ValidateNames,
            FTOOLS_OT_ChangeDataName,
            FTOOLS_OT_DialogBox,
            CustomProperties

            )

def register():
    for cls in toRegister:
        bpy.utils.register_class(cls)
    bpy.types.Scene.ftools = bpy.props.PointerProperty(type=CustomProperties)


def unregister():
    del bpy.types.Scene.ftools
    for cls in toRegister:
        bpy.utils.unregister_class(cls)
    



