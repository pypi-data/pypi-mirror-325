# graph_db_interface

This repository acts as an interface to abstract SPARQL queries to callable methods to interact with a running GraphDB instance in an easier way.

# Installation

# Getting Started


```python
from graph_db_interface.graph_db_interface import GraphDB

myDB = GraphDB(
    base_url=<your_graph_db_url>,
    username=<your_graph_db_user>
    password=<your_graph_db_password>
    repository=<your_selected_repository_id>
)
```

# License

The package is licensed under the [MIT license](LICENSE).


# Acknowledgements
This package is developed as part of the INF subproject of the [CRC 1574: Circular Factory for the Perpetual Product](https://www.sfb1574.kit.edu/english/index.php). This work is therefore supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) [grant-number: SFB-1574-471687386]