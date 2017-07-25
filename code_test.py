import unittest
import code as code


class TestCode(unittest.TestCase):


    def test_simple_input(self):
        input_matrix = [
          [0, 0, 0, 0, -1, -1, 0],
          [0, 1, 1, 0, -1, -1, 0],
          [0, 1, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]
        ]
        s = code.paths(input_matrix)
        output_matrix = [
          [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None)],
          [(None, None), (3, -1), (3, -1), (None, None), (None, None), (None, None), (None, None)],
          [(None, None), (3, -1), (3, -1), (None, None),  (None, None),  (None, None), (None, None)],
          [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None)],
          [(None, None), (None, None), (None, None), (None, None), (None, None), (None, None)]
        ]
        self.assertEqual(s, output_matrix)

    def test_complex_input(self):
        input_matrix = [
            [-1,0,0,0,0,-1],
            [0,1,1,0,0,0],
            [0,1,1,0,0,0],
            [-1,0,0,0,0,0],
            [0,0,0,0,0,-1]
        ]

        output_matrix = [
            [(None,None), (None,None), (None,None), (None,None), (None,None), (None,None)],
            [(None,None), (-1,-1), (4,-1), (None,None), (None,None), (None,None), (None,None)],
            [(None,None), (1,1), (4,2), (None,None), (None,None), (None,None), (None,None)],
            [(None,None), (None,None), (None,None), (None,None), (None,None), (None,None)],
            [(None,None), (None,None), (None,None), (None,None), (None,None), (None,None)]
        ]
        s = code.paths(input_matrix)

        self.assertEqual(s, output_matrix)

    
    def test_linear_input(self):
        input_matrix = [
            [0,0,1,0,0,0,0,0],
            [0,1,0,0,0,-1,0,0],
            [0,1,0,0,0,0,-1,0],
            [0,0,0,0,0,0,-1, 0]
        ]
        output_matrix = [
            [(None, None),(None, None),(3,1) ,(None, None),(None, None),(None, None),(None, None),(None, None)],
            [(None, None),(5,1),(None, None),(None, None),(None, None),(None, None),(None, None),(None, None)],
            [(None, None),(5,1),(None, None),(None, None),(None, None),(None, None),(None, None),(None, None)],
            [(None, None),(None, None),(None, None),(None, None),(None, None),(None, None),(None, None), (None, None)]
        ]
        s = code.paths(input_matrix)

        self.assertEqual(s, output_matrix)


if __name__ == '__main__':
    unittest.main()
