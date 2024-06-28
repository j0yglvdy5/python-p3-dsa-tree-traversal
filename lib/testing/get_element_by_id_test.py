from tree import Tree

class TestTree:
    '''Class Tree in tree.py'''

    def test_get_element_by_id(self):
        '''get_element_by_id test'''
        tree = Tree({
            'tag_name': 'body',
            'id': None,
            'children': [
                {
                    'tag_name': 'div',
                    'id': 'main',
                    'children': [
                        {
                            'tag_name': 'h1',
                            'id': 'heading',
                            'text_content': 'Title',
                            'children': []
                        },
                        {
                            'tag_name': 'h2',
                            'id': None,
                            'text_content': 'Subtitle',
                            'children': []
                        }
                    ]
                }
            ]
        })

        # Test case 1: Element with id 'heading' exists
        expected_heading = {
            'tag_name': 'h1',
            'id': 'heading',
            'text_content': 'Title',
            'children': []
        }
        assert tree.get_element_by_id('heading') == expected_heading

        # Test case 2: Element with id 'nope' does not exist
        assert tree.get_element_by_id('nope') is None

if __name__ == '__main__':
    import unittest
    unittest.main()
