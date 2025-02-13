def add_row (layout, data, prop, text):
  row = layout.column().row()
  row.prop(data, prop, text = text)

def add_row_with_label (layout, label, data, prop, factor):
  split = layout.column().split(factor = factor)
  row_label = split.row()
  row_label.label(text = label)
  row_prop = split.row()
  row_prop.prop(data, prop, text = "")

def add_row_with_operator (layout, operator, text):
  row = layout.column().row()
  row.operator(operator, text = text)
  