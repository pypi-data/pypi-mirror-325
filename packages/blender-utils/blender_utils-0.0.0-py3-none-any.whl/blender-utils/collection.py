from .get_b_vars import get_context, get_collections

def create_collection (collection_name):
  new_collection = get_collections().new(collection_name)
  # 将新集合添加到当前场景中
  get_context().scene.collection.children.link(new_collection)

  return new_collection
