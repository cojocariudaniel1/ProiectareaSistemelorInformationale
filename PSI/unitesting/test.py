# import os
# from base import Base
# from sqlalchemy_schemadisplay import create_uml_graph, create_schema_graph
# from sqlalchemy.orm import class_mapper
# from sqlalchemy import MetaData
# os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'
# # lets find all the mappers in our model
# mappers = []
# for attr in dir(Base):
#     if attr[0] == '_': continue
#     try:
#         cls = getattr(Base, attr)
#         mappers.append(class_mapper(cls))
#     except Exception:
#         pass
#
# # pass them to the function and set some formatting options
# graph = create_uml_graph(mappers,
#     show_operations=False, # not necessary in this case
#     show_multiplicity_one=False # some people like to see the ones, some don't
# )
# graph.write_png('schema1.png') # write out the file