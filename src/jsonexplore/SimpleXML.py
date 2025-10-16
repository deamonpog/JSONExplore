import xml.etree.ElementTree as ET

class SimpleXML:
    def __init__(self, xml_string):
        self.xml_string = xml_string
        self.root = ET.fromstring(self.xml_string)

    def to_dict(self):
        return self._element_to_dict(self.root)

    def _element_to_dict(self, element):
        if element is None:
            return None

        result = {}
        for child in element:
            result[child.tag] = self._element_to_dict(child)

        if not result:
            return element.text

        return result
    
    def analyze_tag_usagee(self):
        tag_counts = {}
        self._count_tags(self.root, tag_counts)
        return tag_counts
    
    def _count_tags(self, element, tag_counts):
        if element.tag in tag_counts:
            tag_counts[element.tag] += 1
        else:
            tag_counts[element.tag] = 1
        
        for child in element:
            self._count_tags(child, tag_counts)
