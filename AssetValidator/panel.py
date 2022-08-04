from bpy.types import Panel

class FTOOLS_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Asset Validator"
    bl_category = "FTOOLS"

    def draw(self, context):
        
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column()
        subcol = col.column(align=True)
        col.separator(factor=1)
        
        subcol.prop(context.scene.ftools, "gather_unc", text="Gather Uncategorized?")
        subcol.prop(context.scene.ftools, "unc_coll", text="Uncatagorized")
        subcol.prop(context.scene.ftools, "low_suffix", text="Low Suffix")
        subcol.prop(context.scene.ftools, "high_suffix", text="High Suffix")
        
        layout.separator(factor=100)
        col.separator(factor=1)
        props = col.operator("ftools.categorize",
                        text="Categorize Objects",
                        icon="OUTLINER")
        col.separator(factor=2)
        
        col.prop(context.scene.ftools, "check_unc", text="Check Uncategorized?")
        col.label(text="Regular Expression", icon="SYNTAX_OFF")
        col.column().prop(context.scene.ftools, "regex_pat")
        col.separator(factor=0.2)
        col.operator("ftools.validatenames",
                        text="Validate Obj Names",
                        icon="SYNTAX_OFF")

        col.separator(factor=0.2)

        col.operator("ftools.changedataname",
                        text="Fix Mesh Data Names",
                        icon="SEQ_STRIP_DUPLICATE")
        col.separator(factor=2)
        col.operator("ftools.dialogbox",
                        text="Check Mesh",
                        icon="SEQ_STRIP_DUPLICATE")