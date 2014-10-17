(function() {
  packages = {

    // Lazily construct the package hierarchy from class names.
    root: function(classes) {
      var map = {};

      function find(name, data) {
        var node = map[name], i;
        if (!node) {
          node = map[name] = data || {name: name, children: []};
          if (name.length) {
            node.parent = find(name.substring(0, i = name.lastIndexOf(".")));
            node.parent.children.push(node);
            node.key = name.substring(i + 1);
          }
        }
        return node;
      }

      classes.forEach(function(d) {
        find(d.name, d);
      });

      return map[""];
    },

    // Return a list of imports for the given array of nodes.
    imports: function(nodes) {
      var map = {},map1={}
          imports = [];

      // Compute a map from name to node.
      nodes.forEach(function(d) {
        map[d.name] = d;
	map1[d.idval] = d.name;
      });

      // For each import, construct a link from the source to target node.
      nodes.forEach(function(d) {
        if (d.listf) {
	   //var listing = d.listf.substring(1, d.listf.length-1);
	   //var arr = listing.split(", ");
	   d.listf.forEach(function(i) {
          	imports.push({source: map[d.name], target: map[map1[i]]});
           });
	}
      });

      return imports;
    }

  };
})();
