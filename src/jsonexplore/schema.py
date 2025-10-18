"""
Schema exploration for unknown JSON structures.

This module provides the ExploreUnknown class for exploring JSON data
when the structure is not known in advance. It combines exploration
capabilities with safe access patterns.
"""

import os
import json
from .Maybe import Maybe

class ExploreUnknown:
    """
    Explorer for JSON data with unknown or varying schema structure.

    This class provides schema-ish traversal capabilities when the JSON
    structure is not known in advance. It combines the functionality of
    the Explore class with safe access patterns from Maybe.

    Parameters
    ----------
    json_object : dict, list, or any
        The JSON object to explore with unknown schema.

    Attributes
    ----------
    json_object : dict, list, or any
        The original JSON object being explored.
    child_keys : list
        A list of keys (for dicts) or indices (for lists) of direct children.

    Examples
    --------
    >>> data = {'users': [{'name': 'Alice'}, {'name': 'Bob', 'age': 30}]}
    >>> explorer = ExploreUnknown(data)
    >>> print(explorer.get_child_keys())
    ['users']
    
    >>> field_counts = explorer.invest_grandchildren()
    >>> print(field_counts)  # Shows distribution of fields in nested objects
    """
    def __init__(self, json_object):
        self.json_object = json_object
        self.child_keys = []
        if type(self.json_object) is dict:
            self.child_keys = list(self.json_object.keys())
        if type(self.json_object) is list:
            self.child_keys = [idx for idx in range(len(self.json_object))]

    def __repr__(self):
        """
        Return a string representation of the ExploreUnknown object.

        Returns
        -------
        str
            A formatted string showing the type and size of the explored object.
        """
        return f"ExploreUnkown({type(self.json_object)}[size={len(self.child_keys)}])"

    def get_child_keys(self):
        """
        Get the keys or indices of direct children.

        Returns
        -------
        list
            For dictionaries: list of string keys.
            For lists: list of integer indices.
            For other types: empty list.
        """
        return self.child_keys
    
    def explore_child(self, child_key):
        """
        Create a new ExploreUnknown instance for a specific child.

        Parameters
        ----------
        child_key : str or int
            The key (for dict) or index (for list) of the child to explore.

        Returns
        -------
        ExploreUnknown
            A new ExploreUnknown instance wrapping the child object, or None if not found.
        """
        if child_key in self.json_object:
            return ExploreUnknown(self.json_object[child_key])
        return ExploreUnknown(None)
    
    def invest_grandchildren(self, verbose=False):
        """
        Analyze the distribution of grandchild keys across all children.

        This method examines each child of the current object and counts
        how frequently each grandchild key appears across all children.
        Useful for understanding the schema of collections with varying structures.

        Parameters
        ----------
        verbose : bool, optional
            If True, print detailed exploration progress, by default False.

        Returns
        -------
        dict
            A dictionary mapping grandchild keys to their occurrence counts.

        Examples
        --------
        >>> data = [
        ...     {'name': 'Alice', 'age': 30},
        ...     {'name': 'Bob', 'email': 'bob@example.com'},
        ...     {'name': 'Charlie', 'age': 25}
        ... ]
        >>> explorer = ExploreUnknown(data)
        >>> counts = explorer.invest_grandchildren()
        >>> print(counts)
        {'name': 3, 'age': 2, 'email': 1}
        """
        if verbose:
            print(f"Exploring grandchildren of type: {type(self.child_keys)} (size={len(self.json_object)}) with keys: {self.get_child_keys()}")
        counts = {}
        for child_key in self.child_keys:
            if verbose:
                print(f"Exploring child key: {child_key}")
            expChild = self.explore_child(child_key)
            if verbose:
                print(f"  Child type: {type(expChild.json_object)} with keys: {expChild.get_child_keys()}")
            for grandChildKey in expChild.get_child_keys():
                if verbose:
                    print(f"    Found grandchild key: {grandChildKey}")
                if grandChildKey in counts:
                    counts[grandChildKey] += 1
                else:
                    counts[grandChildKey] = 1
            
        return counts
        
    def field(self, field):
        """
        Safely access a field in a JSON object (dict).

        Parameters
        ----------
        field : str
            The field name to access in the dictionary.

        Returns
        -------
        Maybe
            A Maybe instance wrapping the field value or None if not present.
        """
        if self.json_object is not None and type(self.json_object) is dict and field in self.json_object:
            return Maybe(self.json_object[field])
        return Maybe(None)
    
    def index(self, index):
        """
        Safely access an index in a JSON array (list).

        Parameters
        ----------
        index : int
            The zero-based index to access in the list.

        Returns
        -------
        Maybe
            A Maybe instance wrapping the item value or None if not present.
        """
        if self.json_object is not None and type(self.json_object) is list and index < len(self.json_object):
            return Maybe(self.json_object[index])
        return Maybe(None)
    
    def array(self, func=lambda m: m, as_type=list):
        """
        Convert a JSON array to a list of transformed items.

        Parameters
        ----------
        func : callable, optional
            Function to transform each item in the array, by default identity function.
        as_type : type, optional
            The type constructor for the result container, by default list.

        Returns
        -------
        list or as_type
            A container of transformed items, or empty container if not a list.
        """
        if self.json_object is not None and type(self.json_object) is list:
            return as_type([func(obj) for obj in self.json_object])
        return []
    
    def array_from_dict(self, func=lambda k,o: o, as_type=list):
        """
        Convert a JSON object (dict) to a list of transformed key-value pairs.

        Parameters
        ----------
        func : callable, optional
            Function to transform each key-value pair. Signature: func(key, value).
            Default returns the value.
        as_type : type, optional
            The type constructor for the result container, by default list.

        Returns
        -------
        list or as_type
            A container of transformed items, or empty container if not a dict.
        """
        if self.json_object is not None:
            return as_type([func(key, obj) for key,obj in self.json_object.items()])
        return []
    
    def value(self):
        """
        Get the wrapped value.

        Returns
        -------
        any
            The wrapped JSON object, which may be None if no value exists.
        """
        return self.json_object




    

