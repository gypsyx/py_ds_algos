import copy

class SimpleVersionedMap:
    """
    A versioned map that persists all previous versions. Additions create a new version.
    This is a naive implementation, not very efficient.
    """

    def __init__(self):
        self.current_version = {}
        self.versions = []

    def __repr__(self):
        val = ''
        for k,v in self.current_version.items():
            val += "'"+ k + "'" + ": " + self._get_val_repr(v) + ","
        
        return f"{{{val}}}"
    
    def _get_val_repr(self, val):
        if isinstance(val, str):
            return "'" + val + "'"
        return str(val)
        


    def set(self, key, value):
        """Creates new version from previous version with new key,value pair added"""
        new_version = copy.deepcopy(self.current_version)
        new_version[key] = value
        self.versions.append(new_version)
        self.current_version = new_version


    def get(self, key, version = 0):
        """Gets the value for key from the specified version if exists, raises error otherwise."""
        if 0 <= version < len(self.versions):
            request_version = self.versions[version]
            return request_version[key] # raises error if key is absent
        else:
            raise ValueError(f"{version} is invalid")


    def delete(self, key, version = 0):
        if 0 <= version < len(self.versions):
            request_version = self.versions[version]
            del request_version[key] # raises error if key is absent
        else:
            raise ValueError(f"{version} is invalid")


    def revert_to_version(self, version):
        if 0 <= version < len(self.versions):
            self.current_version = self.versions[version]
            # drop all versions after 'version' as that's latest now
            self.versions = self.versions[:version+1]
        else:
            raise ValueError(f"{version} is invalid")

    def show_versions(self):
        print() # to help when running pytests
        for i in range(len(self.versions)):
            print(i, " : ", self.versions[i])

